## W1 ❉ Relational Databases Concepts
📓**Fundamental Relational Database Concepts**
➡️ **Review of Data Fundamentals**
overview of data types, storage solutions, file formats, and systems used to manage and analyze data in modern businesses.

**Definition and Types of Data:**
- Data is unorganized information that is processed to make it meaningful.
- It can encompass facts, observations, perceptions, numbers, characters, symbols, images, or a combination of these elements.
- Data can be categorized into structured, semi-structured, or unstructured types based on the level and rigidity of its organization.

**Structured Data:**
- Represented in rows and columns like a table with a well-defined schema and rigid structure.
- Ideal for relational databases that store data in tables due to their structured nature.

**Semi-Structured Data:**
- Has some organizational properties but not enough to fit into a rigid, tabular schema.
- Organized into a hierarchy using tags and metadata, making it challenging to store in traditional rows and columns.

**Unstructured Data:**
- Lacks identifiable structure, format, sequence, semantics, or rules.
- Cannot be organized into a tabular format for storage in relational databases; often stored in NoSQL databases.

**Data Sources and Collection:**
- Various sources like existing databases, flat files, XML datasets, web scraping, data streams, social platforms, and IoT devices.
- Data can be stored, processed, and analyzed to provide valuable business insights into performance.

**Data File Formats:**
- Common formats include delimited text files (CSV, TSV), spreadsheets, XML, and JSON.
- Each format has specific characteristics and uses.

**Data Storage Solutions:**
- Structured and semi-structured data are often stored in databases, either relational (e.g., DB2) or non-relational (e.g., MongoDB).
- Choice of storage depends on the type of data and required operations.

**OLTP and OLAP Systems:**
- Online Transaction Processing (OLTP) systems: optimized for day-to-day operational data storage, typically in relational databases.
- Online Analytical Processing (OLAP) systems: optimized for complex data analytics, including relational and non-relational databases, data warehouses, and data lakes.

**Relational Databases:**
- Consist of structured data stored in related tables with minimized data duplication.
- Managed by Relational Database Management Systems (RDBMS) like IBM DB2, Microsoft SQL Server, Oracle, MySQL.
- Used for day-to-day business activities and data analysis purposes.

**Data Transfer and Conclusion:**
- Data can be transferred in various file formats like CSV, XML, and JSON.
- Recap: Data includes various information types, can be structured or unstructured, stored in diverse repositories, and transferred using different file formats.

➡️ **Information and Data Models**

- Understand the distinction between an information model and a data model.
- Recognize the advantages of the relational model.
- Differentiate between entities and attributes.

**Information Model vs. Data Model:**
- Information Model: Abstract, formal representation of entities, encompassing their properties, relationships, and operations.
- Data Model: More concrete, specific, and detailed representation compared to the information model. Serves as the blueprint for a database system.

**Types of Information Models:**
- Hierarchical Model: Represents data using a tree structure with parent and child nodes. IBM's Information Management System was an early example.
- Relational Model: Utilizes tables for storing data, providing data independence in logical, physical, and storage aspects.

**Entity-Relationship Data Model (ERD):**
- Describes entities (tables) and their relationships, illustrated through an Entity-Relationship Diagram (ERD).
- Entities exist independently and are represented as objects (nouns - persons, places, things).
- Attributes define the characteristics of an entity and provide detailed information about it.

**Conversion of ER Diagram to Database Tables:**
- Entities and their attributes are depicted in an ER Diagram (entities as rectangles, attributes as ovals).
- Attributes are specific data elements characterizing an entity (e.g., book title, author, publication year).

**Entity-to-Table Mapping:**
- Entities (e.g., Book, Author) in an ERD become tables in the database.
- Attributes of entities become columns in respective tables.
- Example: Book entity in an ERD becomes a table with columns like book title, edition, year written, etc.
- Example: Author entity becomes a table with columns such as last name, first name, email, city, country, and an author ID.

**Database Design Process:**
- Identification of various entities (e.g., borrowers, book copies, authors) in the database, leading to the final ER Diagram.
- Each identified entity translates into a table in the database design.

➡️ **ERDs & Types of Relationship**

![[Screenshot_2 1.jpg]]


**Building Blocks of a Relationship:**
- Entities, relationship sets, and crows foot notations are the fundamental components.
- Entity sets represented by rectangles, relationship sets by diamonds, with lines connecting associated entities.

**Representation of Relationships:**
- Various techniques exist for representing relationships, including crows foot notations (greater-than symbol, less-than symbol, vertical line).
- ER diagrams illustrate entities (e.g., Book, Author) and their attributes (properties like title, edition, author details).

**One-to-One Relationship:**
- One entity associated with exactly one instance of another entity.
- Example: A book having only one author.

**One-to-Many Relationship:**
- One entity linked with one or more instances of another entity.
- Example: One book being written by multiple authors.

**Many-to-Many Relationship:**
- Multiple instances of one entity associated with multiple instances of another entity.
- Example: Many authors contributing to multiple books, or vice versa.

➡️ **Mapping Entities to Tables**

**ER Diagrams in Database Design:**
- Entity-Relationship Diagrams serve as the foundational tool for database design.

**Mapping ERD to Relational Database Tables:**
- Begin with an ERD, then translate it into tables for the database.
- Example used: ERD for the entity "Book" with multiple attributes.

