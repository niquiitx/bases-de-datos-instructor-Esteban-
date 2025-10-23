#  Práctica: Gestión de Contenedores de Bases de Datos con Docker (CMD)

##  Descripción General

En esta actividad se levantaron tres contenedores de bases de datos utilizando **Docker desde la línea de comandos (CMD)**, sin emplear Docker Desktop ni Docker Compose.  
Cada contenedor fue posteriormente conectado a tres diferentes clientes gráficos de bases de datos: **DBeaver**, **HeidiSQL** y **Beekeeper Studio**, para crear bases de datos de prueba.

---

##  Objetivos

- Implementar contenedores independientes de **MySQL**, **MariaDB** y **PostgreSQL** desde la terminal.
- Conectarse a cada contenedor mediante clientes SQL de escritorio.
- Crear bases de datos dentro de cada contenedor.
- Documentar y evidenciar el proceso con capturas de pantalla y descripciones.

---

##  Requisitos Previos

- Docker instalado y funcionando correctamente.  
- Clientes SQL instalados:  
  - [DBeaver](https://dbeaver.io/download/)
  - [HeidiSQL](https://www.heidisql.com/download.php)
  - [Beekeeper Studio](https://www.beekeeperstudio.io/)
- Puertos disponibles:  
  - MySQL → **3306**  
  - MariaDB → **3307** (puede modificarse si hay conflicto)  
  - PostgreSQL → **5432**

---

##  1. Creación de Contenedores desde CMD

A continuación se muestran los comandos utilizados para crear los tres contenedores.

###  MySQL
```bash
docker run -d --name mysql_container -e MYSQL_ROOT_PASSWORD=admin -p 3306:3306 mysql:latest
```

###  MariaDB
```bash
docker run -d --name mariadb_container -e MARIADB_ROOT_PASSWORD=admin -p 3307:3306 mariadb:latest
```

###  PostgreSQL
```bash
docker run -d --name postgres_container -e POSTGRES_PASSWORD=admin -p 5432:5432 postgres:latest
```

 **Evidencia 1:** Creación de contenedores desde CMD  
![Creación de contenedores]
![alt text](image-1.png)

---

##  2. Verificación del Estado de los Contenedores

Comando para verificar que todos los contenedores estén activos:

```bash
docker ps
```
 **Evidencia 2:** Contenedores activos en ejecución.  
![Contenedores activos] ![alt text](image-2.png)

---

##  3. Conexión desde Clientes SQL

Cada contenedor fue conectado desde los siguientes clientes para crear tres bases de datos distintas:

| Cliente SQL | Base de datos creada | Contenedor conectado | Puerto |
|--------------|----------------------|----------------------|--------|
| DBeaver | `db_dbeaver` | MySQL / MariaDB / PostgreSQL | 3306 / 3307 / 5432 |
| HeidiSQL | `db_heidisql` | MySQL / MariaDB / PostgreSQL | 3306 / 3307 / 5432 |
| Beekeeper Studio | `db_beekeeper` | MySQL / MariaDB / PostgreSQL | 3306 / 3307 / 5432 |

---

###  Conexión en DBeaver

1. Abrir DBeaver → Crear nueva conexión.
2. Seleccionar el tipo de base de datos (MySQL, MariaDB o PostgreSQL).
3. Ingresar los datos de conexión:

| Campo | Valor |
|--------|--------|
| Host | localhost |
| Puerto | 3306 / 3307 / 5432 |
| Usuario | root / postgres |
| Contraseña | admin |

4. Probar conexión y guardar.

 **Evidencia 3:** Conexión exitosa desde DBeaver.  
![Conexión DBeaver]![alt text](image-3.png)

 **Evidencia 4:** Creación de base de datos `db_dbeaver`.  
![Base DBeaver]![alt text](image-4.png)

---

###  Conexión en HeidiSQL

1. Abrir HeidiSQL → Nueva sesión.
2. Elegir tipo de base de datos (MySQL o MariaDB).
3. Configurar la conexión con los mismos parámetros anteriores.
4. Conectarse y crear la base de datos `db_heidisql`.

 **Evidencia 5:** Conexión exitosa desde HeidiSQL.  
![Conexión HeidiSQL]![alt text](image-5.png)

 **Evidencia 6:** Creación de base de datos `db_heidisql`.  
![Base HeidiSQL]![alt text](image-6.png)
![alt text](image-7.png)

---

### 🔹 Conexión en Beekeeper Studio

1. Abrir Beekeeper Studio → “New Connection”.
2. Seleccionar el motor de base de datos.
3. Configurar host, puerto, usuario y contraseña.
4. Guardar y conectar.
5. Crear la base de datos `db_beekeeper`.

 

 **Evidencia 7:** Creación de base de datos `db_beekeeper`.  
![Base Beekeeper]![alt text](image-8.png)

---

## 🧩 4. Verificación Final desde CMD

Para listar los contenedores activos:
```bash
docker ps
```

Para ingresar a un contenedor y listar las bases de datos:

### MySQL / MariaDB
```bash
docker exec -it mysql_container mysql -u root -p
SHOW DATABASES;
```

### PostgreSQL
```bash
docker exec -it postgres_container psql -U postgres
\l
```

 **Evidencia 8:** Listado de bases de datos dentro de cada contenedor.  
![Bases de datos listadas]![alt text](image-9.png)

---

##  Observaciones y Conclusiones

- Los tres contenedores se levantaron correctamente utilizando únicamente la **línea de comandos**.
- La conexión desde diferentes clientes demuestra la **interoperabilidad de Docker** con herramientas externas.
- Cada contenedor mantuvo su entorno aislado, mostrando la ventaja del **aislamiento de servicios**.
- Docker facilita la gestión simultánea de múltiples bases de datos sin conflictos de dependencias.

---

##  Estructura del Repositorio

```
├── README.md
├── /screenshots
│   ├── cmd_containers.png
│   ├── docker_ps.png
│   ├── dbeaver_connection.png
│   ├── dbeaver_db.png
│   ├── heidisql_connection.png
│   ├── heidisql_db.png
│   ├── beekeeper_connection.png
│   ├── beekeeper_db.png
│   └── db_list.png
```

---

##  Referencias

- [Documentación oficial de Docker](https://docs.docker.com/)
- [MySQL Docker Hub](https://hub.docker.com/_/mysql)
- [MariaDB Docker Hub](https://hub.docker.com/_/mariadb)
- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)
- [DBeaver Docs](https://dbeaver.io/docs/)
- [HeidiSQL Docs](https://www.heidisql.com/help.php)
- [Beekeeper Studio Docs](https://docs.beekeeperstudio.io/)
