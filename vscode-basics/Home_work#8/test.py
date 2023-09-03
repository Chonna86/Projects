from datetime import date, datetime, timedelta
today = date.today()
print(today)
target_date = date(year=2024,month=1,day=1)
print(target_date)
differnce = target_date - today
print(differnce)