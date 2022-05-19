
def __int_to_str_round__(number):
    number = str(number)
    if number.__len__() < 2:
        round_str = f"0{number}"
        return round_str
    return number


def __task_two__():
    print("**********  Task 2  **********")
    isNotCorrectInput = True
    while (isNotCorrectInput):
        time_in_second = input("Введите время в секундах: ")
        try:
            time_in_second = int(time_in_second)
            isNotCorrectInput = False
        except Exception:
            print("Введен не верный формат данных, попробуйте еще раз.")

    hour = time_in_second // 3600
    try:
        minute = (time_in_second % (hour * 3600)) // 60
    except ZeroDivisionError:
        minute = time_in_second // 60

    second = time_in_second - hour * 3600 - minute * 60
    print(f"Ваше время: {__int_to_str_round__(hour)}:{__int_to_str_round__(minute)}:{__int_to_str_round__(second)} ")
