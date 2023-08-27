-- write a query in SQL to display the first name, last name, department number, and department name for each employee
-- write a query in SQL to display the first and last name, department, city, and state province for each employee
-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
-- write a query in SQL to display all departments including those where does not have any employee
-- write a query in SQL to display the first name of all employees including the first name of their manager
-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
-- write a query in SQL to display the job title and the average salary of employees
-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
-- write a query in SQL to display the department name and the number of employees in each department

SELECT first_name, last_name, employees.department_id, department_name FROM employees
LEFT JOIN department ON employees.department_id = department.department_id;

SELECT first_name, last_name, department_name, city, state_province FROM employees
LEFT JOIN department ON employees.department_id = department.department_id
LEFT JOIN locations ON department.location_id = locations.location_id;

SELECT first_name, last_name, employees.department_id, department_name FROM employees
LEFT JOIN department ON employees.department_id = department.department_id
WHERE employees.department_id = 80 OR 40;

SELECT * FROM departments;

SELECT 
    E.first_name AS employee_first_name, 
    E.employee_id, 
    M.first_name AS manager_first_name, M.manager_id
FROM employees E
JOIN employees M ON E.employee_id = M.manager_id
WHERE E.employee_id = M.manager_id;

SELECT job_title,
       CONCAT(first_name, ' ', last_name) AS full_name,
       (MAX(salary) OVER (PARTITION BY employees.job_id) - salary) AS salary_difference
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id;

SELECT job_title, AVG(salary) AS average_salary
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id
GROUP BY job_title;

SELECT CONCAT(first_name, ' ', last_name) AS full_name, salary
FROM employees
JOIN department ON employees.department_id = department.department_id
JOIN locations ON department.location_id = locations.location_id
WHERE locations.city = 'London';

