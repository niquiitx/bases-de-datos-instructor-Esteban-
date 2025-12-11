# Conexion entre MySQL, MongoDB y Redis - Caso de uso integrado

Flujo:
1. Usuario crea cuenta -> MySQL (users) y MongoDB (user_profiles).
2. Usuario crea appointment -> MySQL (appointments).
3. Backend LPUSH queue:appointments "appointment:{id}" in Redis.
4. Worker RPOP queue:appointments, consulta MySQL y escribe log en MongoDB.
5. Worker incrementa counters en Redis e, si aplica, guarda documentos en MongoDB.

Llaves: user_id y appointment_id son usadas como referencia entre los sistemas. No se recomienda replicar objetos completos en Redis; usar punteros y datos mínimos.
