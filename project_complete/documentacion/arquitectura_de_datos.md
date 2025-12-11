# Arquitectura de datos - Justificación

- MySQL: manejo de datos transaccionales (users, appointments, transactions, payments) con integridad referencial y ACID.
- MongoDB: perfiles extendidos, historiales y documentos que requieren esquema flexible.
- Redis: sesiones, contadores, colas y estructuras en memoria para baja latencia.

Se usa user_id / appointment_id como llaves lógicas entre sistemas. Redis guarda punteros (e.g., appointment:5) y estados, evitando duplicar datos pesados.
