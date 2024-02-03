## W1 ❉ Getting Started with SQL
📓**Basic SQL**
➡ **Introduction to Databases**

**SQL (Structured Query Language)**
- SQL is a language used to query or retrieve data from relational databases.
- It's an acronym for Structured Query Language and is essential for interacting with databases.

**Data**
- Data refers to factual information, including words, numbers, or images, and is a crucial asset for businesses.
- Examples of data include personal information stored by banks, credit card companies, and online platforms like PayPal.

**Databases**
- A database is a repository or program that stores data and provides functions for adding, modifying, and querying data.
- Data can be stored in different forms, including tabular form, where it's organized in tables resembling spreadsheets with columns and rows.

**Relational Databases**
- Relational databases organize data in tables, where columns represent properties (e.g., LastName, FirstName) and rows contain related items.
- Relationships between tables can be established in a relational database.

**Database Management Systems (DBMS)**
- A DBMS is a set of software tools that manages databases, controlling access, organization, and storage of data.
- RDBMS (Relational Database Management System) is a type of DBMS that specifically manages relational databases.
- Examples of RDBMS include MySQL, Oracle database, DB2 warehouse, and DB2 on Cloud.

**Basic SQL Commands**
- Five fundamental SQL commands are mentioned:
  - Create a table
  - Insert data into the table
  - Select data from the table
  - Update data in the table
  - Delete data from the table

➡ **SELECT statement**
SELECT queries to retrieve data from the database

```sql
SELECT COLUMN1, COLUMN2, ... FROM TABLE_1 ;

SELECT * FROM TABLE_1 ; --> retrieve the entire table

--> WHERE clause to filter the required data based on a predicate.
SELECT <COLUMNS> FROM TABLE_1 WHERE <predicate> ;

--> ex:
SELECT * FROM COUNTRY WHERE ID <= 5;

```


➡ **COUNT, DISTINCT, LIMIT**
```sql
--> COUNT is a SQL function used to count the number of rows that match a specific condition within a table.
COUNT(*) -->counts all rows in a table.

SELECT COUNT(column_name) AS count_alias
FROM table_name
WHERE condition;


SELECT COUNT(*) AS active_users
FROM users
WHERE is_active = 1;

---------------------
DISTINCT --> is used to retrieve unique values from a specific column or set of columns in a table.

SELECT DISTINCT column_name1, column_name2, ...
FROM table_name
WHERE condition;


--> fetch unique department names from the employees table
SELECT DISTINCT department
FROM employees;

---------------------
--> LIMIT is used to restrict the number of rows returned by a query.

SELECT column1, column2, ...
FROM table_name
LIMIT number_of_rows;

SELECT *
FROM products
LIMIT 10;

-------------------
--> This will skip the first 20 rows and fetch the subsequent 10 rows from the orders table, useful for implementing pagination.
SELECT *
FROM orders
LIMIT 10 OFFSET 20;

```

➡ **INSERT, UPDATE, and DELETE**

```sql
--> INSERT statement
INSERT INTO table_name (column1, column2, ... )
VALUES (value1, value2, ... );

--> UPDATE statement
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition ;

--> DELETE statement
DELETE FROM table_name
WHERE condition ;
```

## W2 ❉ Introduction to Relational Databases and Tables
📓**Introduction to Relational Databases and Tables**
➡ **Relational Database Concepts**

**1. Relational Model and Data Independence**
- The relational model is widely used in databases due to its allowance for data independence.
- Tables offer logical, physical, and storage independence for stored data.

**2. Entity Relationship Model (ER Model)**
- The ER model is an alternative to the relational model and is used as a tool to design relational databases.
- It presents entities as objects existing independently within the database and helps to represent relationships between entities via an ERD.

**3. Entities, Attributes, and Mapping**
- Entities are represented as objects (persons, places, things) and are depicted as rectangles in an ER diagram.
- Attributes, characteristics that describe entities, are shown as ovals in an ER diagram and provide more information about the entity.
- Attributes of an entity become columns in a table when mapping to a relational database.
- Tables are formed from entities, with attributes becoming columns and rows.

**4. Data Types and Table Structure**
- Attributes of entities have various data types (characters, numbers, dates, etc.) that correspond to column data types in tables.
- Examples of common data types include CHAR, VARCHAR, integers, decimals, timestamps, etc.
- Each table should have a primary key to uniquely identify rows and prevent data duplication.

