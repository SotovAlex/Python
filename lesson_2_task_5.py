def month_to_season():
    month = int(input("Введите номер месяца (от 1 до 12):"))

    if month == 1 or month == 2 or month == 12:
        print("Зима")
    elif month == 3 or month == 4 or month == 5:
        print("Весна")
    elif month == 6 or month == 7 or month == 8:
        print("Лето")
    elif month == 9 or month == 10 or month == 11:
        print("Осень")
    else:
        print("Номер месяца введен не верно")


month_to_season()
