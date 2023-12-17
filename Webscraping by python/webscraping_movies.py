# extract the information of the top 50 movies with the best average rating from the web link shared below.

# https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

# libraries for this lab.
# pandas library for data storage and manipulation.
# BeautifulSoup library for interpreting the HTML document.
# requests library to communicate with the web page.
# sqlite3 for creating the database instance.

# requests and sqlite3 come bundled with Python3, 
# we need to install pandas and BeautifulSoup libraries to the IDE.

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Initialization
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'

df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# requests.get().text  #  to load the entire web page as an HTML

#Loading the webpage for Webscraping
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser') # to enable extraction of relevant information. 

#Scraping of required information

#loop to extract the appropriate information from the web page. The rows of the table needed can be accessed using the find_all() function with the BeautifulSoup object using the statements below.

tables = data.find_all('tbody') # gets the body of all the tables in the web page
rows = tables[0].find_all('tr') #  gets all the rows of the first table.

#iterate over the rows to find the required data.
for row in rows:
    if count<50:
        col = row.find_all('td') #cell of a table that contains data
        if len(col)!=0:#if the length of col is 0 there is no data in a current row
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break


print(df)
#---------------------
# Storing the data

#save dataframe to a CSV file :
df.to_csv(csv_path)

#To store the required data in a database, we first need to initialize a connection to the database, save the dataframe as a table, and then close the connection. This can be done using the following code:

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

#Note that the CSV and the DB files are also created under the project folder.