**5. Relationship between Tables**
- Tables may have foreign keys, which establish relationships by linking to primary keys in other tables.

➡ **Types of SQL statements (DDL vs. DML)**

**1. Purpose of SQL Statements**
- SQL statements are used for interacting with entities (tables), attributes (columns), and their tuples (rows with data values) in relational databases.

**2. Data Definition Language (DDL) Statements**
- DDL statements are used to define, modify, or remove database objects like tables.
- Types of DDL statements:
  - CREATE: Creates tables and defines their columns.
  - ALTER: Modifies tables, including adding/dropping columns or modifying data types.
  - TRUNCATE: Deletes data from a table but not the table itself.
  - DROP: Deletes tables entirely from the database.

**3. Data Manipulation Language (DML) Statements**
- DML statements are used to read from and modify data in tables.
- Often referred to as CRUD operations (Create, Read, Update, Delete) for tables.
- Types of DML statements:
  - INSERT: Inserts one or multiple rows of data into a table.
  - SELECT: Retrieves or reads rows from a table.
  - UPDATE: Modifies existing rows in a table.
  - DELETE: Removes one or multiple rows of data from a table.

**4. Summary of DDL and DML Statements**
- DDL statements are for defining or changing database objects (like tables).
- DML statements are for manipulating or working with data within tables.


➡ **CREATE TABLE Statement**

```sql
CREATE TABLE table_name (
    column1_name datatype constraints,
    column2_name datatype constraints,
    ...
    table_constraints
);

--> Creating a simple table with a few columns:
CREATE TABLE employees (
    employee_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    hire_date DATE
);

--> Adding constraints while creating the table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) DEFAULT 0.00,
    available_date DATE,
    UNIQUE(product_name)
);

```

➡ **ALTER, DROP, and Truncate tables**
```sql
ALTER TABLE --> statement is used to modify an existing table's structure by adding, modifying, or dropping columns, constraints, or indexes.

--> Adding a new column to an existing table:
ALTER TABLE table_name
ADD column_name datatype;

--> Modifying an existing column in a table:
ALTER TABLE table_name
ALTER COLUMN column_name new_datatype;

--> Dropping a column from a table:
ALTER TABLE table_name
DROP COLUMN column_name;

DROP TABLE --> statement is used to remove an entire table and all its data permanently from the database.

DROP TABLE table_name;

TRUNCATE TABLE --> statement is used to delete all rows from a table, but the table structure, columns, constraints, and indexes remain intact.

TRUNCATE TABLE table_name;


```

## W3 ❉ Intermediate SQL
📓**Refining your Results**
➡ **Using String Patterns and Ranges**

**Using String Patterns**
```sql
LIKE --> operator is used to match patterns in string values
% --> is a wildcard representing zero or more characters.

-- Selecting all employees whose name starts with 'J'
SELECT * FROM employees
WHERE employee_name LIKE 'J%';

```

**Using Ranges:**
```sql
BETWEEN --> operator selects values within a specified range.

-- Selecting orders placed between specific dates
SELECT * FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

--> Ranges can also be specified using comparison operators like <, >, <=, >=.
-- Selecting products with prices between $10 and $50
SELECT * FROM products
WHERE price >= 10 AND price <= 50;

```

**Using Sets of Values:**
```sql
IN --> operator is used to specify multiple values in a WHERE clause.
-- Selecting orders from specific customers
SELECT * FROM orders
WHERE customer_id IN (101, 103, 105);

NOT IN Operator:
-- Selecting products not in a certain category
SELECT * FROM products
WHERE category_id NOT IN (4, 7);

```

