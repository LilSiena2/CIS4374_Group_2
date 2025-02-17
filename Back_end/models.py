'''CREATE DATABASE IF NOT EXISTS taylor_ai;
USE taylor_ai;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    service_type VARCHAR(100),
    cost DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); '''
