if user_birthday.month == 1:
            birthday_this_year = user_birthday.replace(year=current_year + 1)
        else:
            birthday_this_year = user_birthday.replace(year=current_year)

        if birthday_this_year < today:
            continue