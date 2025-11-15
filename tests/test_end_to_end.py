import hashlib
import logging
import unittest
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOGGER = logging.getLogger(__name__)


PROJECT_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_DIR / "processed"
FINAL_PATH = PROJECT_DIR / "db" / "final" / "Base_Final_Aurelion.csv"
FINAL_MD5 = FINAL_PATH.with_suffix(".md5")
FINAL_PARSE_DATES = ["fecha"]
LEGACY_ROOT_PATH = PROJECT_DIR / "Base_Final_Aurelion.csv"

DATA_SPECS = {
    "df_clientes_True": {
        "filename": "clientes_limpio.csv",
        "parse_dates": ["fecha_alta"],
    },
    "df_ventas_True": {
        "filename": "ventas_limpio.csv",
        "parse_dates": ["fecha"],
    },
    "df_detalle_ventas_True": {
        "filename": "detalle_ventas_limpio.csv",
        "parse_dates": [],
    },
    "df_productos_True": {
        "filename": "productos_limpio.csv",
        "parse_dates": [],
    },
}

PREFER_PROD_COLS = [
    "id_producto",
    "nombre_producto",
    "categoria",
    "marca",
    "subcategoria",
    "tipo_producto",
]

PREFER_CLI_COLS = [
    "id_cliente",
    "nombre_cliente",
    "segmento",
    "provincia",
    "ciudad",
    "region",
    "pais",
    "categoria_cliente",
]


def _load_processed_frames():
    frames = {}
    for var_name, spec in DATA_SPECS.items():
        csv_path = PROCESSED_DIR / spec["filename"]
        if not csv_path.exists():
            raise AssertionError(f"Missing processed artifact: {csv_path}")
        frames[var_name] = pd.read_csv(
            csv_path,
            parse_dates=spec.get("parse_dates") or [],
        )
    return frames


def _dimension_columns(source_df, prefer_list, existing_cols, key_col):
    cols = []
    for col in prefer_list:
        if col == key_col and col in source_df.columns:
            if col not in cols:
                cols.append(col)
        elif col in source_df.columns and col not in existing_cols:
            cols.append(col)
    if key_col not in cols and key_col in source_df.columns:
        cols.insert(0, key_col)
    if len(cols) == 1:
        extras = [
            c for c in source_df.columns if c not in existing_cols and c != key_col
        ]
        cols.extend(extras)
    return cols


def _build_base_consolidada(frames):
    df_detalle = frames["df_detalle_ventas_True"].copy()
    df_productos = frames["df_productos_True"].copy()
    df_ventas = frames["df_ventas_True"].copy()
    df_clientes = frames["df_clientes_True"].copy()

    if "FK_producto" in df_detalle.columns and "id_producto" not in df_detalle.columns:
        df_detalle = df_detalle.rename(columns={"FK_producto": "id_producto"})

    detalle_cols = list(df_detalle.columns)
    cols_prod = _dimension_columns(
        df_productos,
        PREFER_PROD_COLS,
        detalle_cols,
        "id_producto",
    )
    df_productos_dim = df_productos[cols_prod].copy()
    df_detalle_prod = df_detalle.merge(
        df_productos_dim,
        on="id_producto",
        how="left",
        validate="m:1",
    )

    ventas_cols = list(df_ventas.columns)
    cols_cli = _dimension_columns(
        df_clientes,
        PREFER_CLI_COLS,
        ventas_cols,
        "id_cliente",
    )
    df_clientes_dim = df_clientes[cols_cli].copy()
    df_ventas_cli = df_ventas.merge(
        df_clientes_dim,
        on="id_cliente",
        how="left",
        validate="m:1",
    )

    df_final = df_detalle_prod.merge(
        df_ventas_cli,
        on="id_venta",
        how="left",
        validate="m:1",
        suffixes=("", "_ventas"),
    )
    duplicated_cols = df_final.columns.duplicated()
    if duplicated_cols.any():
        df_final = df_final.loc[:, ~duplicated_cols]
    return df_final


def _finalize_base(base_consolidada):
    base_final = base_consolidada.copy()
    if base_final.duplicated().any():
        base_final = base_final.drop_duplicates()

    rename_map = {}
    for col in base_final.columns:
        if col.endswith("_x"):
            rename_map[col] = col[:-2]
        elif col.endswith("_y"):
            rename_map[col] = col[:-2]
    if rename_map:
        base_final = base_final.rename(columns=rename_map)

    duplicated_mask = base_final.columns.duplicated()
    if duplicated_mask.any():
        base_final = base_final.loc[:, ~duplicated_mask]

    id_cols = [c for c in base_final.columns if "id" in c.lower()]
    date_cols = [
        c for c in base_final.columns if "fecha" in c.lower() or "date" in c.lower()
    ]
    money_cols = [
        c
        for c in base_final.columns
        if any(x in c.lower() for x in ["precio", "importe", "monto", "total"])
    ]
    other_cols = [
        c for c in base_final.columns if c not in id_cols + date_cols + money_cols
    ]
    ordered_cols = [
        c for c in id_cols + date_cols + other_cols + money_cols if c in base_final.columns
    ]
    return base_final[ordered_cols].copy()


def _compute_md5(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class TestEndToEndPipeline(unittest.TestCase):
    def test_modular_pipeline_matches_export(self):
        frames = _load_processed_frames()
        base_consolidada = _build_base_consolidada(frames)
        base_final = _finalize_base(base_consolidada)

        self.assertFalse(
            LEGACY_ROOT_PATH.exists(),
            "Base_Final_Aurelion.csv no debe existir en la raíz del proyecto",
        )
        self.assertTrue(
            FINAL_PATH.exists(),
            "Base_Final_Aurelion.csv missing inside db/final",
        )
        exported_final = pd.read_csv(FINAL_PATH, parse_dates=FINAL_PARSE_DATES)
        pd.testing.assert_frame_equal(
            base_final.reset_index(drop=True),
            exported_final[base_final.columns].reset_index(drop=True),
            check_dtype=False,
            atol=1e-9,
            rtol=1e-9,
        )

        self.assertTrue(
            FINAL_MD5.exists(),
            "Base_Final_Aurelion.md5 missing next to db/final export",
        )
        expected_md5 = FINAL_MD5.read_text(encoding="utf-8").strip()
        computed_md5 = _compute_md5(FINAL_PATH)
        self.assertEqual(
            expected_md5,
            computed_md5,
            "Checksum mismatch for db/final/Base_Final_Aurelion.csv",
        )

        LOGGER.info(
            "E2E OK | registros=%s columnas=%s | CSV db/final=%s | md5=%s",
            len(base_final),
            len(base_final.columns),
            FINAL_PATH,
            expected_md5,
        )


if __name__ == "__main__":
    unittest.main()