➡ **Sorting Result Sets**
```sql
ORDER BY --> clause allows you to arrange the retrieved data in a specified order based on one or more columns.

SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;

--> Sorting by Single Column:

-- Sorting employees by their names in ascending order (alphabetically)
SELECT employee_id, employee_name, salary
FROM employees
ORDER BY employee_name ASC;

--> Sorting by Multiple Columns:

-- Sorting orders by date (ascending) and total amount (descending)
SELECT order_id, order_date, total_amount
FROM orders
ORDER BY order_date ASC, total_amount DESC;

--> Orders the result set first by order_date in ascending order.
--> For orders with the same order_date, it sorts those with higher total_amount first in descending order.

--> Sorting with Expression:

-- Sorting products by discount price (original price - discount)
SELECT product_id, product_name, price, discount,
       (price - discount) AS discounted_price
FROM products
ORDER BY discounted_price DESC;

--> Sorting with NULL Values:
-- Sorting employees by their department and handling NULL values
SELECT employee_id, employee_name, department
FROM employees
ORDER BY department DESC NULLS LAST;

NULLS LAST --> places the rows with NULL values in the department column at the end of the sorted result set.
```

➡ **Grouping Result Sets**
```sql
GROUP BY --> clause, allowing aggregation of data based on specific columns and then applying aggregate functions to those grouped data. 

--> aggregate_function(): Functions like COUNT, SUM, AVG, MIN, MAX, etc., applied to grouped data.

SELECT column1, column2, ..., aggregate_function(column)
FROM table_name
GROUP BY column1, column2, ...;

--> Grouping with Aggregate Functions:
|order_id|customer_id|
|--------|-----------|
|1       |        101|
|2       |        102|
|3       |        101|
|4       |        103|

--> Counting Number of Orders per Customer
SELECT customer_id, COUNT(order_id) AS order_count
FROM orders
GROUP BY customer_id;

|customer_id|order_count|
|-----------|-----------|
|101        |          2|
|102        |          1|
|103        |          1|

-------------------------------------

--> Using Multiple Columns in GROUP BY:
--> Orders table

|order_id|customer_id|order_date|total_amount|
|--------|-----------|----------|------------|
|1       |101        |2023-01-05|      150.00|
|2       |102        |2023-01-08|      200.00|
|3       |101        |2023-01-15|      180.00|
|4       |103        |2023-01-20|      300.00|
|5       |101        |2023-02-05|      250.00|
|6       |104        |2023-02-10|      190.00|

SELECT YEAR(order_date) AS order_year, MONTH(order_date) AS order_month,
       SUM(total_amount) AS total_sales
FROM orders
GROUP BY order_year, order_month;
--> SUM(total_amount) for each unique combination of year and month in the order_date.
-->output
|order_year|order_month|total_sales|
|----------|-----------|-----------|
|2023      |1          |830.00     |
|2023      |2          |440.00     |

-------------------------------------
--> Grouping with HAVING Clause:
--> in order to filter the data as per the given condition and then group as per identical values of a specified parameter.
SELECT column_name(s) 
FROM table_name 
GROUP BY column_name(s) 
HAVING condition

--> Employees

|employee_id|department|salary|
|-----------|----------|------|
|1          |Sales     |60000 |
|2          |Finance   |65000 |
|3          |Sales     |58000 |
|4          |Marketing |70000 |
|5          |Finance   |62000 |
|6          |Sales     |63000 |

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
-->output
|department|avg_salary|
|----------|----------|
|Finance   |63500.00  |
|Marketing |70000.00  |

```

📓**Functions, Multiple Tables, and Sub-queries**
➡ **Built-in Database Functions**
**COUNT**

```sql
COUNT --> function returns the number of rows that match a specified criterion.
SELECT COUNT(column_name) FROM table_name WHERE condition;

SELECT COUNT(dep_id) FROM employees;
```
**AVG**
```sql
AVG -->function returns the average value of a numeric column.
SELECT AVG(column_name) FROM table_name WHERE condition;

SELECT AVG(salary) FROM employees;
```
**SUM**
```sql
SUM --> function returns the total sum of a numeric column.
SELECT SUM(column_name) FROM table_name WHERE condition;

SELECT SUM(salary) FROM employees;
```

**MIN**
```sql
MIN --> function returns the smallest value of the SELECTED column.
SELECT MIN(column_name) FROM table_name WHERE condition;

SELECT MIN(salary) FROM employees;
```

**MAX**
```sql
MAX --> function returns the largest value of the SELECTED column.
SELECT MAX(column_name) FROM table_name WHERE condition;

SELECT MAX(salary) FROM employees;
```

**ROUND**
```sql
ROUND --> function rounds a number to a specified number of decimal places.
SELECT ROUND(2number, decimals, operation) AS RoundValue;

SELECT ROUND(salary) FROM employees;
```

