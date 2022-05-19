
def __print_var_typeVar__(name):
    print(f'Значение переменной: {name}, тип переменной: {type(name)}')


def __task_one__():
    print("**********  Task 1  **********")
    __print_var_typeVar__("Hello!")  # строка
    __print_var_typeVar__("C")  # и это тоже будет строка, в python нет типа char
    __print_var_typeVar__(5)
    __print_var_typeVar__(1.6)
    __print_var_typeVar__(True)

    for i in range(5):
        user_input = input(f"Введите данные {i + 1} из 5: ")

        try:
            user_input = int(user_input)
        except Exception:
            try:
                user_input = float(user_input)
            except Exception:
                user_input = str(user_input)

        print("Вы вели следующие данные: ")
        __print_var_typeVar__(user_input)
