# 📘 Proyecto Aurelion - Documentación

# 1° demo: asincrónica

## 1. Tema, problema y solución
**Tema:** Gestión y análisis de datos de ventas minoristas.  
**Problema:** Las pequeñas tiendas suelen carecer de herramientas de análisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.  
**Solución:** Desarrollar un sistema basado en bases de datos que consolide información de clientes, productos y transacciones, permitiendo generar reportes de rendimiento, productos más vendidos y comportamiento de compra.

---

## 2. Dataset de referencia
**Fuente:** Datos generados con fines educativos, provista por Guayerd & IBM.  
**Definición:** Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y el detalle de cada operación.  
**Archivos utilizados:**
- `clientes.xlsx`: información demográfica y de contacto de los clientes.
- `productos.xlsx`: catálogo de productos disponibles.
- `ventas.xlsx`: encabezado general de las operaciones realizadas.
- `detalle_ventas.xlsx`: detalle línea a línea de cada venta.

**Resumen de función:**
Cada archivo cumple un rol complementario dentro de la base. Las relaciones principales son:
- `clientes` (1:N) `ventas`
- `ventas` (1:N) `detalle_ventas`
- `productos` (1:N) `detalle_ventas`

---

## 3. Estructura por tabla

### **Tabla: clientes (clientes.xlsx)**
| Columna         | Tipo de dato  | Escala de medición  | Descripción                     |
|-----------------|---------------|---------------------|---------------------------------|
| id_cliente      | int           | Nominal             | Identificador único del cliente |
| nombre_cliente  | str           | Nominal             | Nombre completo del cliente     |
| email           | str           | Nominal             | Correo de contacto              |
| ciudad          | str           | Nominal             | Ciudad de residencia            |
| fecha_alta      | date          | Intervalo           | Fecha de alta                   |

### **Tabla: productos (productos.xlsx)**
| Columna         | Tipo de dato  | Escala de medición  | Descripción                  |
|-----------------|---------------|---------------------|------------------------------|
| id_producto     | int           | Nominal             | Identificador del producto   |
| nombre_producto | str           | Nominal             | Nombre del producto          |
| categoría       | str           | Nominal             | Categoría o tipo de producto |
| precio_unitario | float         | De razón            | Precio unitario del producto |

### **Tabla: ventas (ventas.xlsx)**
| Columna         | Tipo de dato  | Escala de medición  | Descripción                  |
|-----------------|---------------|---------------------|------------------------------|
| id_venta        | int           | Nominal             | Identificador de la venta    | 
| fecha           | date          | Intervalo           | Fecha de concreción de venta |
| id_cliente      | int           | Nominal             | Cliente asociado a la venta  |
| nombre_cliente  | str           | Nominal             | Nombre completo de cliente   |
| email           | str           | Nominal             | correo decontacto de cliente |
| medio_pago      | str           | Nominal             | Metodo de pago utilizado     |

### **Tabla: detalle_ventas (detalle_ventas.xlsx)**
| Columna         | Tipo de dato  | Escala de medición  | Descripción                  |
|-----------------|---------------|---------------------|------------------------------|
| id_venta        | int           | Nominal             | Venta asociada               |
| id_producto     | int           | Nominal             | Producto vendido             |
| nombre_producto | str           | Nominal             | Nombre del producto          |
| cantidad        | int           | De razón            | Cantidad del mismo producto  |
| precio_unitario | int           | De razón            | Precio unitario del producto |
| importe         | float         | De razón            | Subtotal por producto        |

---

## 4. Escalas de medición
| Escala       | Descripción                                    | Ejemplo                                 |
|--------------|------------------------------------------------|-----------------------------------------|
| Nominal      | Categorización sin orden.                      | Nombre del cliente, categ, del producto.|
| Ordinal      | Datos con orden lógico, sin distancia exacta.  | Fecha de venta.                         |
| De intervalo | Diferencias medibles pero sin cero absoluto.   | Fecha de alta o fecha de venta.         |
| De razón     | Datos numéricos con cero absoluto y proporción.| Precio, cantidad, total de venta.       |

---

## 5. Sugerencias y mejoras con Copilot
- Generar automáticamente consultas SQL para métricas clave (productos más vendidos, clientes top, ventas por mes).  
- Sugerir visualizaciones con librerías como **Matplotlib** o **Power BI**.  
- Implementar detección de anomalías en ventas con **IA de GitHub Copilot**.  
- Crear scripts automáticos de carga y limpieza de datos (ETL).  
- Sugerir nombres de funciones y optimización de código en VS Code.  

---

## 6. Salir
**Fin del documento — Proyecto Aurelion**
