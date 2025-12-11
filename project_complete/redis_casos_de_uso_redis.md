# Casos de uso Redis - Documentación

1) Cola de atención (LIST)
- Producer: al crear appointment en MySQL, backend hace LPUSH queue:appointments "appointment:{id}".
- Worker: hace RPOP queue:appointments, obtiene id, consulta MySQL para datos, envía notificación y guarda log en MongoDB.

2) Contador de visitas (STRING)
- Incremento en cada view: INCR service:{id}:visits
- Persistencia periódica: worker que lee y persiste en MySQL para reporting

3) Sesiones (HASH + TTL)
- Al login: HSET session:{token} user_id {id} ...; EXPIRE session:{token} 3600

4) Configuración por servicio (HASH)
- service:config:{id} HSET currency USD price_override 0.0
