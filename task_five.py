import main


def __task_five__():
    print("**********  Task 5  **********")
    income = main.__checking_for_number__("Введите значения выручки: ")
    expenses = main.__checking_for_number__("Введите значения затрат: ")

    if income > expenses:
        print("Фирма работает в прибыль")
        print(f"Рентабельность фирмы составляет: {(income - expenses)*100/income}%")
        count_employee = main.__checking_for_number__("Введите численность сотрудников в фирме: ")
        print(f"На каждого сотрудника фирма заработала: {(income - expenses) / count_employee} у.е.")
    else:
        print("Фирма работает в убыток")
