
def __task_four__():
    print("**********  Task 4  **********")
    isNotCorrectInput = True
    while isNotCorrectInput:
        number = input("Введите целое положительное число: ")
        try:
            number = int(number)
            if number <= 0:
                raise Exception("Some exception")
            isNotCorrectInput = False
        except Exception:
            print("Введен не верный формат данных, попробуйте еще раз.")

    str_number = str(number)
    i = 0
    max_number = 0
    while i < str_number.__len__():
        if int(str_number[i]) > max_number:
            max_number = int(str_number[i])
        i += 1

    print(f"Наибольшее число равно {max_number}")
