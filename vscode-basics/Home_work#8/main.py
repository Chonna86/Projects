from datetime import date, datetime, timedelta



def get_birthdays_per_week(users):
    # Отримуємо поточний день тижня та поточну дату
    today = date.today()
    current_weekday = today.weekday()  # 0 - понеділок, 1 - вівторок, ..., 6 - неділя
    current_year = today.year

    # Створюємо словник для збереження днів народження наступного тижня
    birthdays_next_week = {}
    for i in range(7):
        next_weekday = (current_weekday + i) % 7
        next_week = today + timedelta(days=(7 - current_weekday + i))
        next_weekday_name = next_week.strftime('%A')  # Назва дня тижня
        birthdays_next_week[next_weekday_name] = []

    # Додаємо користувачів до відповідних днів народження
    for user in users:
        user_name = user['name']
        user_birthday = user['birthday']


        # Перевіряємо, чи день народження вже минув у цьому році
        if user_birthday.month == 1:
            birthday_this_year = user_birthday.replace(year=current_year + 1)
        else:
            birthday_this_year = user_birthday.replace(year=current_year)

        if birthday_this_year < today:
            continue
        days_until_birthday = (user_birthday - today).days
        next_weekday_name = (today + timedelta(days=days_until_birthday)).strftime('%A')
    
        # Переносимо вихідні на понеділок, якщо потрібно
        if next_weekday_name == 'Saturday':
            next_weekday_name = 'Monday'
        elif next_weekday_name == 'Sunday':
            next_weekday_name = 'Monday'

        # Додаємо користувача до відповідного дня народження
        birthdays_next_week[next_weekday_name].append(user_name)

    # Переносячи вихідні на понеділок
    if current_weekday == 5:  # Субота
        birthdays_next_week['Monday'] += birthdays_next_week['Saturday']
        birthdays_next_week['Saturday'] = []
    elif current_weekday == 6:  # Неділя
        birthdays_next_week['Monday'] += birthdays_next_week['Sunday']
        birthdays_next_week['Sunday'] = []

    # Видаляємо пусті значення
    birthdays_next_week = {k: v for k, v in birthdays_next_week.items() if v}

    return birthdays_next_week

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
