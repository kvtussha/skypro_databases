-- SQL-команды для создания таблиц
CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	first_name CHARACTER VARYING(100),
	last_name CHARACTER VARYING(100),
	title CHARACTER VARYING(100),
	birth_date DATE,
	notes TEXT
)

CREATE TABLE customers (
	customer_id CHARACTER VARYING(5) PRIMARY KEY,
	company_name CHARACTER VARYING(100),
	contact_name CHARACTER VARYING(50)
)

CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY,
	customer_id CHARACTER REFERENCES customers(customer_id),
	employee_id INTEGER REFERENCES employees(employee_id),
	order_date DATE,
	ship_city CHARACTER VARYING(100)
)