**Mapping Entities to Tables:**
- Entity (e.g., "Book") is transformed into a table with the same name ("Book" table).
- All attributes of the entity in the ERD translate into columns within the respective table.
- The entity-to-table mapping separates the entity from its attributes, which then form columns within the table.

**Relational Database Table Representation:**
- Tables in a relational database consist of rows and columns.
- Initially, the entity becomes the table structure, not yet in rows and columns format.
- Attributes of the entity are mapped into columns within the table structure.
- Adding data values to each column completes the formation of rows and columns within the table.

**Example with "Author" Entity:**
- Similar translation process for the "Author" entity: Entity "Author" becomes a table, and attributes become columns within that table.
- Adding data values to the columns finalizes the table structure.

➡️ **Data Types**
**Understanding Data Types in Databases**
- **Database Table Representation**:
  - Represents a single entity.
  - Columns represent attributes of that entity (e.g., a Book table with columns for title, published date, and number of pages).

- **Purpose of Data Types**:
  - Ensure consistency: Data in a column should be of the same type.
  - Column data types define what kind of data can be stored.

- **Common Data Types in Relational Database Management Systems (RDBMS)**:
  - **Character String Data Types**:
    - Fixed length (e.g., CHAR) and variable length (e.g., VARCHAR).
  - **Numeric Data Types**:
    - Integer types and decimal types (e.g., numeric, decimal, real, double, etc.).
  - **Date/Time Data Types**:
    - Dates, times, and timestamps.

- **Other Commonly Used Data Types**:
  - Boolean, binary strings, large objects (LOBs), XML data types.

- **Custom/User Defined Data Types (UDTs)**:
  - Possible in many relational databases, derived or extended from built-in types.

**Advantages of Using Appropriate Data Types**
- **Data Integrity and Accuracy**:
  - Prevents incorrect data insertion.
  - Enables accurate sorting, selection, and manipulation of data.

- **Functional Benefits**:
  - Accurate sorting and selection.
  - Perform calculations and utilize standard functions based on data types.

➡️ **Relational Model Concepts**

- Explain the difference between:
  - Relational schema
  - Relational instance

- The Relational Model:
  - Proposed in 1970
  - Based on a mathematical model and terms
  - Building blocks are Relation and Sets

- Relation in the Relational Model:
  - A mathematical concept based on sets
  - Defined as an unordered collection of distinct elements
  - Represents a collection of items of the same type
  - Characteristics:
    - No order
    - No duplicates

- Relational Database:
  - Composed of relations (tables)
  - A table comprises rows and columns

- Components of a Relation:
  - Relation Schema:
    - Specifies:
      - Name of relation
      - Name and type of each column (attributes)
  - Relation Instance:
    - Table made up of rows and columns
    - Columns are attributes/fields
    - Rows are tuples

- Example: Entity 'Author':
  - Author as the relation name
  - Attributes and their data types:
    - Author_ID (char)
    - Last name, first name, email, city (varchar)
    - Country (char)
  - Representation of Relation Schema

- Degree and Cardinality in a Relation:
  - Degree:
    - Number of attributes (columns) in a relation
  - Cardinality:
    - Number of tuples (rows) in a relation
  - Example:
    - Degree: 6 (6 columns)
    - Cardinality: 5 (5 rows)

Key Takeaways from the Video:

- Relational Model based on the concept of relation (table)
- Relation as a mathematical term for a table
- Degree refers to the number of attributes (columns)
- Cardinality refers to the number of tuples (rows)
- Relation Schema specifies the name of a relation
- Relation Instance is a table comprising attributes and tuples

📓**Introducing Relational Database Products**
➡️ **Database Architectures**

Deployment Topologies:

- Single-Tier Architecture:
  - Small database on a local desktop
  - Limited user access
  - Useful for development, testing, or embedded databases in local applications

- Client-Server Architecture:
  - Larger databases accessed by multiple users
  - Database on a remote server
  - Users access it through client systems (web pages or local applications)
  - Possible inclusion of a middle-tier (application server) between clients and the remote database
  - Commonly used in production environments for multi-user scenarios

- Cloud Deployment:
  - Database resides in a Cloud environment
  - Advantages:
    - No need to download or install database software
    - No infrastructure maintenance required
    - Easy access for users with an internet connection
  - Access through an application server layer or interface in the Cloud
  - Flexible for development, testing, and production environments

2-Tier Architecture (Client-Server Topology):

- Application and database run in separate tiers
- Application in the client tier connects to the database server through:
  - Database interface (API or Framework)
  - Database Client or API on the client system
- Database server comprises multiple layers:
  - Data Access layer (interfaces for different client types)
  - Database Engine layer (compiles queries, retrieves/processes data)
  - Database Storage layer (where data is stored)
![[2-tier.png]]

3-Tier Architecture:

- Also known as a client-server topology
- Three tiers:
  - Presentation layer (interface for end-users)
  - Business logic layer
  - Database server accessed via an application server or middle-tier
  - Communication facilitated by a database API or driver
![[3-tier.png]]
Key Takeaways:

- Databases deployed in various topologies based on processing and access needs
- Single-tier for small, single-user databases
- 2-tier for remote server databases accessed from client systems
- 3-tier for remote server databases accessed via an application server or middle-tier
- Cloud deployments accessible through cloud-based interfaces or application servers


➡️ **Distributed Architectures**


Distributed Database Architectures:

