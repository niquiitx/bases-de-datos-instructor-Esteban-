# Análisis Conceptual – Basado en el artículo de Devart

## 1. Problema que resuelve la normalización y su importancia en sistemas empresariales

La normalización elimina redundancias en los datos y previene inconsistencias causadas por la duplicación de información.  
En entornos empresariales, esto es fundamental para garantizar datos organizados, confiables y fácilmente actualizables.  
Por ejemplo, si un cliente cambia su dirección, en una base de datos normalizada el cambio se realiza una sola vez y se refleja automáticamente en todo el sistema.

---

## 2. Diferencias entre 1NF, 2NF y 3NF

**Primera Forma Normal (1NF):** Cada atributo debe contener un solo valor. No se permiten listas ni datos combinados.  
*Ejemplo:* Una celda con “Mesa, Silla, Sofá” viola la 1NF, ya que contiene múltiples valores.

**Segunda Forma Normal (2NF):** Cumple la 1NF, pero además exige que los atributos no clave dependan completamente de la clave primaria.  
*Ejemplo:* Si la clave es (ID_Pedido, ID_Producto) y el nombre del producto depende solo del ID_Producto, existe una dependencia parcial que debe eliminarse separando los datos.

**Tercera Forma Normal (3NF):** Cumple la 2NF y elimina dependencias transitivas, asegurando que ningún atributo no clave dependa de otro atributo no clave.  
*Ejemplo:* Si “Ciudad” depende de “Código Postal”, y este a su vez depende del cliente, se requiere una tabla adicional para separar esa dependencia.

---

## 3. Normalización: impacto en integridad y rendimiento

La normalización mejora la integridad de los datos dividiendo grandes tablas en entidades más pequeñas como “Clientes”, “Pedidos” y “Productos”.  
Sin embargo, puede afectar el rendimiento, ya que las consultas requieren más operaciones JOIN para combinar información, aumentando los tiempos de respuesta en bases con grandes volúmenes de datos.

---

## 4. Rol e identificación de las dependencias funcionales

Las dependencias funcionales determinan qué atributos dependen de otros dentro de una tabla.  
Por ejemplo, ID_Cliente → (Nombre, Correo) indica que el identificador del cliente determina los demás campos.  
Estas dependencias se identifican observando patrones de repetición y son esenciales para aplicar correctamente las formas normales.

---

## 5. Desnormalización: cuándo aplicarla

La desnormalización se emplea cuando se prioriza la velocidad de consulta sobre la estructura ideal de datos.  
Por ejemplo, en sistemas de reportes donde hay muchas lecturas y pocas escrituras, se permite cierta redundancia para optimizar la eficiencia de las consultas.

---

# Parte 2: Fred’s Furniture

## Reto 1 – Diagnóstico inicial

La tabla original `furniture_sales` contenía información de ventas, productos, clientes y vendedores en una sola estructura, generando redundancia y pérdida de consistencia.

**Anomalías detectadas:**  
- **Inserción:** No se podían registrar nuevos clientes o productos sin una venta.  
- **Actualización:** Un cambio en los datos de un vendedor debía repetirse en múltiples filas.  
- **Eliminación:** Borrar una venta implicaba eliminar información de clientes o productos relacionados.

**Solución aplicada:**  
Se normalizó la base de datos hasta la **Tercera Forma Normal (3NF)** para eliminar redundancias y asegurar la integridad referencial.

---

## Reto 2 – Aplicación de la Primera Forma Normal (1NF)

**Objetivo:** Garantizar que cada campo contuviera un valor único y eliminar datos agrupados o repetidos.

**Acciones realizadas:**  
- Se identificaron las entidades principales: `Clientes`, `Productos`, `Vendedores`, `Ventas` y `Detalles de Venta`.  
- Se crearon tablas independientes para cada entidad, asegurando la atomicidad de los datos.

**Código SQL:**

```sql
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_address VARCHAR(200)
);

CREATE TABLE Salespersons (
    salesperson_id INT AUTO_INCREMENT PRIMARY KEY,
    salesperson_name VARCHAR(100),
    salesperson_phone VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE,
    customer_id INT,
    salesperson_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (salesperson_id) REFERENCES Salespersons(salesperson_id)
);

CREATE TABLE Sale_Details (
    sale_id INT,
    product_id INT,
    quantity INT,
    total DECIMAL(10,2),
    PRIMARY KEY (sale_id, product_id),
    FOREIGN KEY (sale_id) REFERENCES Sales(sale_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
```

