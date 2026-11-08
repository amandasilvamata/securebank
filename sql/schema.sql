CREATE DATABASE IF NOT EXISTS securebank;

USE securebank;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    receiver_account_id INT,
    type VARCHAR(20) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (receiver_account_id) REFERENCES accounts(id)
);