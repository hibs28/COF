import datetime

date_now = datetime.datetime.now().astimezone() # Creates a timestamp

print(date_now)

my_date = datetime.date(2024, 12, 31)

print(my_date.strftime("%d-%b-%Y"))         # 31-Dec-2024
print(date_now.strftime("%d-%B-%Y %Z"))     # 26-November-2024 GMT
