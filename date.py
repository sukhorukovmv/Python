#!/usr/bin/python3
#from datetime import date, timedelta
import datetime
year, mounth, day = str(input()).split()
mydate = datetime.date(int(year), int(mounth), int(day))
tdelta = datetime.timedelta(days=int(input()))
newdate = mydate + tdelta
print(newdate.strftime('%Y %m %d').replace(' 0', ' '))