- Shared Disk Architecture:
  - Multiple database servers process workload in parallel
  - Connected to shared storage infrastructure and each other via high-speed interconnects
  - Benefits:
    - Faster workload processing
    - Scalability by distributing client workloads among servers
    - High availability by rerouting clients to other servers in case of server failure
![[Screenshot_3 1.jpg]]
- Database Replication:
  - Technique: Changes on one server replicated to one or more database replicas
  - Benefits:
    - Improved performance through workload distribution
    - High availability with replicas within the same location
    - Disaster recovery by setting up replicas in geographically distributed locations
![[Screenshot_4 1.jpg]]
- Partitioning:
  - Dividing large data tables into multiple logical partitions
  - Example: Sales records by Quarters (Quarter 1, Quarter 2, etc.)
  - Allows for management of subsets of data
  - Commonly used in sharding

- Sharding:
  - Placement of partitions on separate nodes in a cluster
  - Each shard has its compute resources (Processing, Memory, Storage) for its data subset
  - Parallel query processing on multiple nodes for improved performance
  - Scalability: Add shards and nodes to handle increased data or query workloads

Benefits of Partitioning and Sharding:

- Commonly used for data warehousing and business intelligence workloads
- Partitioning enables managing large volumes of data efficiently
- Sharding facilitates improved parallel processing and performance for specific data subsets
![[Screenshot_5 1.jpg]]
Key Takeaways:

- Shared disk architecture allows parallel workload processing and scalability
- Database replication ensures high availability within the same location and disaster recovery in separate locations
- Partitioning divides large tables into logical partitions; sharding distributes partitions across nodes for improved performance

➡️ **Database Users and Usage Patterns**

Major Categories of Database Users:

1. **Data Engineers and Database Administrators (DBAs):**
   - Administrative tasks:
     - Creating and managing database objects
     - Setting access controls
     - Monitoring and performance tuning
   - Mechanisms used:
     - GUI or web-based management tools provided by databases or third-party tools
     - Command-line interfaces and utilities for specific tasks
     - APIs for programmatic access from applications

2. **Data Scientists, Data Analysts, and Business Intelligence (BI) Analysts:**
   - Analyzing data, deriving insights, and making data-driven predictions
   - Read-only access to existing data sources
   - Tools used:
     - For Data Science and Machine Learning: Jupyter, R Studio, Zeppelin, SAS, SPSS
     - Reporting, Dashboarding, and Business Intelligence: Excel, IBM Congos, PowerBI, Tableau, MicroStrategy
     - SQL interfaces and APIs to interface with relational databases

3. **Application Developers:**
   - Create applications requiring read and write access to databases
   - Programming languages used:
     - C++, C#, Java, JavaScript, .Net, PHP, Perl, Python, Ruby
   - Accessing databases through:
     - SQL interfaces and APIs (ODBC, JDBC, REST APIs)
     - ORM frameworks to simplify database interaction and mask complexity (ActiveRecord, Django, Entity Framework, Hibernate, Sequelize)

Interfaces and Tools for Database Access:

- Graphical and Web Interfaces:
  - Ease of visual interaction with databases
- Command-line tools and scripts:
  - Power for automation and experienced Data Engineers
- APIs and ORMs:
  - Aid application developers in creating user-friendly applications

Categories of Database Applications:

- Database Management Tools (phpMyAdmin, pgAdmin)
- Data Science and BI Tools (Excel, IBM Congos, MicroStrategy)
- Purpose-built or off-the-shelf business applications (e-commerce, supply chain, etc.)

Key Takeaways:

- Users categorized into Data Engineers, Data Scientists, Business Analysts, and Application Developers
- Access methods vary based on user needs: GUIs, command-line tools, APIs, and ORMs
- Database applications range from management tools to data analysis and business-specific applications
➡️ **Introduction to Relational Database Offerings**

**History of Relational Databases:**

- 1960s: IBM Sabre Seat Reservation System was the first recognizable relational database.
- Early 70s: Edgar F. Codd defined 12 rules for relational databases.
- Late 70s: Ingres at UC Berkeley and System R at IBM San Jose were developed.
- 1976: Peter P. Chen proposed the Entity-Relationship (ER) model.
- 1980s: Relational databases commercially succeeded with IBM's Db2 and SQL standardization.
- Late 80s: IBM designed distributed relational database architecture for network-connected databases.
- Early 90s: Client tools like Oracle Developer, PowerBuilder, and VB gained popularity.

**Evolution and Popularity:**

- Late 90s: Database industry experienced exponential growth, and desktop users accessed client-server databases.
- 2000s: Open source databases like MySQL and PostgreSQL gained traction.
- 2010s: Cloud databases soared in popularity with Amazon RDS, IBM Db2 on Cloud, Microsoft SQL Azure, Oracle Cloud.

**Popular Relational Databases:**

- Commercial Leaders: Oracle, Microsoft SQL Server, IBM Db2.
- Open Source: MySQL (Oracle), PostgreSQL, SQLite.
  
**Popularity Assessment:**

- DB Engines' ranking (February 2021):
  - Oracle
  - MySQL
  - Microsoft SQL Server
  - PostgreSQL
  - IBM Db2
  - SQLite
  - Microsoft Access
  - MariaDB
  - Hive
  - Microsoft Azure SQL Database

**Trends in Database Popularity:**

