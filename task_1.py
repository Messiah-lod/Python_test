
def __print_var_typeVar__(name):
    print(f'Значение переменной: {name}, тип переменной: {type(name)}')


def __task_1__():
    print("Task 1")
    list_value = ["Hello!", 'R', 1.5, 9, 0, True, {"key": "val"}, {"first", "second"}, (1,2,3), ["a", "b", "c"], complex(5, 6), None]
    for item in list_value:
        __print_var_typeVar__(item)
