
# Project: Acquiring and Processing Information on the World's Largest Banks

## Overview:
This project involved the creation of an automated system to compile and process information about the top 10 largest banks globally, ranked by market capitalization in billion USD. The project aimed to transform and store this data in GBP, EUR, and INR based on provided exchange rate information, saving the processed information locally in both CSV and database formats. The process was designed to be repeatable for quarterly reports.

## Code Information:
- **Code Name:** `banks_project.py`
- **Data URL:** [List of largest banks](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)
- **Exchange Rate CSV Path:** [Exchange rate CSV file](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)
- **Output CSV Path:** `./Largest_banks_data.csv`
- **Database Name:** `Banks.db`
- **Table Name:** `Largest_banks`
- **Log File:** `code_log.txt`

## Project Tasks:

### Task 1: Logging Progress
- Implemented the `log_progress()` function to log progress stages in `code_log.txt` at specified checkpoints.

### Task 2: Data Extraction
- Inspected the webpage structure and identified the relevant table under the 'By market capitalization' section.
- Developed the `extract()` function to extract tabular information from the provided URL and saved it to a dataframe.

### Task 3: Data Transformation
- Created the `transform()` function to add columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, utilizing the provided exchange rate information from the CSV file.

### Task 4: Export to CSV
- Implemented the `load_to_csv()` function to load the transformed dataframe into an output CSV file (`Largest_banks_data.csv`).

### Task 5: Database Population
- Developed the `load_to_db()` function to load the transformed dataframe into an SQL database table (`Largest_banks`) within the `Banks.db` database.

### Task 6: Database Querying
- Executed a set of pre-defined queries on the populated database table to verify successful data insertion.

### Task 7: Log Verification
- Ensured all stages of the code execution were properly logged by cross-checking the contents of `code_log.txt`.

## Usage Instructions:
- Execute `banks_project.py` to run the entire process.
- Ensure all required dependencies are installed before running the code.
- Verify the generated outputs in CSV format and within the created SQLite database.
