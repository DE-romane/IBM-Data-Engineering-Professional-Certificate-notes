# read README file  first
#required data seems to be available on the URL
#'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'


# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

# initialize all the known entities
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

table_attribs = ["Country", "GDP_USD_millions"] #columns for the dataframe
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'

#Task 1: Extracting information

def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''

    #1-Extract the web page as text.
    page = requests.get(url).text
    #2-Parse the text into an HTML object
    data = BeautifulSoup(page,'html.parser')
    #3-Create an empty pandas DataFrame columns as the table_attribs.
    df = pd.DataFrame(columns=table_attribs)
    #4-Extract all 'tbody' attributes of the HTML object and then extract all the rows of the index 2 table using the 'tr' attribute.
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    #5-Check the contents of each row, having attribute ‘td’, for the following conditions.
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:#The row should not be empty.
            #The first column should contain a hyperlink.
            #The third column should not be '—'.
            if col[0].find('a') is not None and '—' not in col[2]:
                #Store all entries matching the conditions in step 5 to a dictionary with keys the same as entries of table_attribs. Append all these dictionaries one by one to the dataframe.
                data_dict = {"Country": col[0].a.contents[0],
                             "GDP_USD_millions": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df


#Task 2: Transform information



def transform(df):
        ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
        
        GDP_list = df["GDP_USD_millions"].tolist()
        #convert the currency text into numerical text. Type cast the numerical text to float.
        GDP_list = [float("".join(x.split(','))) for x in GDP_list]
        # Divide all these values by 1000 and round it to 2 decimal places
        GDP_list = [np.round(x/1000,2) for x in GDP_list]
        df["GDP_USD_millions"] = GDP_list
        #Modify the name of the column from 'GDP_USD_millions' to 'GDP_USD_billions'
        df=df.rename(columns = {"GDP_USD_millions":"GDP_USD_billions"})
        return df

#Task 3: Loading information

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

# Task 4: Querying the database table
    
def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
     prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

# Task 5: Logging progress
def log_progress(message): 
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')


#Function calls

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('World_Economies.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()