-- Insert ServiceProviders
INSERT INTO service_serviceprovider (name, email, phone)
VALUES 
('Provider 1', 'service_provider1@example.com', '123-456-7890'),
('Provider 2', 'service_provider2@example.com', '123-456-7890'),
('Provider 3', 'service_provider3@example.com', '123-456-7890'),
('Provider 4', 'service_provider4@example.com', '123-456-7890');

-- Insert Customers
INSERT INTO service_customer (name, email, phone)
VALUES 
('Customer 1', 'customer1@example.com', '123-456-7890'),
('Customer 2', 'customer2@example.com', '123-456-7891'),
('Customer 3', 'customer3@example.com', '123-456-7892'),
('Customer 4', 'customer4@example.com', '123-456-7893');

-- Insert ServiceCategories
INSERT INTO service_servicecategory (name, description)
VALUES
('Hair Care', 'Services related to hair'),
('Nail Care', 'Services related to nails'),
('Body Care', 'Services related to full body care');

-- Insert Services
INSERT INTO service_service (service_provider_id, name, description, price)
VALUES
(1, 'Haircut', 'A simple haircut', 20.00),
(1, 'Manicure', 'Nail trimming and polish', 30.00),
(1, 'Massage', 'Full body massage', 100.00),
(2, 'Haircut', 'A simple haircut', 20.00),
(2, 'Manicure', 'Nail trimming and polish', 30.00),
(2, 'Massage', 'Full body massage', 100.00),
(3, 'Haircut', 'A simple haircut', 20.00),
(3, 'Manicure', 'Nail trimming and polish', 30.00),
(3, 'Massage', 'Full body massage', 100.00),
(4, 'Haircut', 'A simple haircut', 20.00),
(4, 'Manicure', 'Nail trimming and polish', 30.00),
(4, 'Massage', 'Full body massage', 100.00);

-- Insert Many-to-Many Relations between Services and Categories
INSERT INTO service_servicecategory_services (service_id, servicecategory_id)
VALUES
(1, 1), 
(1, 3),
(2, 2),
(3, 3),
(4, 1),
(5, 2),
(6, 3),
(7, 1),
(8, 2),
(9, 3),
(10, 1),
(11, 2),
(12, 3);

-- Insert Appointments
INSERT INTO service_appointment (customer_id, service_id, appointment_date, appointment_time, created_at)
VALUES
(1, 1, '2024-08-04', '10:00:00', '2024-08-02 00:00:00'),
(2, 2, '2024-08-05', '11:30:00', '2024-08-04 00:00:00'),
(3, 3, '2024-08-07', '14:00:00', '2024-08-05 00:00:00'),
(4, 4, '2024-08-08', '09:00:00', '2024-08-03 00:00:00'),
(1, 5, '2024-08-10', '13:00:00', '2024-08-01 00:00:00'),
(2, 6, '2024-08-11', '15:30:00', '2024-08-03 00:00:00'),
(3, 5, '2024-08-12', '12:00:00', '2024-08-10 00:00:00'),
(4, 8, '2024-08-14', '10:00:00', '2024-08-03 00:00:00'),
(1, 9, '2024-08-15', '11:30:00', '2024-08-11 00:00:00'),
(2, 10, '2024-08-17', '14:00:00', '2024-08-03 00:00:00'),
(1, 2, '2024-08-05', '10:00:00', '2024-08-03 00:00:00'),
(2, 2, '2024-08-08', '11:30:00', '2024-08-01 00:00:00'),
(3, 3, '2024-08-05', '14:00:00', '2024-08-02 00:00:00'),
(4, 3, '2024-08-12', '09:00:00', '2024-08-10 00:00:00'),
(1, 5, '2024-08-10', '13:00:00', '2024-08-03 00:00:00');