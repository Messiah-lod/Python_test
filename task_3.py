def __task_3__():
    print("Task 3")
    list_month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                  "Ноябрь", "Декабрь"]
    dict_month = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль",
                  8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

#    month_number = 0

    while True:
        answer = input("Введите месяц в виде целого числа от 1 до 12: ")
        try:
            month_number = int(answer)
            if 0 < month_number <= 12:
                break
        except Exception:
            print("Введен не верный формат данных, попробуйте еще раз.")

    print(f'Ваш месяц в переменной типа list: {list_month[month_number-1]}')
    print(f'Ваш месяц в переменной типа dict: {dict_month.get(month_number)}')