**LENGTH**
```sql
LENGTH --> function returns the length of a string (in bytes).
SELECT LENGTH(column_name) FROM table;

SELECT LENGTH(f_name) FROM employees;
```

**UCASE**
```sql
UCASE --> function displays the column name in each table in uppercase.
SELECT UCASE(column_name) FROM table;

SELECT UCASE(f_name) FROM employees;
```

**LCASE**
```sql
LCASE --> function displays the column name in each table in lowercase.
SELECT LCASE(column_name) FROM table;

SELECT LCASE(f_name) FROM employees;
```

**DISTINCT**
```sql
DISTINCT --> function is used to display data without duplicates.
SELECT DISTINCT column_name FROM table;

SELECT DISTINCT UCASE(f_name) FROM employees;
```

➡ **Date and Time Built-in Functions**
```sql
DAY --> function returns the day of the month for a given date.
SELECT DAY(column_name) FROM table 
SELECT DAY(b_date) FROM employees where emp_id = 'E1002';

-------------------------------
CURRENT_DATE	--> is used to display the current date.
SELECT CURRENT_DATE;

-------------------------------
DATEDIFF() --> is used to calculate the difference between two dates or time stamps. The default value generated is the difference in number of days.

SELECT DATEDIFF(date1, date2); 
SELECT DATEDIFF(CURRENT_DATE, date_column) FROM table;
-------------------------------

FROM_DAYS() --> is used to convert a given number of days to YYYY-MM-DD format.
SELECT FROM_DAYS(number_of_days); 	
SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, date_column)) FROM table;

-------------------------------
DATE_ADD() --> is used to calculate the date after lapse of mentioned number of units of date type, i.e. if n=3 and type=DAY, the result is a date 3 days after what is mentioned in date column. The type valiable can also be months or years.

SELECT DATE_ADD(date, INTERVAL n type);
SELECT DATE_ADD(date, INTERVAL 3 DAY);;

-------------------------------
DATE_SUB() --> is used to calculate the date prior to the record date by mentioned number of units of date type, i.e. if n=3 and type=DAY, the result is a date 3 days before what is mentioned in date column. The type valiable can also be months or years

SELECT DATE_SUB(date, INTERVAL n type); 
SELECT DATE_SUB(date, INTERVAL 3 DAY);;
```

➡ **Sub-Queries and Nested Selects**

```sql
--> Subquery is a query within another SQL query and embedded within the WHERE clause.
--> A subquery is used to return data that will be used in the main query as a condition to further restrict the data to be retrieved.

SELECT column_name [, column_name ] FROM table1 [, table2 ] WHERE column_name OPERATOR (SELECT column_name [, column_name ] FROM table1 [, table2 ] [WHERE])


SELECT emp_id, fmame, lname, salary
FROM employees
where salary < (SELECT AVG(salary) FROM employees);


 SELECT * FROM ( SELECT emp_id, f_name, l_name, dep_id FROM employees) AS emp4all;


 SELECT * FROM employees WHERE job_id IN (SELECT job_ident FROM jobs);

```

➡ **Working with Multiple Tables**
```sql
--> Implicit Inner Join combines two or more records but displays only matching values in both tables. Inner join applies only the specified columns.

SELECT column_name(s) FROM table1, table2
WHERE table1.column_name = table2.column_name;

SELECT * FROM employees, jobs where employees.job_id = jobs.job_ident;

-------------------------------
--> Implicit Cross Join is defined as a Cartesian product where the number of rows in the first table is multiplied by the number of rows in the second table.

SELECT column_name(s) FROM table1, table2;
SELECT * FROM employees, jobs;


```














## W4 ❉ Accessing databases Using python
📓**Accessing databases using Python**
➡ **How to Access Databases Using Python**

**Benefits of Using Python for Database Access:**
- Rich Python ecosystem with tools for data science (NumPy, Pandas, matplotlib, SciPy)
- Easy to learn with a simple syntax
- Portability across platforms due to open-source nature
- Support for relational database systems
- Presence of Python Database API (DB API) for easier database access
- Notebooks as popular tools for data science, particularly Jupyter notebooks
- Support for over 40 programming languages in Jupyter notebooks
- Sharing and collaboration options through email, Dropbox, GitHub, and Jupyter notebook viewer
- Rich interactive output, including HTML, images, videos, LaTeX, and custom types
- Integration with big data tools such as Apache Spark from Python, R, and Scala

