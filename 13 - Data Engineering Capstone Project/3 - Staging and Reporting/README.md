## Description
This section contains two main parts:
- Staging area:
    - The staging area is built in PostgreSQL to hold the periodical extracted data from the web server data (transactional data - MySQL Server and catalog data - MongoDB)
    - This database is used as an intermediate load for the production database built in IBM Db2
    - The database schema is built below:

![alt text](https://github.com/DE-romane/IBM-Data-Engineering-Professional-Certificate-notes/blob/main/13%20-%20Data%20Engineering%20Capstone%20Project/3%20-%20Staging%20and%20Reporting/softcartRelationships.jpg)

- Production data warehouse:
    - The production dataware house is built in cloud using IBM Db2
    - Simply the same schema as the staging dataware house in PostgreSQL
    - Perform the Roll-up, Cube, Grouping Sets and Materialized Query Table (MQT). More info of the [code](https://github.com/DE-romane/IBM-Data-Engineering-Professional-Certificate-notes/blob/main/13%20-%20Data%20Engineering%20Capstone%20Project/3%20-%20Staging%20and%20Reporting/codes.sql)
    