- Shift from commercial to open source: Approx. 50% market share for each.
- Cloud database popularity: Doubled in the past decade.
- Forecast: Gartner predicts 75% of databases to be on the cloud by 2022.
  
**Cloud Databases:**

- Offered through cloud platforms like Amazon DynamoDB, Microsoft Azure Cosmos DB, Google BigQuery.
- Benefits include scalability and compatibility with cloud computing.
  
**Key Takeaways:**

- Relational databases available with both commercial and open-source licensing.
- Open source databases now hold approximately 50% market share.
- Cloud databases have seen exponential growth, doubling in popularity over the past decade.

➡️ **Db2 Overview**

**Db2 History and Products:**

- Released by IBM in 1983 as a relational database management system.
- Evolved to run on multiple platforms including mainframes, OS/2, UNIX, Linux, and Windows.
- Db2 Suite includes: Db2 Database, Db2 Warehouse, Db2 on Cloud, Db2 Big SQL, Db2 Event Store, and Db2 for z/OS.

**Evaluation and Licensing:**

- Various options for evaluation such as Db2 Database Community License, free Docker image, and Lite Plan of Db2 on Cloud.
- Trial editions available for Db2 Warehouse Enterprise Edition and Db2 Big SQL.

**Key Features:**

- Utilizes AI-powered functionality for data management.
- Includes machine learning algorithms, column store feature, and data skipping for improved query efficiency.
- Common SQL engine for seamless migration between Db2 products and platforms.
- Supports relational, structured, and unstructured data.

**Db2 Family Products:**

- Db2 Database: Enterprise-ready RDBMS optimized for OLTP.
- Db2 Warehouse: On-premises data warehouse for advanced analytics.
- Db2 on Cloud: Fully managed cloud-based SQL database.
- Db2 Warehouse on Cloud: Elastic, cloud-based data warehouse.
- Db2 Big SQL: SQL-on-Hadoop engine for advanced querying.
- Db2 Event Store: Memory-optimized database for event-driven applications.
- Db2 for z/OS: Enterprise data server for IBM Z.

**Cloud Pak for Data:**

- Integrated data and AI platform on Red Hat OpenShift for managing all data sources.
- Offers connectivity to Db2 and other data sources, analytics services, and AI integration.

**Db2 on Cloud Plans:**

- Lite Plan: Free, time-unlimited with limitations on data size and connections.
- Standard Plan: Flexible scaling and high availability clustering.
- Enterprise Plan: Dedicated instance with flexible scaling and high availability clustering.

**Deployment and Access:**

- Deploy on IBM Cloud or Amazon Web Services (AWS).
- Access via command line interface, GUI console, or standard APIs like ODBC, JDBC, and REST.
- Supports data loading from various sources programmatically.

**High Availability and Disaster Recovery (HADR):**

- HADR functionality replicates changes to standby servers for failover support.
- Automatically promotes standby databases in case of primary database failure.

**Scalability with Partitioning:**

- Db2 Warehouse offers massively parallel processing and scalability.
- Easily scale storage capacity by adding or removing nodes to rebalance partitions.

**Key Takeaways:**

- Db2 provides a suite of products for diverse data management needs.
- Available for deployment across multiple platforms including on-premises and cloud.
- Db2 on Cloud offers managed SQL databases on IBM Cloud or AWS.
- Offers high availability, disaster recovery, and scalability functionalities.
## W2 ❉ Using Relational Database
📓**Creating Tables and Loading Data**

➡️ **Types of SQL statements (DDL vs. DML)**

**Data Definition Language (DDL) Statements**
- CREATE: Used to create tables and define their columns.
- ALTER: Modifies tables by adding or dropping columns or altering their data types.
- TRUNCATE: Deletes all data within a table but retains the table structure.
- DROP: Deletes entire tables from the database.

**Data Manipulation Language (DML) Statements**
CRUD operations: Create, Read, Update, and Delete rows in a table
1. INSERT: Adds new rows of data into a table.
2. SELECT: Retrieves or reads rows from a table.
3. UPDATE: Modifies existing rows in a table.
4. DELETE: Removes specific rows of data from a table.

➡️ **Creating Tables**
**Considerations for Creating Tables:**
- Database Schema: Defines logical groupings of database objects (tables, views, functions, etc.).
- Information Needed: Table name, column names, data types for each column, allowance of duplicate or null values.
- Utilize Entity Relationship Diagram (ERD) for guidance in table creation.

**Creating Tables:**
- Visual Interface: Available in most databases for small tasks but not suitable for scaling.
- SQL Statement (CREATE TABLE): Ideal for automating table creation for multiple tables.
- Administrative APIs: Some databases offer programmatically managing databases.

**Key Takeaways:**
- Relational Database Management Systems (RDBMS) typically use schemas to organize various database objects.
- GUI interfaces in RDBMS facilitate table creation, but SQL statements also serve this purpose.
- Tables can be modified after creation to include new columns, change data types, or add primary/foreign keys.

➡️ **CREATE TABLE Statement**

**Example: Creating a Table for Provinces in Canada:**
```sql
CREATE TABLE provinces (
    id CHAR(2) PRIMARY KEY NOT NULL,
    name VARCHAR(24)
);
```
- `id`: Stores abbreviated province codes (e.g., AB, BC).
- `name`: Stores full province names (e.g., ALBERTA, BRITISH COLUMBIA).

