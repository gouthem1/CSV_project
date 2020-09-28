import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

highs = []
dates = []
lows = []


x = datetime.strptime('2018-07-01','%Y-%m-%d')
print(x)



for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
print(highs)

import matplotlib.pyplot as plt 

fig = plt.figure()

plt.plot(dates,highs,c="red", alpha=0.5)
plt.plot(dates,lows,c="blue", alpha=0.5)

plt.title("Daily High Temp, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=.1)

fig.autofmt_xdate()

plt.ylabel("temperature (F)", fontsize = 12 )
plt.tick_params(axis="both", labelsize=12)

plt.show()