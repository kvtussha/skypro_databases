-- SQL-команды для создания таблиц
CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	first_name CHARACTER VARYING(100),
	last_name CHARACTER VARYING(100),
	title CHARACTER VARYING(100),
	birth_date DATE,
	notes TEXT
);

CREATE TABLE customers (
	customer_id CHARACTER VARYING(100) PRIMARY KEY,
	company_name CHARACTER VARYING(100),
	contact_name CHARACTER VARYING(100)
);

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id CHARACTER VARYING(100),
	employee_id INTEGER,
	order_date DATE,
	ship_city TEXT,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);


