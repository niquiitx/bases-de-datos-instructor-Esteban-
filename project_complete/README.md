# Proyecto Final - Sistema híbrido MySQL + MongoDB + Redis

## Resumen
Proyecto de ejemplo listo para ejecutar con Docker Compose. Contiene:
- MySQL (appdb) con tablas normalizadas.
- MongoDB con colecciones para perfiles, logs y documentos.
- Redis para colas, contadores y sesiones.
- Worker de ejemplo en Python y script de seed para MongoDB.

## Requisitos
- Docker & Docker Compose
- Opcional: Python 3.8+, pip para ejecutar worker/seed

## Pasos rápidos (con Docker)
1. Coloca este repo en una carpeta local.
2. Ejecuta: `docker-compose up -d`
3. Espera a que MySQL inicialice (revisar logs).
4. Si usas Docker, los scripts SQL en /sql se ejecutarán al inicializar MySQL.
5. Importa Mongo data:
   - `docker cp mongodb_inserts.json proj_mongo:/tmp/mongodb_inserts.json`
   - `docker exec -it proj_mongo bash`
   - `mongoimport --db appdb --collection user_profiles --file /tmp/mongodb_inserts.json --jsonArray` (o usar seed_mongo.py)
6. Conecta Redis: `redis-cli ping`

## Ejecutar worker (local o en container)
Instala dependencias:
`pip install redis pymysql pymongo`

Configura variables si es necesario y ejecuta:
`python worker_example.py`

## Archivos importantes
- /sql/create_tables_mysql.sql
- /sql/insert_data_mysql.sql
- /sql/queries_avanzadas_mysql.sql
- /mongodb/mongodb_inserts.json
- /redis/redis_comandos_basicos.txt
- docker-compose.yml