**Accessing Databases Using Python in Jupyter Notebooks:**
- Mechanism of Python program communication with DBMS
- Connection to the database using API calls
- Explanation of SQL APIs and Python DB APIs
- API as a set of functions for accessing a service
- SQL API illustration with library function calls
- Buffer creation and API calls to send SQL statements to DBMS
- API calls for checking status and handling errors
- API call to disconnect from the database

**Proprietary APIs for Popular SQL-Based DBMS Systems:**
- MySQL C API for MySQL databases
- psycopg2 API for connecting Python applications to PostgreSQL databases
- IBM_DB API for connecting Python applications to IBM DB2 databases
- dblib API for connecting to SQL Server databases
- ODBC for database access on Microsoft Windows OS
- OCI for Oracle databases
- JDBC for Java applications


➡ **Create & Access SQLite database using Python**
SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.

```python
#### Create database using SQLite
import sqlite3

# Create a new database and open a database connection to allow sqlite3 to work with it.
# to create a connection to the database INSTRUCTOR.db in the current working directory, implicitly creating it if it does not exist.
 sqlite3.connect()


import sqlite3
con = sqlite3.connect("INSTRUCTOR.db")

_________________
# To execute SQL statements and fetch results from SQL queries, use a database cursor. 
# to create the Cursor.

cursor_obj = con.cursor()
_________________

# execute  method in Python's SQLite library allows to perform SQL commands, including retrieving data from a table using a query like "Select * from table_name." When you execute this command, the result is obtained as a collection of table data stored in an object, typically in the form of a list of lists.

cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')

_________________
# fetchall()  method in Python retrieves all the rows from the result set of a query and presents them as a list of tuples.

cursor_obj.fetchall() 

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)

_________________
# fetchmany()  method retrieves the subsequent group of rows from the result set of a query rather than just a single row.
# To fetch a few rows from the table, use fetchmany() and mention how many rows you want to fetch.

 cursor_obj.fetchmany(numberofrows)

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
output_many = cursor_obj.fetchmany(2)
for row_many in output_many:
    print(row_many)

_________________
# read_sql_query()  is a function provided by the Pandas library in Python, and it is not specific to MySQL.
# It is a generic function used for executing SQL queries on various database systems, including MySQL, and retrieving the results as a Pandas DataFrame.

 read_sql_query() 
df = pd.read_sql_query("select * from instructor;", conn)
_________________

 dataframe.shape 
# It provides a tuple indicating the shape of a DataFrame or Series, represented as (number of rows, number of columns).

df.shape
_________________

 con.close() # is a method used to close the connection to a MySQL database. When called, it terminates the connection, releasing any associated resources and ensuring the connection is no longer active.
# This is important for managing database connections efficiently and preventing resource leaks in your MySQL database interactions.	

con.close()

_________________
 seaborn.barplot(x="x-axis_variable", y="y-axis_variable", data=data) 
# is a function in the Seaborn Python data visualization library used to create a bar plot, also known as a bar chart. It is particularly used to display the relationship between a categorical variable and a numeric variable by showing the average value for each category.

import seaborn
seaborn.barplot(x='Test_Score',y='Frequency', data=dataframe)
_________________

df = pd.read_csv('file_path.csv')
# read_csv()  is a function in Python's Pandas library used for reading data from a Comma-Separated Values (CSV) file and loading it into a Pandas DataFrame. It's a common method for working with tabular data stored in CSV format

import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
_________________

df.to_sql('table_name', index=False) 

df.to_sql() # is a method in Pandas, a Python data manipulation library used to write the contents of a DataFrame to a SQL database. It allows to take data from a DataFrame and store it structurally within a SQL database tabl

import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')

df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")

_________________
df = pd.read_sql(sql_query, conn)

# read_sql()  is a function provided by the Pandas library in Python for executing SQL queries and retrieving the results into a DataFrame from an SQL database. It's a convenient way to integrate SQL database interactions into your data analysis workflows.

selectQuery = "select * from INSTRUCTOR"
df = pandas.read_sql(selectQuery, conn)
```

➡ **Accessing Databases with SQL magic**

