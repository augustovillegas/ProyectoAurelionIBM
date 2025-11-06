# Proyecto Aurelion - Pseudocódigo en Python (con actualización de documentación Demo 2)

# Paso 1: Cargar en memoria los textos de la documentación
documentacion = {
    1: """Tema, problema y solución
Tema: Gestión y análisis de datos de ventas minoristas.
Problema: Las pequeñas tiendas suelen carecer de herramientas de análisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.
Solución: Desarrollar un sistema basado en bases de datos que consolide información de clientes, productos y transacciones, permitiendo generar reportes de rendimiento, productos más vendidos y comportamiento de compra.
""",
    2: """Dataset de referencia
Fuente: Datos generados con fines educativos, provista por Guayerd & IBM.
Definición: Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y el detalle de cada operación.
Archivos utilizados:
- clientes.xlsx: información demográfica y de contacto de los clientes.
- productos.xlsx: catálogo de productos disponibles.
- ventas.xlsx: encabezado general de las operaciones realizadas.
- detalle_ventas.xlsx: detalle línea a línea de cada venta.

Resumen de función:
Cada archivo cumple un rol complementario dentro de la base. Las relaciones principales son:
- clientes (1:N) ventas
- ventas (1:N) detalle_ventas
- productos (1:N) detalle_ventas
""",
    3: """Estructura por tabla

Tabla: clientes (clientes.xlsx)
| Columna         | Tipo de dato  | Escala de medición  | Descripción                     |
|-----------------|---------------|---------------------|---------------------------------|
| id_cliente      | int           | Nominal             | Identificador único del cliente |
| nombre_cliente  | str           | Nominal             | Nombre completo del cliente     |
| email           | str           | Nominal             | Correo de contacto              |
| ciudad          | str           | Nominal             | Ciudad de residencia            |
| fecha_alta      | date          | Intervalo           | Fecha de alta                   |

Tabla: productos (productos.xlsx)
| Columna         | Tipo de dato  | Escala de medición  | Descripción                  |
|-----------------|---------------|---------------------|------------------------------|
| id_producto     | int           | Nominal             | Identificador del producto   |
| nombre_producto | str           | Nominal             | Nombre del producto          |
| categoría       | str           | Nominal             | Categoría o tipo de producto |
| precio_unitario | float         | De razón            | Precio unitario del producto |

Tabla: ventas (ventas.xlsx)
| Columna         | Tipo de dato  | Escala de medición  | Descripción                  |
|-----------------|---------------|---------------------|------------------------------|
| id_venta        | int           | Nominal             | Identificador de la venta    | 
| fecha           | date          | Intervalo           | Fecha de concreción de venta |
| id_cliente      | int           | Nominal             | Cliente asociado a la venta  |
| nombre_cliente  | str           | Nominal             | Nombre completo de cliente   |
| email           | str           | Nominal             | Correo de contacto de cliente|
| medio_pago      | str           | Nominal             | Método de pago utilizado     |

Tabla: detalle_ventas (detalle_ventas.xlsx)
| Columna         | Tipo de dato  | Escala de medición  | Descripción                  |
|-----------------|---------------|---------------------|------------------------------|
| id_venta        | int           | Nominal             | Venta asociada               |
| id_producto     | int           | Nominal             | Producto vendido             |
| nombre_producto | str           | Nominal             | Nombre del producto          |
| cantidad        | int           | De razón            | Cantidad del mismo producto  |
| precio_unitario | int           | De razón            | Precio unitario del producto |
| importe         | float         | De razón            | Subtotal por producto        |
""",
    4: """Escalas de medición
| Escala       | Descripción                                    | Ejemplo                                 |
|--------------|------------------------------------------------|-----------------------------------------|
| Nominal      | Categorización sin orden.                      | Nombre del cliente, categ. del producto.|
| Ordinal      | Datos con orden lógico, sin distancia exacta.  | (No aplica en variables numéricas del set)|
| De intervalo | Diferencias medibles pero sin cero absoluto.   | Fecha de alta o fecha de venta.         |
| De razón     | Datos numéricos con cero absoluto y proporción.| Precio, cantidad, total de venta.       |
""",
    5: """Sugerencias y mejoras con Copilot
- Generar automáticamente consultas SQL para métricas clave (productos más vendidos, clientes top, ventas por mes).
- Sugerir visualizaciones con librerías como Matplotlib o Power BI.
- Implementar detección de anomalías en ventas con IA de GitHub Copilot.
- Crear scripts automáticos de carga y limpieza de datos (ETL).
- Sugerir nombres de funciones y optimización de código en VS Code.
""",    
    6: """Actualización Demo 2: formato de base de datos (.xlsx)
- La documentación fue actualizada para reflejar la extensión correcta: **.xlsx** en lugar de .csv.
- Los ejemplos de exportación utilizan ahora:  `df.to_excel('db/<tabla>_limpio.xlsx', index=False)`
- Archivos esperados:
  • clientes.xlsx
  • productos.xlsx
  • ventas.xlsx
  • detalle_ventas.xlsx

Consulta: 'DOCUMENTACION_actualizado.md' para el detalle.
Ruta sugerida: ./DOCUMENTACION_actualizado.md
""",
    7: """Estado de análisis (resumen de secciones incluidas en la documentación)
- Estadísticas descriptivas básicas: documentadas en el .md.
- Identificación del tipo de distribución de variables: documentada en el .md.
- Correlaciones entre variables principales: documentadas en el .md.
- Detección de outliers (valores extremos): documentada en el .md.
- Interpretación de resultados orientada al problema: documentada en el .md.

Nota: Las visualizaciones deben referenciarse desde el .md (sección "Visualizaciones clave").
""",
    8: """Visualizaciones clave (referencia)
- Ver sección "Visualizaciones clave" en la documentación.
- Mantener, sin cambiar la estructura del documento, al menos tres gráficos exportados desde los notebooks.
- Recomendación de consistencia: títulos y ejes alineados con las variables descritas en el .md.
Rutas sugeridas de imágenes (según exportes del notebook):
  ./figs/hist_importe.png
  ./figs/heatmap_correlaciones.png
  ./figs/ingresos_por_mes.png
(Estas rutas son orientativas; usar las que existan en tu proyecto.)
""",
    9: """Rutas de archivos y entrega
- Documentación actualizada: ./DOCUMENTACION_actualizado.md
- Datos fuente: ./clientes.xlsx, ./productos.xlsx, ./ventas.xlsx, ./detalle_ventas.xlsx
- Datos limpios (exportados desde notebooks): ./db/<tabla>_limpio.xlsx
- Notebooks de limpieza/transformación: 
  • limp_y_trans_clientes.ipynb
  • limp_y_trans_productos.ipynb
  • limp_y_trans_ventas.ipynb
  • limp_y_trans_detalle_ventas.ipynb

Esta sección se limita a listar rutas esperadas, sin lógica adicional.
"""
}

# Mostrar el menú principal
def mostrar_menu():
    print("\n===== MENÚ DOCUMENTACIÓN AURELION =====")
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia")
    print("3. Estructura por tabla (tipo y escala)")
    print("4. Escalas de medición")
    print("5. Sugerencias y mejoras con Copilot")   
    print("6. Actualización Demo 2 (.xlsx y exportación)")
    print("7. Estado de análisis (resumen)")
    print("8. Visualizaciones clave (referencia)")
    print("9. Rutas de archivos y entrega")
    print("10. Salir")

# Paso 3 y 4: Control del flujo
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion in documentacion:
                print("\n--- Sección", opcion, "---")
                print(documentacion[opcion])
            elif opcion == 10:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
        else:
            print("Por favor, ingrese un número válido.")

# Inicio del programa
if __name__ == "__main__":
    main()

