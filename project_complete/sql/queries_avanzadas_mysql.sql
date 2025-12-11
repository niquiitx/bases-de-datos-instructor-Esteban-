-- queries_avanzadas_mysql.sql
USE appdb;

-- 1) INNER JOIN
SELECT a.appointment_id, u.email, CONCAT(u.first_name,' ',u.last_name) AS user_name, s.name AS service_name, a.scheduled_at
FROM appointments a
INNER JOIN users u ON a.user_id = u.user_id
INNER JOIN services s ON a.service_id = s.service_id;

-- 2) LEFT JOIN (last appointment per user)
SELECT u.user_id, u.email, a.appointment_id, a.scheduled_at
FROM users u
LEFT JOIN appointments a ON a.user_id = u.user_id
  AND a.scheduled_at = (
    SELECT MAX(scheduled_at) FROM appointments WHERE user_id = u.user_id
  );

-- 3) RIGHT JOIN (all locations)
SELECT l.name AS location_name, a.appointment_id, a.scheduled_at
FROM appointments a
RIGHT JOIN locations l ON a.location_id = l.location_id;

-- 4) FULL JOIN emulation (appointments vs transactions)
SELECT a.appointment_id, t.transaction_id, a.scheduled_at, t.amount
FROM appointments a
LEFT JOIN transactions t ON a.appointment_id = t.appointment_id
UNION
SELECT a.appointment_id, t.transaction_id, a.scheduled_at, t.amount
FROM appointments a
RIGHT JOIN transactions t ON a.appointment_id = t.appointment_id;

-- 5) GROUP BY + HAVING
SELECT s.name, SUM(t.amount) AS total_facturado
FROM services s
JOIN appointments a ON a.service_id = s.service_id
JOIN transactions t ON t.appointment_id = a.appointment_id
GROUP BY s.name
HAVING SUM(t.amount) > 30;

-- 6) Subquery: users with more than 1 appointment
SELECT * FROM users WHERE user_id IN (
  SELECT user_id FROM appointments GROUP BY user_id HAVING COUNT(*) > 1
);

-- 7) CTE: upcoming appointments count by service
WITH proximas AS (
  SELECT * FROM appointments WHERE scheduled_at > NOW()
)
SELECT s.name, COUNT(*) AS n_citas
FROM proximas p
JOIN services s ON p.service_id = s.service_id
GROUP BY s.name;
