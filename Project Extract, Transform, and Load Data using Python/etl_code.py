#Extract, Transform, and Load Data using Python

# Importing Libraries and setting paths
# we will extract data from CSV, JSON, and XML formats. 
#First, we need to import the appropriate Python libraries to use the relevant functions.

#The xml library can be used to parse the information from an .xml file format. 
#The .csv and .json file formats can be read using the pandas library.
#we will use the pandas library to create a data frame format that will store the extracted data from any file.

#To call the correct function for data extraction, we need to access the file format information. For this access, we can use the glob library.

#To log the information correctly, we need the date and time information at the point of logging. For this information, we require the datetime package.

#While glob, xml, and datetime are inbuilt features of Python, we need to install the pandas library to IDE.


import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

# require two file paths that will be available globally in the code for all functions. These are transformed_data.csv, to store the final output data that we can load to a database, and log_file.txt, that stores all the logs.

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

#Task 1 -  Extraction

#To extract from a CSV file using the pandas function read_csv

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

#To extract from a JSON file using the pandas function read_json
# lines=True to enable the function to read the file as a JSON object on line to line

def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe 

#To extract from an XML file
#we need first to parse the data from the file using the ElementTree function.
#we can then extract relevant information from this data and append it to a pandas dataframe as follows.

# we must know the headers of the extracted data to write this function. 
def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe 

# we need a function to identify which function to call on basis of the filetype of the data file.
#use the glob library to identify the filetype. 

def extract(): 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
     
    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 


#Task 2 - Transformation
#The height in the extracted data is in inches, and the weight is in pounds. However, for our application, the height is required to be in meters, and the weight is required to be in kilograms, rounded to two decimal places. Therefore, we need to write the function to perform the unit conversion for the two parameters.

def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data 

#Task 3 - Loading and Logging
#we need to load the transformed data to a CSV file that we can use to load to a database as per requirement.

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 


#Finally, we need to implement the logging operation to record the progress of the different operations. For this operation, we need to record a message, along with its timestamp, in the log_file.


#To record the message, we need to implement a function log_progress() that accepts the log message as the argument.
# The function captures the current date and time using the datetime function from the datetime library. 

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 


#Testing ETL operations and log progress

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 















