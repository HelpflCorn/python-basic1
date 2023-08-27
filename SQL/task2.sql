SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees;
SELECT DISTINCT department_id FROM employees;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary*0.12 AS "PF" FROM employees;
SELECT MAX(salary), MIN(salary) FROM employees;
SELECT first_name, last_name, employee_id, ROUND(salary/12, 2) AS "Monthly Decimal SALARY" FROM employees