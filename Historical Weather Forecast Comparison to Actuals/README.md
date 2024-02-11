# Project(bash): Historical Weather Forecast Comparison to Actuals

## Overview
The objective of this project is to develop an automated Extract, Transform, Load (ETL) process to fetch daily weather forecast and observed weather data. The collected data will be loaded into a live report for analysis by the analytics team. Initially, the focus will be on monitoring the historical accuracy of temperature forecasts for a single station and one source, specifically for Casablanca, Morocco.

## Components of the ETL Process
1. **Extraction:**
   - Utilize the weather data package provided by the open-source project `https://wttr.in/casablanca` to fetch weather data for Casablanca, Morocco.

2. **Transformation:**
   - Extract relevant data from the raw format obtained from wttr.in.
   - Transform the data as required to meet the desired format for analysis.

3. **Load:**
   - Load the transformed data into a live report for further analysis by the analytics team.

## Data Source
The weather data will be obtained from `https://wttr.in/casablanca`, a web service that offers weather forecast information in a simple and text-based format.

## Steps
### 1 - Initialize weather report log file

**1.1 Create a text file**
`rx_poc.log` will be  POC weather report log file ,which contains a growing history of the daily weather data
```bash
touch rx_poc.log
```

**1.2 Add a header to your weather report**
```bash
echo -e "year\tmonth\tday\thour\tobs_temp\tfc_temp">rx_poc.log
```

### 2- Extract and load the required data
**2.1. Create a text file and make it an executable Bash script**
`rx_poc.sh`
an ETL shell script to gather weather data into a report
```bash
touch rx_poc.sh
```

Make  script executable by running the following in the terminal:
```bash
chmod u+x rx_poc.sh
```

### 3- Schedule Bash script `rx_poc.sh` to run every day at noon local time

**3.1 Create a cron job that runs script**

Edit the crontab file:
 `crontab -e`

Add the following line at the end of the file:
 `0 8 * * * /home/project/rx_poc.sh`

Save the file and quit the editor.

### 4- Create a script to report historical forecasting accuracy

create another script to measure and report the accuracy of the forecasted temperatures against the actuals.
create a tab-delimited file named `historical_fc_accuracy.tsv`
```bash
touch historical_fc_accuracy.tsv
```

```bash
echo -e "year\tmonth\tday\tobs_temp\tfc_temp\taccuracy\taccuracy_range" > historical_fc_accuracy.tsv
```

create an executable Bash script called `fc_accuracy.sh`
for handling the accuracy calculations based on just one instance, or day.

### 5- Create a script to report weekly statistics of historical forecasting accuracy

create an executable bash script called `weekly_stats.sh`




