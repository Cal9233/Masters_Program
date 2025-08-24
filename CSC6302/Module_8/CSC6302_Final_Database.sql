-- Drop and create database
DROP DATABASE IF EXISTS finance_db;
CREATE DATABASE finance_db;
USE finance_db;

-- ==============================
-- Tables
-- ==============================
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category_name VARCHAR(100) NOT NULL,
    category_type ENUM('income', 'expense') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_name VARCHAR(100) NOT NULL,
    account_type ENUM('checking', 'savings', 'credit', 'investment') NOT NULL,
    balance DECIMAL(12,2) DEFAULT 0.00,
    date_opened DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    category_id INT,
    transaction_type ENUM('income', 'expense', 'transfer') NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    transaction_date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Budgets (
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    budget_amount DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (user_id, category_id, start_date, end_date),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Financial_Goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    goal_name VARCHAR(100) NOT NULL,
    target_amount DECIMAL(12,2) NOT NULL,
    current_amount DECIMAL(12,2) DEFAULT 0.00,
    target_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ==============================
-- Sample Data
-- ==============================
INSERT INTO Users (username, email, password_hash) VALUES
('alice', 'alice@email.com', 'hash1'),
('bob', 'bob@email.com', 'hash2'),
('carol', 'carol@email.com', 'hash3');

INSERT INTO Categories (user_id, category_name, category_type) VALUES
(1, 'Salary', 'income'),
(1, 'Groceries', 'expense'),
(1, 'Rent', 'expense'),
(2, 'Freelance', 'income'),
(2, 'Entertainment', 'expense'),
(3, 'Consulting', 'income'),
(3, 'Dining', 'expense');

INSERT INTO Accounts (user_id, account_name, account_type, balance, date_opened) VALUES
(1, 'Checking Account', 'checking', 2500.00, '2020-01-10'),
(1, 'Savings Account', 'savings', 5000.00, '2020-02-01'),
(2, 'Credit Card', 'credit', -350.00, '2021-03-15'),
(3, 'Business Account', 'checking', 1000.00, '2022-01-01');

-- Add 30+ transactions for requirement (fixed category references)
INSERT INTO Transactions (account_id, category_id, transaction_type, amount, transaction_date, description) VALUES
(1, 1, 'income', 3000.00, '2023-01-01', 'Monthly Salary'),
(1, 2, 'expense', -200.00, '2023-01-05', 'Grocery Store'),
(1, 3, 'expense', -1200.00, '2023-01-10', 'Rent Payment'),
(1, 2, 'expense', -150.00, '2023-01-15', 'Supermarket'),
(1, 2, 'expense', -180.00, '2023-01-20', 'Groceries'),
(1, 2, 'expense', -210.00, '2023-01-25', 'Groceries'),
(1, 3, 'expense', -1200.00, '2023-02-10', 'Rent Payment'),
(1, 2, 'expense', -160.00, '2023-02-12', 'Groceries'),
(1, 2, 'expense', -170.00, '2023-02-18', 'Groceries'),
(1, 2, 'expense', -190.00, '2023-02-25', 'Groceries'),
(2, 4, 'income', 1500.00, '2023-03-01', 'Freelance Project'),
(2, 5, 'expense', -80.00, '2023-03-05', 'Entertainment'),
(2, 5, 'expense', -100.00, '2023-03-12', 'Movies'),
(2, 5, 'expense', -120.00, '2023-03-20', 'Concert'),
(2, 5, 'expense', -90.00, '2023-03-25', 'Streaming'),
(4, 6, 'income', 2000.00, '2023-04-01', 'Consulting Project'),
(4, 7, 'expense', -150.00, '2023-04-05', 'Business Dinner'),
(4, 7, 'expense', -200.00, '2023-04-10', 'Client Dinner'),
(4, 7, 'expense', -180.00, '2023-04-15', 'Lunch Meeting'),
(4, 7, 'expense', -220.00, '2023-04-20', 'Conference Dinner'),
(1, 2, 'expense', -250.00, '2023-04-25', 'Groceries'),
(1, 2, 'expense', -260.00, '2023-05-05', 'Groceries'),
(1, 2, 'expense', -270.00, '2023-05-12', 'Groceries'),
(1, 2, 'expense', -280.00, '2023-05-18', 'Groceries'),
(1, 2, 'expense', -290.00, '2023-05-25', 'Groceries'),
(1, 2, 'expense', -300.00, '2023-06-01', 'Groceries'),
(1, 2, 'expense', -310.00, '2023-06-08', 'Groceries'),
(1, 2, 'expense', -320.00, '2023-06-15', 'Groceries'),
(1, 2, 'expense', -330.00, '2023-06-22', 'Groceries'),
(1, 2, 'expense', -340.00, '2023-06-29', 'Groceries'),
(2, 5, 'expense', -75.00, '2023-07-01', 'Movie Night'),
(2, 5, 'expense', -125.00, '2023-07-15', 'Concert Tickets');

INSERT INTO Budgets (user_id, category_id, start_date, end_date, budget_amount) VALUES
(1, 2, '2023-01-01', '2023-01-31', 600.00),
(1, 3, '2023-01-01', '2023-01-31', 1200.00),
(2, 5, '2023-01-01', '2023-01-31', 300.00);

INSERT INTO Financial_Goals (user_id, goal_name, target_amount, current_amount, target_date) VALUES
(1, 'Vacation', 2000.00, 500.00, '2024-06-01'),
(2, 'Buy New Laptop', 1500.00, 200.00, '2023-12-01');

-- ==============================
-- Views
-- ==============================
DROP VIEW IF EXISTS user_expense_summary;
CREATE VIEW user_expense_summary AS
SELECT 
    u.user_id,
    u.username,
    c.category_name,
    SUM(CASE WHEN t.transaction_type = 'expense' THEN ABS(t.amount) ELSE 0 END) AS total_spent,
    SUM(CASE WHEN t.transaction_type = 'expense' THEN 1 ELSE 0 END) AS expense_count
FROM Users u
JOIN Categories c ON c.user_id = u.user_id
LEFT JOIN Transactions t ON t.category_id = c.category_id
GROUP BY u.user_id, u.username, c.category_name
ORDER BY u.username, c.category_name;

DROP VIEW IF EXISTS budget_vs_spend_monthly;
CREATE VIEW budget_vs_spend_monthly AS
SELECT
    u.user_id,
    u.username,
    c.category_name,
    b.start_date,
    b.end_date,
    b.budget_amount,
    COALESCE((
        SELECT SUM(ABS(t.amount))
        FROM Transactions t
        WHERE t.category_id = b.category_id
          AND t.transaction_type = 'expense'
          AND t.transaction_date BETWEEN b.start_date AND b.end_date
    ), 0) AS actual_spent,
    (b.budget_amount - COALESCE((
        SELECT SUM(ABS(t.amount))
        FROM Transactions t
        WHERE t.category_id = b.category_id
          AND t.transaction_type = 'expense'
          AND t.transaction_date BETWEEN b.start_date AND b.end_date
    ), 0)) AS remaining_amount
FROM Budgets b
JOIN Categories c ON c.category_id = b.category_id
JOIN Users u ON u.user_id = b.user_id
ORDER BY u.username, b.start_date, c.category_name;

-- ==============================
-- Stored Procedures
-- ==============================
DELIMITER $$

CREATE PROCEDURE GetUserTransactions (IN p_user_id INT)
BEGIN
    SELECT t.transaction_id, t.transaction_type, t.amount, t.transaction_date, t.description
    FROM Transactions t
    JOIN Accounts a ON t.account_id = a.account_id
    WHERE a.user_id = p_user_id
    ORDER BY t.transaction_date DESC;
END $$

CREATE PROCEDURE InsertTransaction (
    IN p_account_id INT,
    IN p_category_id INT,
    IN p_type ENUM('income','expense','transfer'),
    IN p_amount DECIMAL(12,2),
    IN p_date DATE,
    IN p_desc VARCHAR(255)
)
BEGIN
    INSERT INTO Transactions (account_id, category_id, transaction_type, amount, transaction_date, description)
    VALUES (p_account_id, p_category_id, p_type, p_amount, p_date, p_desc);
END $$

CREATE PROCEDURE UpdateAccountBalance (
    IN p_account_id INT, 
    IN p_new_balance DECIMAL(12,2)
)
BEGIN
    UPDATE Accounts SET balance = p_new_balance WHERE account_id = p_account_id;
    -- Cascading effect: Update related transaction amounts proportionally (demonstration)
    UPDATE Transactions 
    SET amount = amount * 1.01 
    WHERE account_id = p_account_id AND transaction_type = 'income';
END $$

CREATE PROCEDURE DeleteUserCascade (IN p_user_id INT)
BEGIN
    -- This will cascade delete due to foreign key constraints
    DELETE FROM Users WHERE user_id = p_user_id;
END $$

DELIMITER ;

-- ==============================
-- Demo Sequence (Required Format)
-- ==============================

-- Step 1: Call both views initially
SELECT '=== INITIAL VIEW: User Expense Summary ===' AS summary_example;
SELECT * FROM user_expense_summary;

SELECT '=== INITIAL VIEW: Budget vs Spend Monthly ===' AS summary_example;
SELECT * FROM budget_vs_spend_monthly;

-- Step 2: Execute each stored procedure once
SELECT '=== PROCEDURE 1: Get User 1 Transactions ===' AS summary_example;
CALL GetUserTransactions(1);

SELECT '=== PROCEDURE 2: Insert New Transaction ===' AS summary_example;
CALL InsertTransaction(1, 2, 'expense', -99.99, '2023-07-01', 'Extra groceries');

SELECT '=== PROCEDURE 3: Update Account Balance (with cascade effect) ===' AS summary_example;
CALL UpdateAccountBalance(1, 3000.00);

SELECT '=== PROCEDURE 4: Delete User (cascade delete) ===' AS summary_example;
CALL DeleteUserCascade(3);

-- Step 3: Call both views again to show changes
SELECT '=== FINAL VIEW: User Expense Summary (After Changes) ===' AS summary_example;
SELECT * FROM user_expense_summary;

SELECT '=== FINAL VIEW: Budget vs Spend Monthly (After Changes) ===' AS summary_example;
SELECT * FROM budget_vs_spend_monthly;