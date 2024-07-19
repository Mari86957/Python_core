from datetime import datetime

def get_days_from_today():
    date = input("Введіть дату в форматі YYY-MM-DD: ")
    user_date = datetime.strptime(date,  '%Y-%m-%d').date()
    # print(user_date)

    today_date = datetime.today().date()
    # print(today_date)

    delta_days = today_date - user_date
    return(delta_days)