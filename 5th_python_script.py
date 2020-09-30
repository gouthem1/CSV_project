import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

highs = []
dates = []
lows = []


for row in csv_file:
    x = datetime.strptime('2018-07-01','%Y-%m-%d')
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)

import matplotlib.pyplot as plt 


fig, ax = plt.subplots(2)

plt.title.ax[0]("SITKA AIRPORT, AK US", fontsize=12)
ax[0].plot(dates,highs,c="red", alpha=0.5)
ax[0].plot(dates,lows,c="blue", alpha=0.5)
ax[0].fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


fig.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize=12)
ax[0].tick_params(axis="both", which= 'major', labelsize=12)

open_file = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

highs = []
dates = []
lows =[]



x = datetime.strptime('2018-07-01','%Y-%m-%d')
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

plt.title("DEATH VALLEY, CA US", fontsize=12)
ax[1].plot(dates,highs,c="red", alpha=0.5)
ax[1].plot(dates,lows,c="blue", alpha=0.5)

ax[1].fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax[1].tick_params(axis="both",labelsize=16)

fig.autofmt_xdate()

plt.show()