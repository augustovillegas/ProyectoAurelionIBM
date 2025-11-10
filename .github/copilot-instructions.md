## Copilot / AI agent instructions for Proyecto Aurelion

Purpose: help an AI coding agent be immediately productive in this repo by summarizing architecture, data flows, important files, and project-specific conventions.

- Big picture
  - This repository contains data-cleaning notebooks and a small console helper program for exploring documentation. The primary artifacts are:
    - `DOCUMENTACION.md` — canonical project description, data model, and analysis notes.
    - `limp_y_trans_*.ipynb` — Jupyter notebooks that perform cleaning and transformation per table (clientes, productos, ventas, detalle_ventas).
    - `db/` — target folder for cleaned exports (not always populated in VCS). Notebooks export cleaned tables as Excel files here.
    - `programa.py` — a lightweight CLI menu that prints sections from the in-repo documentation (used for quick checks and demos).

- Data flow and integration points (explicit)
  - Source files: root-level Excel files referenced in docs (`clientes.xlsx`, `productos.xlsx`, `ventas.xlsx`, `detalle_ventas.xlsx`).
  - Notebooks read source files, clean/transform data and export cleaned outputs using: `df.to_excel('db/<tabla>_limpio.xlsx', index=False)`.
  - Any code change that alters column names/types must preserve the exported filenames and columns, since notebooks, docs and downstream analysis expect those names.

- Project-specific conventions and patterns
  - Data format: .xlsx (not .csv). Prefer using pandas `read_excel` / `to_excel` in notebooks and scripts.
  - Filenames: cleaned files follow the `db/<tabla>_limpio.xlsx` pattern; refer to `DOCUMENTACION.md` before renaming.
  - Notebooks are the canonical ETL implementation for each table — prefer editing the corresponding notebook (`limp_y_trans_clientes.ipynb`, `limp_y_trans_productos.ipynb`, etc.) rather than creating parallel scripts unless adding a reusable module.
  - `programa.py` is demonstration-only (prints documentation sections). Do not convert it into a production service without adding argument parsing and tests.

- How to run locally (developer workflows)
  - Run the menu program: `python .\programa.py` (Windows PowerShell). It uses stdin prompts.
  - Open and run notebooks with Jupyter (Notebook or Lab). The notebooks will export cleaned `.xlsx` files into `db/` when their final cells are executed.
  - There is no project-wide build or test harness in the repository; check notebooks for import lists (common packages: pandas, matplotlib). Add a `requirements.txt` if you introduce dependencies.

- Useful code pointers (examples to reference)
  - `programa.py` — shows the documentation sections and explains which files/data are expected. Use it to confirm naming conventions.
  - `DOCUMENTACION.md` — contains the data model, table columns and relationships (clients 1:N ventas, ventas 1:N detalle_ventas, productos 1:N detalle_ventas).
  - `limp_y_trans_*.ipynb` — ETL steps and export calls; adopt the same column names and export locations when adding new scripts.

- AI agent behavior rules (practical, repo-specific)
  - Preserve file and column names found in `DOCUMENTACION.md` and `programa.py` unless you also update the docs and notebooks consistently.
  - When proposing changes that touch data exports, include a one-line migration note (e.g., update notebooks to write `db/<new_name>_limpio.xlsx`) and list affected notebooks.
  - Prefer small, reversible edits: notebooks are the source of truth for ETL; changing them requires running the notebook to validate output.

- When to ask the human
  - If a change will rename or remove a cleaned data file under `db/`, ask before applying edits.
  - If you need to add new dependencies, confirm whether to add a `requirements.txt` and which Python version to target.

If anything here is unclear or you want more coverage (tests, CI, dependency pinning), tell me which area to expand next.
