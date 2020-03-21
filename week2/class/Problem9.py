import datetime
import time
import calendar
tday= datetime.datetime.today()
tdelta1=datetime.timedelta(days =5)
tdelta2=datetime.timedelta(seconds =5)
print(tday)
print("Year",tday.year)
print("Month",tday.month)
print("Weekday",tday.isoweekday())
print(tday-tdelta1)
print(tday-tdelta2)