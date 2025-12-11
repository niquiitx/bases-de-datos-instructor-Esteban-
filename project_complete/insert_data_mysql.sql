-- insert_data_mysql.sql
USE appdb;

INSERT INTO users (email, first_name, last_name) VALUES
('ana@example.com','Ana','Gomez'),
('juan@example.com','Juan','Perez'),
('luis@example.com','Luis','Martinez');

INSERT INTO locations (name, address, city) VALUES
('Sucursal Centro','Calle 1 #2-3','Bogota'),
('Sucursal Norte','Av 10 #20-30','Bogota');

INSERT INTO services (name, description, price) VALUES
('Corte de pelo','Corte profesional',25.00),
('Limpieza facial','Tratamiento express',40.00),
('Asesoria tecnica','Revision de dispositivo',60.00);

INSERT INTO appointments (user_id, service_id, location_id, scheduled_at, status) VALUES
(1,1,1,'2025-12-15 10:00:00','scheduled'),
(2,2,2,'2025-12-16 14:30:00','scheduled'),
(1,3,NULL,'2025-12-20 09:00:00','cancelled');

INSERT INTO transactions (appointment_id, amount, currency, status) VALUES
(1,25.00,'USD','paid'),
(2,40.00,'USD','pending');

INSERT INTO payments (transaction_id, method, paid_at, reference) VALUES
(1,'card','2025-12-01 11:00:00','REF12345');
