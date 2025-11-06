# Proyecto Aurelion - Documentacion

## Demo 1 (asincronica)

### 1. Tema, problema y solucion
**Tema:** Gestion y analisis de datos de ventas minoristas.  
**Problema:** Las pequenas tiendas suelen carecer de herramientas de analisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.  
**Solucion:** Desarrollar un sistema basado en bases de datos que consolide informacion de clientes, productos y transacciones, permitiendo generar reportes de rendimiento, productos mas vendidos y comportamiento de compra.

---

### 2. Dataset de referencia
**Fuente:** Datos generados con fines educativos, provistos por Guayerd e IBM.  
**Definicion:** Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y detalle de cada operacion.  
**Archivos utilizados:**
- `clientes.xlsx`: informacion demografica y de contacto de los clientes.
- `productos.xlsx`: catalogo de productos disponibles.
- `ventas.xlsx`: encabezado general de las operaciones realizadas.
- `detalle_ventas.xlsx`: detalle linea a linea de cada venta.

**Relaciones principales:**
- `clientes` (1:N) `ventas`
- `ventas` (1:N) `detalle_ventas`
- `productos` (1:N) `detalle_ventas`

---

### 3. Estructura por tabla

**Tabla: clientes (clientes.xlsx)**
| Columna        | Tipo | Escala    | Descripcion                  |
|----------------|------|-----------|------------------------------|
| id_cliente     | int  | Nominal   | Identificador unico del cliente |
| nombre_cliente | str  | Nominal   | Nombre completo del cliente  |
| email          | str  | Nominal   | Correo de contacto           |
| ciudad         | str  | Nominal   | Ciudad de residencia         |
| fecha_alta     | date | Intervalo | Fecha de alta                |

**Tabla: productos (productos.xlsx)**
| Columna         | Tipo | Escala | Descripcion                 |
|-----------------|------|--------|-----------------------------|
| id_producto     | int  | Nominal| Identificador del producto  |
| nombre_producto | str  | Nominal| Nombre del producto         |
| categoria       | str  | Nominal| Categoria o tipo de producto|
| precio_unitario | int  | Razon  | Precio unitario del producto|

**Tabla: ventas (ventas.xlsx)**
| Columna        | Tipo | Escala    | Descripcion                |
|----------------|------|-----------|----------------------------|
| id_venta       | int  | Nominal   | Identificador de la venta  |
| fecha          | date | Intervalo | Fecha de concrecion        |
| id_cliente     | int  | Nominal   | Relacion con clientes      |
| nombre_cliente | str  | Nominal   | Nombre completo del cliente|
| email          | str  | Nominal   | Contacto del cliente       |
| medio_pago     | str  | Nominal   | Medio de pago utilizado    |

**Tabla: detalle_ventas (detalle_ventas.xlsx)**
| Columna         | Tipo | Escala | Descripcion                 |
|-----------------|------|--------|-----------------------------|
| id_venta        | int  | Nominal| Venta asociada              |
| id_producto     | int  | Nominal| Producto vendido            |
| nombre_producto | str  | Nominal| Nombre del producto         |
| cantidad        | int  | Razon  | Cantidad adquirida          |
| precio_unitario | int  | Razon  | Precio unitario             |
| importe         | int  | Razon  | Subtotal por linea          |

---

### 4. Escalas de medicion
| Escala    | Descripcion                                 | Ejemplo                                |
|-----------|---------------------------------------------|----------------------------------------|
| Nominal   | Categorias sin orden                        | Ciudad, categoria, medio de pago       |
| Ordinal   | Datos con orden sin distancia uniforme      | Prioridad de clientes (si existiera)   |
| Intervalo | Diferencias con cero arbitrario             | Fechas de alta o de venta              |
| Razon     | Diferencias y cocientes con cero absoluto   | Cantidad, precio, importe              |

---

### 5. Sugerencias y mejoras con Copilot
- Generar consultas SQL para metricas clave (productos mas vendidos, clientes destacados, ventas mensuales).
- Sugerir visualizaciones con Matplotlib o Power BI.
- Disenar procesos automatizados de limpieza (ETL) y deteccion de anomalias.
- Proponer nombres de funciones y refactorizaciones en VS Code con Copilot.

---

## Demo 2 (sincronica)

### 1. Estado de requerimientos
| Entregable | Detalle | Estado |
|------------|---------|--------|
| Documentacion (.md) | Se agregaron estadisticas, distribuciones, correlaciones, outliers, graficos e interpretaciones. | Cumplido |
| Notebooks (.ipynb) | Se extendio el flujo de analisis en `limp_y_trans_detalle_ventas.ipynb` con celdas descriptivas y visualizaciones. | Cumplido |
| Base de datos (.xlsx) | Las tablas limpias pueden exportarse desde los notebooks (ver ultima celda) para analisis directo. | Listo para exportar |
| Programa (.py) | Menu actualizado con las nuevas secciones informativas del proyecto. | Cumplido |

