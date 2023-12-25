
# Code for ETL operations on Country-GDP data

# Importing the required libraries
import pandas as pd 
from bs4  import BeautifulSoup
import requests 
from datetime import datetime 
import numpy as np
import sqlite3

# initialize all the known entities
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
exchange_rate_path = 'exchange_rate.csv'

table_attribs = ['Name', 'MC_USD_Billion']
db_name = 'Banks.db'
table_name = 'Largest_banks'
conn = sqlite3.connect(db_name)
query_statements = [
        'SELECT * FROM Largest_banks',
        'SELECT AVG(MC_GBP_Billion) FROM Largest_banks',
        'SELECT Name from Largest_banks LIMIT 5'
    ]

logfile = 'code_log.txt'
output_csv_path = 'Largest_banks_data.csv'


#Task 1: Logging function
def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timeformat = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    #Convert the timestamp to a formatted string based on the time format
    timestamp = now.strftime(timeformat)
    
    with open(logfile, 'a') as f:
        f.write(timestamp + ' : ' + message + '\n')


 # Task 2 : Extraction of data
        
def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    
    #Create an empty DataFrame with specified column names
    df = pd.DataFrame(columns = table_attribs)

    #Fetch the HTML content from the provided URL
    page = requests.get(url).text
     
    #Parse the HTML content using BeautifulSoup
    data = BeautifulSoup(page, 'html.parser')
   
   #Find all table bodies in the HTML and select the first one
    tables = data.find_all('tbody')[0]
    #Find all table rows in the selected table body
    rows = tables.find_all('tr')

   #Iterate through each row in the table
    for row in rows:
        #Find all table cells (columns) in the row
        col = row.find_all('td')
        if len(col) != 0:
             # Extract the second anchor tag from the second column (index 1)
            ancher_data = col[1].find_all('a')[1]
            # Check if anchor_data exists
            if ancher_data is not None:
                # Create a dictionary containing 'Name' and 'MC_USD_Billion'
                data_dict = {
                    'Name': ancher_data.contents[0],
                    'MC_USD_Billion': col[2].contents[0]
                }
                # Create a temporary DataFrame (df1) from the data_dict
                df1 = pd.DataFrame(data_dict, index = [0])
                # Concatenate the temporary DataFrame with the main DataFrame (df)
                df = pd.concat([df, df1], ignore_index = True)
# Extract 'MC_USD_Billion' column values and convert them to float
    USD_list = list(df['MC_USD_Billion'])
    USD_list = [float(''.join(x.split('\n'))) for x in USD_list]
    # Update the 'MC_USD_Billion' column in the DataFrame with the converted values
    df['MC_USD_Billion'] = USD_list

    return df

#Task 3 : Transformation of data
def transform(df, exchange_rate_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    csvfile = pd.read_csv(exchange_rate_path)

    dict = csvfile.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * dict['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * dict['INR'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * dict['EUR'],2) for x in df['MC_USD_Billion']]

    return df

#Task 4: Loading to CSV
def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

#Task 5: Loading to Database
def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

#Task 6: Function to Run queries on Database

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    for query in query_statements:
        print(query)
        print(pd.read_sql(query, sql_connection), '\n')




log_progress('Preliminaries complete. Initiating ETL process.')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process.')


df = transform(df, exchange_rate_path)
log_progress('Data transformation complete. Initiating loading process.')

load_to_csv(df, output_csv_path)
log_progress('Data saved to CSV file.')

log_progress('SQL Connection initiated.')


load_to_db(df, conn, table_name)
log_progress('Data loaded to Database as table. Running the query.')

run_query(query_statements, conn)
conn.close()
log_progress('Process Complete.')