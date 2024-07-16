from datetime import datetime
# def get_days_from_today():
date = input("Введіть дату в форматі:'YYY-MM-DD': ")
day = datetime.strptime(date, '%Y-%m-%d').date()
# print(day)

today_date = datetime.today().date()
# print(today_date)

delta_days = today_date - day
print(delta_days)