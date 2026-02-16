CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT,
    joining_date DATE
);

INSERT INTO employees (name, department, salary, joining_date) VALUES
('Alice', 'IT', 70000, '2021-06-15'),
('Bob', 'HR', 50000, '2020-03-10'),
('Charlie', 'IT', 80000, '2019-08-20'),
('David', 'Finance', 75000, '2022-01-05');