**Elaborate Example Based on a Library Database:**
- Creation of the `AUTHOR` table from the `AUTHOR` entity.
```sql
CREATE TABLE table_name(
column1 data type, column2 data type, ...
);

CREATE TABLE author (
    author_id CHAR(2) PRIMARY KEY NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    email VARCHAR(40),
    city VARCHAR(15),
    country CHAR(2)
);
```
- `author_id`: Assigned as the Primary Key to ensure uniqueness.
- `lastname` and `firstname`: Constrained with NOT NULL to prevent NULL values.
- `email`, `city`, `country`: Define other attributes without specific constraints.

**Key Points:**
- `CREATE` is a DDL statement used to create tables in a database.
- `CREATE TABLE` statement defines columns with their names, datatypes, and optional constraints (e.g., Primary Key, NOT NULL).
- The Primary Key ensures unique identification of each tuple (row) in the table.
- Constraints like `NOT NULL` enforce data integrity rules, ensuring specific columns cannot contain NULL values.

➡️ **ALTER, DROP, and Truncate tables**

**Syntax and Use Cases:**

1. **ALTER TABLE Statement:**
   - Used to modify the structure of an existing table.
    - Allows addition or removal of columns, modification of data types, keys, and constraints.
```sql

ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name;

ALTER TABLE table_name
MODIFY column_name datatype; --> change the data type of a column in a table

ALTER TABLE table_name
RENAME TO new_table_name; --> rename an existing table.

```


2. **Modifying Data Types with ALTER TABLE:**
   - Syntax: `ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE new_data_type;`
   - Example: `ALTER TABLE author ALTER COLUMN telephone_number SET DATA TYPE CHAR(20);`
   - Changing data types requires compatibility with existing data; inconsistencies might cause errors.

3. **Dropping a Column with ALTER TABLE:**
   - Syntax: `ALTER TABLE table_name DROP COLUMN column_name;`
   - Example: `ALTER TABLE author DROP COLUMN telephone_number;`
   - Used to remove unnecessary columns from a table.

4. **DROP TABLE Statement:**
   - Deletes an entire table from the database.
   - Removes the table and its associated data.
```sql
DROP TABLE table_name;  --> delete a table from the database.

DROP DATABASE database_name;  --> delete an entire database

DROP INDEX index_name;   --> remove an index from a table

DROP VIEW view_name;   --> delete a view.

DROP PROCEDURE procedure_name; --> remove a stored procedure.

DROP TRIGGER trigger_name;  --> to delete a trigger.

DROP FUNCTION function_name; --> remove a user-defined function.

```
5. **TRUNCATE TABLE Statement:**
   - Deletes all rows/data in a table, leaving the table structure intact.
   - Efficiently deletes data but retains the table structure.
```sql
TRUNCATE TABLE table_name;
```

➡️ **Data Movement Utilities**

**Purpose of Data Movement:**
- Necessitated in databases for various reasons like initial population, creating development copies, disaster recovery, etc.
  
**Categories of Tools and Utilities:**
1. **Backup and Restore:**
   - **Backup:** Saves database objects and their data for recovery and duplication.
   - **Restore:** Creates a copy of the original database from the backup files.
   - Preserves entire database structure, objects, and data.

2. **Import and Export:**
   - **Import:** Reads file data and performs INSERT statements to a target table.
   - **Export:** Selects table data and saves it into a file.
   - Supported through command line, management APIs, and graphical tools.
   - Multiple file formats supported (DEL, ASC, PC/IXF, JSON) for Importing and Exporting data.

3. **Load Utilities:**
   - **Load:** Faster data insertion by writing formatted pages directly into the database.
   - Bypasses database logging for higher performance.
   - Preferable for large data volumes but skips constraint checking.

**Examples and Utilities:**
- **DB2 Example:** 
  - Command line import/export utilities.
  - Exporting a table to a CSV file using the Db2 console.
  
**Key Learnings:**
- Data movement is essential for database management, including backups, inserts, and exports.
- Backup and Restore utilities are for database duplication and recovery.
- Import and Export tools facilitate data movement between files and database tables.
- Load utilities offer faster data insertion, ideal for large datasets.

➡️ **Loading Data**

**Purpose of Load Data Functionality:**
- Efficiently loads large amounts of data into tables.
- Practical for handling hundreds or thousands of rows compared to individual INSERT statements.
- Enables loading data from various sources and formats.

**Types of Data Sources for Loading Data:**
- Delimited text files (e.g., CSV files).
- S3 Object Storage (Amazon Web Services).
- Cloud Object Storage (IBM Cloud).

**Four Steps in the Load Data Process using Db2 Web Console:**
1. **Source Identification:**
   - Select the source data location (local file or cloud storage).
   - Enter authentication details for cloud storage (e.g., IBM Cloud Object Storage).

2. **Target Selection:**
   - Choose the target schema and table for data loading.
   - Option to append new data or overwrite existing data (caution: overwriting deletes existing data).

3. **Define Data Aspects:**
   - Set character encoding, delimiters, and handling for column headings and date formats.

4. **Final Review:**
   - Review all settings before initiating the data load.

**Benefits and Outcomes:**
- Loading data through this utility is quicker, more efficient, and scalable compared to using multiple INSERT statements.
- Flexibility to load data from different sources and formats using the Db2 Web Console.

📓**Designing Keys, Indexes, and Constraints**

➡️ **Database Objects & Hierarchy (Including Schemas)**

