import main


def __task_three__():
    print("**********  Task 3  **********")
    number = main.__checking_for_number__("Введите число: ")

    result = int(str(f"{number}{number}{number}")) + int(str(f"{number}{number}")) + int(str(f"{number}"))
    print(f"Сумма чисел {number}{number}{number} + {number}{number} + {number} равна {result}")