---

### 2. Dataset trabajado en esta iteracion
- Se integraron `ventas`, `detalle_ventas` y `productos` para analizar comportamiento de ingresos a nivel linea y por mes.
- El dataset final (`df_detalle_ventas_limpio`) conserva 343 filas y 6 columnas, sin valores nulos ni duplicados.
- Se normalizaron nombres, tipos de datos y medios de pago para permitir agregaciones directas.

---

### 3. Estadisticas descriptivas principales
| Variable         | Conteo | Media  | Desvio | Min | Q1    | Mediana | Q3     | Max    |
|------------------|--------|--------|--------|-----|-------|---------|--------|--------|
| cantidad         | 343    | 2.96   | 1.37   | 1   | 2.00  | 3.00    | 4.00   | 5.00   |
| precio_unitario  | 343    | 2654.50| 1308.69| 272 | 1618.5| 2512.00 | 3876.0 | 4982.0 |
| importe          | 343    | 7730.08| 5265.54| 272 | 3489.0| 6702.00 | 10231.5| 24865.0|

- La dispersion confirma ventas con importes concentrados entre 3.5k y 10.2k ARS, con compras maximas cercanas a 25k ARS.
- Las mediciones se tomaron sobre variables numericas luego de estandarizar tipos y formatos.

---

### 4. Distribucion de variables
- `importe` presenta asimetria positiva (skew 0.87), lo que indica una cola derecha con ventas de alto valor poco frecuentes.
- Las cantidades vendidas mantienen una distribucion casi uniforme (skew 0.06), apoyando ofertas de unidades moderadas.
- El histograma con densidad (ver visualizacion) confirma la concentracion de importes en el rango medio y pocos extremos.

---

### 5. Correlaciones entre variables
|                | cantidad | precio_unitario | importe |
|----------------|----------|-----------------|---------|
| cantidad       | 1.00     | -0.07           | 0.60    |
| precio_unitario| -0.07    | 1.00            | 0.68    |
| importe        | 0.60     | 0.68            | 1.00    |

- La correlacion positiva fuerte entre `precio_unitario` e `importe` demuestra que los precios altos elevan el ticket, incluso con pocas unidades.
- `cantidad` tambien contribuye al importe, aunque con menor magnitud por la oferta equilibrada de unidades.

---

### 6. Deteccion de outliers (criterio IQR)
| id_venta | Producto                     | Medio de pago   | Cantidad | Importe (ARS) |
|----------|------------------------------|-----------------|----------|---------------|
| 16       | Barrita de Cereal 30g        | efectivo        | 5        | 22150         |
| 21       | Pizza Congelada Muzzarella   | transferencia   | 5        | 21430         |
| 50       | Caramelos Masticables        | transferencia   | 5        | 23760         |
| 63       | Energetica Nitro 500ml       | tarjeta         | 5        | 21090         |
| 75       | Pepsi 1.5L                   | qr              | 5        | 24865         |
| 94       | Jugo en Polvo Limon          | qr              | 5        | 20450         |
| 110      | Jugo de Naranja 1L           | efectivo        | 5        | 20850         |

- Todos los outliers comparten pedidos de 5 unidades; se recomienda evaluar promociones que incentivan volumen para confirmar si responden a campanas especificas.

---

### 7. Visualizaciones clave

![Ingresos por mes](data:image/png;base64,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)

---

### 8. Interpretacion orientada al problema
- Las categorias de limpieza y alimentos concentran el ingreso mensual, con picos en enero, mayo y junio por encima de 500k ARS, lo que orienta campanas de abastecimiento para esos meses.
- Los medios de pago electronicos (QR y transferencia) superan el tercio de la facturacion, validando la continuidad de promociones sin contacto.
- Los outliers corresponden a compras por volumen completo (5 unidades) y refuerzan la necesidad de monitorear bundles o packs especiales.
- La combinacion de precio unitario alto y multiples unidades explica los tickets destacados; la estrategia debe equilibrar promociones sin erosionar margen.

---

### 9. Base de datos limpia y disponible
- Celdas finales del notebook guardan los dataframes limpios mediante `df.to_excel('db/<tabla>_limpio.xlsx', index=False)` para su consumo directo.
- Cada tabla fue estandarizada (tipos, duplicados y formatos), por lo que las exportaciones mantienen coherencia con los informes de esta demo.
- Se documentaron en el notebook las rutas y validaciones necesarias para replicar la generacion de archivos `.xlsx` en el entorno de trabajo.

---

## Demo 3 (proximos pasos sugeridos)
- Integrar tablas en un modelo dimensional que facilite dashboards.
- Explorar segmentacion de clientes con tecnicas de clustering.
- Automatizar actualizaciones periodicas mediante jobs programados.

---

## Cierre
**Proyecto Aurelion** mantiene coherencia entre documentacion, notebooks y programa de consulta en consola, garantizando un repositorio ordenado y listo para la siguiente iteracion.