To communicate with SQL Databases from within a JupyterLab notebook,
we can use the SQL "magic" provided by the ipython-sql extension.
"Magic" is JupyterLab's term for special commands that start with "%". 

 we'll use the load_ext magic to load the ipython-sql extension.
 
```python
%load_ext sql

# syntax for connecting to magic sql using sqllite is

%sql sqlite://DatabaseName

_________________
import csv, sqlite3

con = sqlite3.connect("SQLiteMagic.db")
cur = con.cursor()

%load_ext sql
%sql sqlite:///SQLiteMagic.db

```

## W6 ❉ Advanced SQL For Data Engineer
📓**Views, Stored Procedures, and Transactions**
➡ **Views**
- **What is a View:**
  - A view is an alternative way of representing data from one or more tables or views.
  - It can include some or all columns from base tables or existing views.
  - Creating a view establishes a named specification for a results table that can be queried like a table.
  - The data the view represents is stored in the base tables, not the view itself.

- **Benefits and Usage of Views:**
  - Show a selection of data for a table, omitting sensitive information.
  - Combine two or more tables meaningfully.
  - Simplify access to data by granting access to a view without exposing underlying tables.
  - Display only relevant data for a specific process.

- **Creating a View:**
 ```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

 --------------
CREATE VIEW high_salary_employees AS
SELECT employee_id, first_name, last_name
FROM employees
WHERE salary > 50000;
----------------------

SELECT * FROM high_salary_employees;

-----------------------------
CREATE OR REPLACE VIEW  --> command updates a view.

CREATE OR REPLACE VIEW view_name AS 
SELECT column1, column2, ... FROM table_name WHERE condition; 

CREATE OR REPLACE VIEW EMPSALARY AS 
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, JOB_TITLE, MIN_SALARY, MAX_SALARY 
FROM EMPLOYEES, JOBS 
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT; 

```

- **Working with Views:**
  - Views are dynamic and consist of data returned from the `SELECT` statement used to create them.
  - When used in other SQL statements, views behave as if a `SELECT` statement were used to retrieve the view's content.
  - Restrictions on using `ORDER BY` and naming host variables with views.

- **Modifying Views:**
  - Views can be modified using `INSERT`, `UPDATE`, and `DELETE` queries against the view.

- **Removing a View:**
  - Use `DROP VIEW` to remove a view completely.


➡ **Stored Procedures**
- **Definition of Stored Procedure:**
  - A stored procedure is a set of SQL statements stored and executed on the database server.
  - Instead of sending multiple SQL statements from the client to the server, they are encapsulated in a stored procedure on the server.

- **Languages for Writing Stored Procedures:**
  - Stored procedures can be written in various languages, such as SQL, PL, PL/SQL, Java, C, or others.
  - They can accept parameters, perform CRUD operations, and return results to the client application.

- **Benefits of Stored Procedures:**
  - Reduction in network traffic as only one call is needed to execute multiple statements.
  - Performance improvement because processing happens on the server, with only the final result sent back to the client.
  - Code reuse as multiple applications can use the same stored procedure.
  - Increased security by not exposing all table and column information to client-side developers.
  - Server-side logic can validate data before accepting it into the system.

- **Considerations for Stored Procedures:**
  - SQL is not a fully fledged programming language; avoid writing all business logic in stored procedures.

- **Creating a Stored Procedure in MySQL using phpMyAdmin:**

```sql
stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

The default terminator for a stored procedure is semicolon (;). To set a different terminator we use DELIMITER clause followed by the terminator such as $$ or //.


DELIMITER //

CREATE PROCEDURE PROCEDURE_NAME

BEGIN

END //

DELIMITER ;

---------------------------
--> Creates a stored procedure named GetEmployeesByDepartment that takes one input parameter (deptName).

DELIMITER //

CREATE PROCEDURE GetEmployeesByDepartment(IN deptName VARCHAR(50))
BEGIN
    SELECT EmployeeID, FirstName, LastName, Department
    FROM Employees
    WHERE Department = deptName;
END //

DELIMITER ;

--------
--> To execute the stored procedure, you can use the CALL statement
CALL GetEmployeesByDepartment('Sales');


```

- **Changing Delimiters for Multi-Statement Procedures:**
  - Change the delimiter before defining a procedure to mark the end of statements.
  - Example: Using a delimiter (`$$`) and resetting it back to a semicolon (`;`) when done.

