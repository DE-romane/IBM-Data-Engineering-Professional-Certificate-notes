# Determine the difference between today's forecasted and actual temperatures

#Extract the forecasted and observed temperatures for today and store them in variables
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)

#Calculate the forecast accuracy
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc-$today_temp))
echo "accuracy is $accuracy"


#Assign a label to each forecast based on its accuracy
# +/- 1    deg	excellent
# +/- 2    deg	good
# +/- 3    deg	fair
# +/- 4    deg	poor

if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]
then
   accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]
then
    accuracy_range=good
elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]
then
    accuracy_range=fair
else
    accuracy_range=poor
fi

echo "Forecast accuracy is $accuracy"


# Append a record to your historical forecast accuracy file

row=$(tail -1 rx_poc.log)
year=$( echo $row | cut -d " " -f1)
month=$( echo $row | cut -d " " -f2)
day=$( echo $row | cut -d " " -f3)
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv












