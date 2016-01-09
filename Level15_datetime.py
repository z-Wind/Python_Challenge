# http://www.pythonchallenge.com/pc/return/uzi.html
__author__ = 'z-Wind'

import datetime

years = []

for year in range(1996,1216,-20):
    if datetime.date(year, 1, 1).weekday() == 3:
        years.append(year)

print(datetime.date(years[1], 1, 27), 'whom burned?')