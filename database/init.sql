CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    balance NUMERIC(12,2)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(50),
    amount NUMERIC(12,2)
);

INSERT INTO accounts (customer_name, balance)
VALUES 
('Geetanjali Pal', 85000.00),
('Demo Customer', 45000.00);

INSERT INTO transactions (account_id, transaction_type, amount)
VALUES
(1, 'Credit', 25000.00),
(1, 'Debit', 5000.00),
(2, 'Credit', 15000.00);