- **Calling Stored Procedures:**
  - Stored procedures can be called from external applications or dynamic SQL statements.
  - Use the `CALL` statement with the procedure name and pass required parameters.

➡ **ACID Transactions**
- **Definition of Transaction:**
  - A transaction is an indivisible unit of work.
  - It can consist of one or more SQL statements.
  - To be considered successful, all SQL statements must complete successfully or none at all.

- **Example of ACID Transaction:**
  - Illustration using a purchase example:
    - Product added to cart.
    - Payment processed.
    - Account debited, and store's account credited.
    - Inventory reduced.
  - If any of these steps fail, the entire transaction fails to maintain data consistency.

- **ACID Principles:**
  - ACID stands for:
    - Atomic: All changes must be performed successfully or not at all.
    - Consistent: Data must be in a consistent state before and after the transaction.
    - Isolated: No other process can change the data while the transaction is running.
    - Durable: Changes made by the transaction must persist.

- **Managing ACID Transactions:**
  - To start an ACID transaction, use the `BEGIN` command.
  - Commands issued after `BEGIN` are part of the transaction until `COMMIT` or `ROLLBACK` is issued.
  - `COMMIT` is used to save all changes to the database, creating a consistent, stable state.
  - `ROLLBACK` is used to undo all changes if any command in the transaction fails.

- **Calling SQL Commands:**
  - SQL statements can be called from languages like Java, C, R, and Python.
  - Use database-specific access APIs, e.g., JDBC for Java or ibm_db for Python.
  - SQL commands, including `COMMIT` and `ROLLBACK`, can be incorporated into application code.

- **Implicit `BEGIN` Command:**
  - In some databases, like Db2 on Cloud, the `BEGIN` command is implicit; it doesn't need to be explicitly called.

- **Error-Checking in Transactions:**
  - Incorporating SQL commands into application code allows for error-checking routines.
  - These routines control whether the transaction is committed or rolled back based on the success of SQL statements.
```sql

-->  we can use the BEGIN statement:
START TRANSACTION;

-- Deduct money from Account A
UPDATE Accounts
SET Balance = Balance - 100
WHERE AccountID = 123;

-- Add money to Account B
UPDATE Accounts
SET Balance = Balance + 100
WHERE AccountID = 456;

COMMIT;
---------------------
COMMIT --> is used to save all changes to the database, creating a consistent, stable state.

ROLLBACK --> is used to undo all changes if any command in the transaction fails.

-------------------
```

example
 Rose is buying a pair of boots from ShoeShop. So we have to update Rose's balance as well as the ShoeShop balance in the BankAccounts table. Then we also have to update Boots stock in the ShoeShop table. After Boots, let's also attempt to buy Rose a pair of Trainers.
```sql
--> create a stored procedure routine named TRANSACTION_ROSE that includes TCL commands like COMMIT and ROLLBACK.

DELIMITER //

CREATE PROCEDURE TRANSACTION_ROSE()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    START TRANSACTION;
    UPDATE BankAccounts
    SET Balance = Balance-200
    WHERE AccountName = 'Rose';

    UPDATE BankAccounts
    SET Balance = Balance+200
    WHERE AccountName = 'Shoe Shop';

    UPDATE ShoeShop
    SET Stock = Stock-1
    WHERE Product = 'Boots';

    UPDATE BankAccounts
    SET Balance = Balance-300
    WHERE AccountName = 'Rose';

    COMMIT;
END //

DELIMITER ;
```

📓**JOIN Statements**

**➡ Join Overview**
- **Primary and Foreign Keys:**
  - Primary key (PK) uniquely identifies each row in a table .
  - Foreign key (FK) refers to the primary key of another entity.
  
- **Types of Joins in SQL:**
  - SQL offers different types of JOINs.
  - Inner Join: Displays only rows with matching values in a common column (usually a primary key in one table and a foreign key in the other).
  - Outer Joins: Return matching rows and even non-matching rows from one or the other table.
  - Many varieties of outer joins can refine the result set.

 **➡ Inner Join**
INNER JOIN is a type of join operation in relational databases that retrieves rows from two or more tables based on a related column between them. The INNER JOIN keyword selects records that have matching values in both tables.

