
def __task_4__():
    print("Task 4")
    user_str = input("Введите любую строку, состоящую из нескольких слов: ")
    user_str_list = user_str.split(" ")
    number_str = 1
    for word in user_str_list:
        print(f"{number_str}: {word[:10]}")
        number_str += 1