**Hierarchy of Database Objects:**
- **Instance:** A single organization of a database and its contents; can contain multiple databases.
- **Schema:** A logical grouping of objects within a database, defining naming conventions and preventing ambiguities.
- **Database Objects:** Tables, constraints, indexes, etc., within a schema.
- **System Catalog Tables:** Record details of objects within a database.
- **Configuration Files:** Specific to each database within an instance.
![[Screenshot_6.jpg]]

**Instances and Databases:**
- **Instance:** Organizes databases and sets configuration parameters.
- **Multiple Instances:** Useful for separating development and production environments, controlling access.
- **Cloud-Based Instances:** Represents a running copy of a service in cloud-based RDBMSes.
![[Screenshot_7.jpg]]
**Relational Database:**
- A collection of objects for storing, managing, and accessing data.
- Objects include tables, views, indexes, functions, triggers, and packages.
- Focus on establishing relationships between tables to reduce redundancy and enhance data integrity.

**Schemas:**
- Logical grouping of database objects, providing a naming context.
- Differentiates between objects with the same name in different schemas.
- User Schemas: Contain user-defined database objects (tables, views, functions).
- System Schemas: Hold configuration info and metadata for the database.

**Database Partitioning:**
- Management of data across multiple partitions for large volumes of data.
- Useful in scenarios like data warehousing and business intelligence analysis.

**Common Database Objects:**
- **Tables:** Logical structures to store data.
- **Constraints:** Enforce rules and restrictions on data.
- **Indexes:** Improve performance and ensure data uniqueness.
- **Views:** Different representations of data.
- **Aliases:** Alternative names for objects.

**Creating and Managing Database Objects:**
- Done through graphical tools, scripting, or APIs.
- SQL statements like CREATE or ALTER used in Data Definition Language (DDL) for object management.

**Key Takeaways:**
- Instance organizes databases and their parameters.
- Relational databases manage data using various objects.
- Schemas logically group database objects and aid in naming contexts.
- Database partitioning manages large volumes of data across partitions.
- Database objects include tables, constraints, indexes, views, and aliases.

➡️ **Primary Keys and Foreign Keys**

**Primary Keys:**
- Uniquely identifies every row in a table.
- Could be a naturally occurring unique attribute or a newly added column.
- Single or composite (across two or more columns) primary keys are possible.
- Only one primary key allowed per table.
```sql
CREATE TABLE table_name (
    column1 datatype PRIMARY KEY,
    column2 datatype,
    ...
);

--> Creating a table with a primary key
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

--> Adding primary key using ALTER TABLE
ALTER TABLE students
ADD PRIMARY KEY (student_id);

```


**Foreign Keys:**
- Exists in a table but contains information matching a primary key in another table.
- Maintains referential integrity between tables.
- Used to establish relationships between tables.
- Specifies actions for updates or deletions in the parent table (e.g., CASCADE, SET NULL).
```sql
CREATE TABLE child_table (
    column1 datatype,
    column2 datatype,
    FOREIGN KEY (column1) REFERENCES parent_table(parent_column)
);

--> Creating a table with a foreign key constraint

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

--> Adding foreign key using ALTER TABLE
ALTER TABLE courses
ADD CONSTRAINT fk_student_id
FOREIGN KEY (student_id) REFERENCES students(student_id);




```


**Creating Relationships:**
- Foreign keys link to primary keys in other tables, ensuring data consistency.
- Helps ensure that values in a child table always refer to valid entries in the parent table.

**Key Takeaways:**
- Primary keys enforce uniqueness in a table.
- Foreign keys link tables by referencing the primary key of another table.
- Establishing primary and foreign keys creates relationships between tables, ensuring data integrity and consistency.

➡️ **Indexes**

**What are Indexes?**
- Indexes in a database serve as ordered pointers to rows in a table.
- They help speed up data retrieval by allowing quick access to specific rows or subsets of rows.

**Creating Indexes:**
- Use the CREATE INDEX statement to define an index, specifying its name, uniqueness, table, and column on which it's based.
- Primary keys automatically create an index by default. Custom indexes can be created on frequently searched columns.
```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
--> Creating a Simple Index
CREATE INDEX idx_student_id
ON students (student_id);

--> Creating a Unique Index
--> A unique index ensures that the indexed columns contain unique values, allowing fast searches for uniqueness:
CREATE UNIQUE INDEX idx_unique_email
ON users (email);

--> Composite Index
--> A composite index involves multiple columns to create an index on the combination of these columns:

CREATE INDEX idx_composite
ON orders (customer_id, order_date);

```


**Advantages of Indexes:**
- Improved performance of SELECT queries, especially when searching on indexed columns.
- Reduction in the need for sorting data when specific orders are frequently required.
- Guaranteed uniqueness of rows if created with the UNIQUE clause.

**Disadvantages of Indexes:**
- Increased disk space usage for each index created.
- Decreased performance of INSERT, UPDATE, and DELETE queries due to the overhead of maintaining sorted rows.

**Considerations for Index Creation:**
- Weigh the advantages and disadvantages before creating an index.
- Useful when SELECT queries are frequent and update operations are infrequent.
- Creating too many indexes can potentially negate performance benefits, analogous to an overly cluttered book index.

**Key Takeaways:**
- Indexes provide quick access to specific rows or subsets of rows in a table.
- They enhance SELECT query performance but might degrade performance for INSERT, UPDATE, and DELETE queries.
- Consider the trade-offs between improved query performance and increased storage/overhead when creating indexes.

➡️ **Normalization**

**Purpose of Normalization:**
- Normalization is the process of organizing data in a database to reduce redundancy and enhance consistency.

**Normal Form Levels:**
- **First Normal Form (1NF):**
  - Requires each row to be unique and each cell to contain only a single value.
  - Involves breaking down tables to ensure that no cell contains a list of values.
  
- **Second Normal Form (2NF):**
  - Builds upon 1NF and specifies separation of groups of values applying to multiple rows by creating new tables.
  - Ensures that data duplication is reduced and values are logically grouped in tables.
  
- **Third Normal Form (3NF):**
  - Builds upon 2NF and emphasizes eliminating columns that do not depend on the primary key.
  - Removes dependencies on non-key columns, focusing on data integrity.

**Normalization Process:**
- Moving from one normal form to another involves restructuring tables to adhere to the specific normal form requirements.
- Involves creating relationships between tables using primary and foreign keys to ensure data integrity.

**Advanced Normal Forms:**
- There exist higher normal forms such as Boyce Codd Normal Form (BCNF), fourth, and fifth normal forms for specific scenarios.
- In transactional systems (OLTP), data is typically normalized up to 3NF for efficient processing and storage.
- Analytical systems (OLAP) might denormalize data for read performance in data warehousing, where fewer tables can optimize query performance.

**Key Takeaways:**
- Normalization reduces data redundancy and enhances consistency.
- 1NF ensures uniqueness and single-value cells.
- 2NF separates groups of values into different tables.
- 3NF eliminates columns not dependent on the primary key for each table.

➡️ **Relational Model Constraints - Advanced**

**Purpose of Constraints:**
- Constraints in a relational model enforce rules and ensure data integrity in databases by imposing restrictions.

**Types of Constraints:**
1. **Entity Integrity Constraint:**
   - Ensures the primary key uniqueness in a relation.
   - Primary key values cannot accept NULL (unknown) values.
   - Prevents duplicate values in a table.

2. **Referential Integrity Constraint:**
   - Defines and maintains relationships between tables using primary and foreign keys.
   - Ensures the validity of data relationships.
   - Example: Ensuring books have at least one associated author.

3. **Semantic Integrity Constraint:**
   - Focuses on the correctness of data meaning.
   - Rejects values that do not align with the data's intended meaning.
   - Example: Ensuring meaningful values in attributes like City or Country.

4. **Domain Constraint:**
   - Specifies permissible values for attributes.
   - Ensures that attribute values fall within defined domains.
   - Example: Specifying two-letter country codes for the Country attribute.

5. **Null Constraint:**
   - Specifies that attribute values cannot be NULL.
   - Ensures that critical attributes have meaningful values.
   - Example: Making sure Name attributes like FirstName and LastName cannot be NULL.

6. **Check Constraint:**
   - Enforces domain integrity by restricting accepted attribute values.
   - Limits the range or type of values accepted by an attribute.
   - Example: Restricting publication year values to prevent future years in the Year attribute.

**Key Takeaways:**
- Entity Integrity ensures primary key uniqueness.
- Referential Integrity maintains valid relationships between tables.
- Semantic Integrity focuses on the correctness of data meaning.
- Domain Constraint ensures permissible attribute values.
- Null Constraint restricts NULL attribute values.
- Check Constraint limits accepted attribute values.


## W3 ❉ MySQL and postgreSQL
📓**MySQL**
➡️ **Getting Started with MySQL**

**Ways to Use MySQL:**
- MySQL is an open-source RDBMS available for free under the GNU General Public License.
- It offers various editions (Community, Standard, Enterprise, Cluster) with additional functionalities in commercial versions.
- Available for local installation or can be used in the cloud (e.g., IBM Cloud, Amazon RDS, Azure Database, Google Cloud SQL).

**Popular MySQL Tools:**
1. **mysql Command-Line Interface:**
   - Used to interact with MySQL server and data through commands.
   - Supports interactive usage or command execution from text files.
   - Allows tasks such as listing databases, importing/exporting data.

2. **mysqladmin:**
   - Command-line program for administering RDBMS tasks.

3. **MySQL Workbench:**
   - Visual tool for SQL development, administration, database design, and maintenance.
   - Offers a unified environment for various MySQL-related tasks.
   - Features administration capabilities, data import/export, server logs, and performance reports.

4. **phpMyAdmin:**
   - Web-based GUI for MySQL databases.
   - Enables interaction with databases, creation of databases/tables, data loading/querying, and data import/export.

**Key Points:**
- MySQL can be installed on local desktop servers or used via cloud-based managed services.
- Command-line interfaces like `mysql` and `mysqladmin` facilitate database management.
- MySQL Workbench offers a comprehensive development environment for MySQL databases.
- phpMyAdmin is a web interface allowing interaction and management of MySQL databases.




📓**PostgreSQL**

➡️ **Getting Started with PostgreSQL**

- **PostgreSQL Overview**
  - Description of PostgreSQL as an open source object-relational database management system
  - Reputation for reliability, flexibility, and support for various data types
  - Popularity in OLTP, data analytics, and geographic information systems

