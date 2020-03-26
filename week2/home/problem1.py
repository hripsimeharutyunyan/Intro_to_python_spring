import datetime
today=datetime.datetime.today()
print("Current date: ", today)
years=input("Given years: ")
days=input("Given days: ")
num_y=datetime.timedelta(days=365*int(years))
num_d=datetime.timedelta(days=int(days))
print("Final date: ",today+num_y+ num_d)