```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name;
-->  the condition for the join.

------------
SELECT e.employee_id, e.first_name, e.last_name, d.department_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.department_id;

 --> rows will be selected where the department_id values match in both tables.

-------------------
--> Multiple Joins: You can perform INNER JOINs on more than two tables by extending the syntax:

SELECT columns
FROM table1
INNER JOIN table2 ON table1.column_name = table2.column_name
INNER JOIN table3 ON table2.column_name = table3.column_name;

```

 **➡ Outer Joins**
Outer joins are a type of SQL join that retrieves records from one or more tables even if there is no match between the columns being joined. Unlike inner joins, which only return rows with matching values in both tables, outer joins include unmatched rows from one or both tables.

There are three types of outer joins:

**1-LEFT OUTER JOIN (or LEFT JOIN):**

Returns all rows from the left table and the matched rows from the right table. If there is no match, NULL values are returned for columns from the right table.

```sql
SELECT *
FROM table1 LEFT JOIN table2 
ON table1.column = table2.column;

```

**2- RIGHT OUTER JOIN (or RIGHT JOIN):**

Returns all rows from the right table and the matched rows from the left table. If there is no match, NULL values are returned for columns from the left table.
```sql
SELECT *
FROM table1 RIGHT JOIN table2 
ON table1.column = table2.column;

```

**3-FULL OUTER JOIN (or FULL JOIN):**
Returns all rows when there is a match in either the left or right table. If there is no match, NULL values are returned for columns from the table without a match.
```sql
SELECT *
FROM table1 FULL JOIN table2 
ON table1.column = table2.column;
```

```sql
employees:
+-------------+---------+---------------+
| employee_id |  name   | department_id |
+-------------+---------+---------------+
| 1           | John    | 101           |
| 2           | Jane    | 102           |
| 3           | Bob     | NULL          |
+-------------+---------+---------------+

departments:
+----------------+-----------------+
| department_id  | department_name |
+----------------+-----------------+
| 101            | HR              |
| 102            | IT              |
| 103            | Marketing       |
+----------------+-----------------+

_________________
--> LEFT OUTER JOIN (or LEFT JOIN):
--> Returns all rows from the left table (employees) and the matching rows from the right table (departments). If there is no match, NULL values are returned for columns from the right table.


SELECT *
FROM employees LEFT JOIN departments 
ON employees.department_id = departments.department_id;

--> output
+-------------+--------+---------------+-----------------+------------------+
| employee_id |  name  | department_id | department_id | department_name |
+-------------+--------+---------------+-----------------+------------------+
| 1           | John   | 101            | 101            | HR               |
| 2           | Jane   | 102            | 102            | IT               |
| 3           | Bob    | NULL           | NULL           | NULL             |
+-------------+--------+----------------+----------------+------------------+

_________________
--> RIGHT OUTER JOIN (or RIGHT JOIN):
--> Returns all rows from the right table (departments) and the matching rows from the left table (employees). If there is no match, NULL values are returned for columns from the left table.

SELECT *
FROM employees RIGHT JOIN departments 
ON employees.department_id = departments.department_id;

Result:
+-------------+----------+-----------------+-----------------+------------------+
| employee_id |  name    | department_id   | department_id | department_name |
+-------------+----------+-----------------+-----------------+------------------+
| 1           | John     | 101             | 101            | HR               |
| 2           | Jane     | 102             | 102            | IT               |
| NULL        | NULL     | NULL            | 103            | Marketing        |
+-------------+----------+-----------------+-----------------+------------------+

_________________
--> FULL OUTER JOIN (or FULL JOIN):
--> Returns all rows when there is a match in either the left or right table. If there is no match, NULL values are returned for columns from the table without a match.

SELECT *
FROM employees FULL JOIN departments 
ON employees.department_id = departments.department_id;

+-------------+----------+-----------------+-----------------+------------------+
| employee_id |  name    | department_id | department_id | department_name |
+-------------+----------+-----------------+-----------------+------------------+
| 1           | John     | 101            | 101            | HR               |
| 2           | Jane     | 102            | 102            | IT               |
| 3           | Bob      | NULL           | NULL           | NULL             |
| NULL        | NULL     | NULL           | 103            | Marketing        |
+-------------+----------+-----------------+-----------------+------------------+
```








































 