---

## Reto 3 – Aplicación de la Segunda Forma Normal (2NF)

**Objetivo:** Eliminar dependencias parciales, garantizando que todos los atributos no clave dependan completamente de la clave primaria.

**Acciones realizadas:**  
- Se identificaron dependencias parciales en `Sale_Details`.  
- Se crearon tablas adicionales para reflejar las relaciones correctas y eliminar dependencias parciales.

**Código SQL:**

```sql
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100)
);

ALTER TABLE Products
ADD COLUMN category_id INT,
ADD FOREIGN KEY (category_id) REFERENCES Categories(category_id);
```

---

## Reto 4 – Aplicación de la Tercera Forma Normal (3NF)

**Objetivo:** Eliminar dependencias transitivas entre atributos no clave.

**Acciones realizadas:**  
- Se identificaron dependencias transitivas en `Products`.  
- Se reorganizaron las tablas para garantizar independencia entre atributos no clave.

**Código SQL:**

```sql
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);
```

**Diagrama E-R final:**  
![alt text](image.png)

---

## Reglas de Negocio

1. Cada venta debe estar asociada a un cliente y a un vendedor.  
2. Cada detalle de venta debe vincular un producto con una venta específica.  
3. La cantidad de productos vendidos debe ser un número entero positivo.  
4. El total de la venta se calcula como `precio × cantidad`.  
5. Cada producto pertenece a una categoría específica.  
6. El precio del producto debe ser un valor numérico positivo.  
7. No se permiten productos duplicados con el mismo nombre en una categoría.  
8. Los datos de clientes y vendedores deben mantenerse actualizados en todas las ventas asociadas.  
9. No se permiten ventas sin productos asociados.  
10. Cada categoría debe tener un nombre único.

---

## Justificación del Diseño

1. **Eliminación de redundancias y anomalías:**  
   La normalización hasta la 3FN permitió eliminar duplicaciones, asegurando integridad y coherencia.  

2. **Integridad referencial:**  
   Las claves primarias y foráneas garantizan relaciones consistentes entre las entidades.  

3. **Rendimiento optimizado:**  
   Aunque la normalización incrementa el número de tablas, mejora la eficiencia general de las consultas y el mantenimiento.  

4. **Escalabilidad:**  
   La estructura modular facilita futuras expansiones sin alterar la base existente.  

5. **Cumplimiento de las formas normales:**  
   Se aplicaron rigurosamente las tres primeras formas normales, garantizando eficiencia, consistencia y mantenimiento sostenible.

---

# Parte 3: Proyecto Personal – Sistema de Gestión Bibliotecaria

## Descripción General

Este proyecto consiste en el diseño e implementación de una base de datos relacional para la administración de libros, usuarios y préstamos en una biblioteca.  
El sistema está modelado hasta la 3FN para asegurar integridad, consistencia y eficiencia en las operaciones de almacenamiento y consulta.

---

## Modelo E-R Conceptual y Lógico

![alt text](image-1.png)

---

## Reglas de Negocio

1. Cada usuario tiene un identificador único (`id_usuario`).  
2. Cada libro se identifica mediante un `isbn` único.  
3. Relación muchos a muchos entre libros y autores (tabla intermedia `libro_autor`).  
4. Cada libro pertenece a una categoría (`id_categoria`).  
5. Cada préstamo vincula un usuario con un libro, con fechas de préstamo y devolución.  
6. La fecha de devolución debe ser posterior a la fecha de préstamo.  
7. Se implementan claves foráneas para mantener la integridad referencial.

---

## Justificación del Diseño

- **Normalización hasta la 3FN:** Eliminación de redundancias y dependencias indeseadas.  
- **Uso de claves primarias y foráneas:** Relaciones consistentes entre entidades.  
- **Relación muchos a muchos:** Implementada mediante tabla intermedia para evitar duplicación.  
- **Optimización de consultas:** Permite búsquedas eficientes por categoría, autor o usuario.  
- **Escalabilidad:** Estructura modular y fácilmente ampliable.

---

**Autor:** Proyecto académico – Normalización y modelado relacional  
**Versión:** 1.1  
**Licencia:** Uso educativo
