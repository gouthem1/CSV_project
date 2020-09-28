import csv
from datetime import datetime 

open_file = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

highs = []
dates = []
lows =[]



x = datetime.strptime('2018-07-01','%Y-%n-%d')
print(x)



for row in csv_file:
    try:
        high=int(row[4])
        low=int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print('Missing data for {current_date')

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

print(highs)

import matplotlib.pyplot as plt 

fig = plt.figure()

plt.plot(dates,highs,c="red", alpha=0.5)
plt.plot(dates,lows,c="blue", alpha=0.5)

plt.title("Daily High Temp and low temperatures, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.fill_between(datesm highs, lows, facecolor='blue', alpha=0.1)

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both",labelsize=16)

fig.autofmt_xdate()


plt.show()