- **Ways to Use PostgreSQL**
  - Installation on personal servers (macOS, UNIX, Windows)
  - Self-management in virtual machines or containers in the cloud
  - Managed services like IBM Cloud Databases for PostgreSQL, Amazon RDS, Google Cloud SQL, EnterpriseDB cloud, and Microsoft Azure for PostgreSQL

- **Tools for Accessing PostgreSQL**
  - `psql`: Command line interface for PostgreSQL
  - `pgAdmin`: Open-source graphical interface available as a desktop or web application
  - Other commercial options like Navicat and Dbeaver for PostgreSQL and other databases

- **Working with PostgreSQL Tools**
  - `psql`: Interactive command line tool for Postgres databases
    - Running interactive queries
    - Displaying database object information

  - `pgAdmin`: Multi-functional tool for development and administration
    - Creation of databases, tables, stored procedures, and functions
    - Data loading, querying, managing objects, security, and usage monitoring

  - **Query Tool in pgAdmin**
    - Executing SQL commands and interacting with their results
    - Upper pane for entering SQL queries and lower pane displaying results
    - Editing editable results and viewing query plan, server messages, and notifications

  - **ERD Tool in pgAdmin**
    - Creating entity-relationship diagrams
    - Generating SQL statements for creating database objects
    - Modifying tables, relationships, adding notes, and SQL statement generation

- **Key Takeaways from the Video**
  - Installation options for PostgreSQL: personal servers or cloud
  - `psql` as a command-line interface
  - `pgAdmin` as a comprehensive database management tool for PostgreSQL with object navigation, Query Tool, and ERD Tool.


➡ **Creating Databases and Loading Data in PostgreSQL**
```sql
--> To create a database in PostgreSQl
CREATE DATABASE database_name;


--> Loading Data into PostgreSQL:

--> 1- access the desired database:
psql -U username -d database_name

--> 2- load data from an external file (like a CSV) into a table:
\copy table_name FROM 'path/to/your/data.csv' DELIMITER ',' CSV HEADER;
or
COPY table_name FROM 'path/to/your/data.csv' DELIMITER ',' CSV HEADER;

```

➡️ **Understanding Views in PostgreSQL**

- **Definition of Views**
  - Views provide an alternate representation of data sourced from one or multiple tables or views.
  - They offer similar interaction capabilities as tables, enabling operations like insertion, updating, and deletion of data.

- **Purpose and Benefits of Using Views**
  - Views serve to restrict access to sensitive information.
  - Simplify data retrieval by presenting consolidated or processed data.
  - Reduce direct access to underlying tables, enhancing security.

- **Creating and Using Views in PostgreSQL**
  - Views are created within a schema using the interface.
  - Process: Right-click on Views > Create > View, then provide a name and define the view using SQL code in the Code page.
  - Display and interact with created views by expanding the Views folder and viewing the included columns.
  - Running the view: Right-click view name > View/Edit Data > All Rows to display all rows within the view.

- **Materialized Views**
  - An advanced form of view where the result set is saved or materialized for future use.
  - Benefits: Improved performance due to readily available result sets, typically stored in memory.
  - Limitations: Data stored in materialized views cannot be updated or deleted directly.

- **Creating and Using Materialized Views in PostgreSQL**
  - Similar creation process to regular views but initiated from the materialized views folder.
  - Defining a materialized view involves specifying the code to define it.
  - Post creation, the materialized view needs to be refreshed to synchronize it with the underlying tables.
  - Materialized views enable faster access to stored data but require occasional refreshing to update.

- **Key Takeaways from the Video**
  - Views offer an alternative representation of data.
  - Use views to control access and simplify data retrieval.
  - Materialized views store result sets for faster access but do not support direct data modification.
## W4 ❉ Course assignment
📓**assignment**
➡ **Approach to Database Design (Including ERD)**

- **Importance of Good Database Design**
  - Crucial for success in data-driven projects.
  - Contributes to data integrity, reduces redundancy, enhances application performance, and ensures user satisfaction.

- **Database Design Process: Three Key Stages**
  1. **Requirements Analysis:**
     - Analyzing data, understanding data usage requirements.
     - Identifying base objects, relationships, and associated information.
     - Methods include reviewing existing data stores and interviewing users for current and potential usage scenarios.

  2. **Logical Design:**
     - Mapping requirements to entities, attributes, and relationships.
     - Objects identified in the analysis become entities; their features become attributes.
     - Logical models avoid technical specifics, focusing on conceptual structuring.

  3. **Physical Design:**
     - Implementing the logical design into the chosen database management system.
     - Considering database-specific features such as data types, naming conventions, indexes, and constraints.
     - Translating logical entities and attributes into tables and columns with defined keys.

- **Entity-Relationship Diagram (ERD) Tool Purpose**
  - Supports visualization of database design.
  - Enables the creation of ER diagrams and generates SQL scripts for database creation based on the design.
  - Example: pgAdmin includes an ERD Tool for designing and generating databases.

- **Normalization and its Role**
  - Helps optimize databases for transactional (OLTP) or analytical (OLAP) performance.
  - Emphasizes adherence to normal forms (e.g., 1st, 2nd, 3rd normal form).
  - Example: Splitting attributes into separate entities to ensure data integrity.

- **Key Takeaways from the Video**
  - Emphasizes the significance of thorough database design before implementation.
  - Outlines the sequential phases: requirements analysis, logical design, and physical design.
  - Advocates the use of ERD designers for simplifying the design process.
