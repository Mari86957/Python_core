from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date,  '%Y-%m-%d').date()
        today_date = datetime.today().date()
        delta_days = today_date - date
        return delta_days.days
    except ValueError:
        return "Неправильний формат дати. Будь ласка, використовуйте формат 'YYY-MM-DD'."

print(get_days_from_today('2024-07-10'))  
print(get_days_from_today('2024-07-25'))  
print(get_days_from_today('2023-12-31'))
print(get_days_from_today('12.2.2000'))

