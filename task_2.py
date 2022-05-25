
def __task_2__():
    print("Task 2")
    list_val = []
    for user_val in range(7):
        user_val = input("Введите любое значение: ")
        list_val.append(user_val)

    for i in range(len(list_val)):
        if (i+1) % 2 == 0:
            list_val[i], list_val[i-1] = list_val[i-1], list_val[i]

    print(list_val)
