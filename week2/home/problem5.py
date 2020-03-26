import datetime
import datetime
import time
import calendar
birthday= datetime.datetime(1995,3,21)
print("Birthday: ", birthday)
print("Year: ", birthday.year)
print("Month: ", birthday.month)
print ("Day: ", birthday.day)
print("Week: ", birthday.isoweekday())
birthday2020= datetime.datetime(2020,3,21)
tday= datetime.datetime.today()
print("Days until my next birthday: ", birthday2020-tday)
print(calendar.month(2017,5))
timedelta1= datetime.timedelta(days=1)
timedelta2= datetime.timedelta(days=2)
timedelta3= datetime.timedelta(days=3)
yesterday= tday - timedelta1
print("Yesterday: ", yesterday )
print("Yesterday + 2 days:",yesterday + timedelta2)
print("Yesterday - 3 days:",yesterday - timedelta3)