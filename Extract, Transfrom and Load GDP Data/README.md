
---

# Extract, Transform and Load GDP Data

## Project Overview

### Project Scenario:
You have been recruited by an international firm aiming to expand its global operations. As a junior Data Engineer, your task is to develop an automated script capable of extracting and organizing a list of countries based on their Gross Domestic Product (GDP) in billion USD, as documented by the International Monetary Fund (IMF). The script should retrieve this updated information from the IMF's data available on a specific URL, provided below.

### Project Requirements:
- **URL**: [IMF GDP Data - Web Archive Link](https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29)
- **Output Files**:
  - CSV File: `Countries_by_GDP.csv`
  - Database Table: `Countries_by_GDP` in `World_Economies.db`
- **Attributes**:
  - `Country`: Country name
  - `GDP_USD_billion`: GDP in billion USD (rounded to 2 decimal places)
- **Code File**: `etl_project_gdp.py`

### Objectives:
You are tasked with completing the following tasks for this project:

1. **Data Extraction**:
   - Write a function to extract relevant information from the provided URL.

2. **Transformation**:
   - Convert the available GDP data from 'Million USD' to 'Billion USD'.

3. **Loading**:
   - Store the transformed data into a CSV file (`Countries_by_GDP.csv`) and a database file (`World_Economies.db`).

4. **Database Query**:
   - Run a query on the `Countries_by_GDP` table to display entries with a GDP exceeding 100 billion USD.

5. **Logging**:
   - Log the code execution process with appropriate timestamps in a file named `etl_project_log.txt`.

## Execution Steps

1. Run the Python script `etl_project_gdp.py` to initiate the automated process.
2. Monitor the console for progress updates and results.
3. Refer to generated files (`Countries_by_GDP.csv`, `World_Economies.db`, `etl_project_log.txt`) for detailed information and logs.

The successful execution of this script demonstrates its capability to fetch, transform, and store IMF GDP data into accessible CSV and database formats.

---
