import csv

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

highs = []
dates = []




x = datetime.strptime('2018-07-01','%Y-%n-%d')
print(x)



for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))

    the_date = datetime.strptime()

print(highs)

import matplotlib.pyplot as plt 

fig = plt.figure()

plt.plot(dates,highs,c="red", alpha=0.5)
plt.plot(dates,lows,c="blue", alpha=0.5)

plt.title("Daily High Temp, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both",labelsize=16)

fig.autofmt_xdate()


plt.show()