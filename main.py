import random
from functools import reduce
from itertools import count, cycle


def __create_list__(numbers):
    my_rand_list = []
    for i in range(numbers):
        my_rand_list.append(random.randint(0, 100))
    return my_rand_list


def __task_second__():
    print("********** Task 2 **********")
    source_list = __create_list__(10)
    print(source_list)
    result_list = []
    for i in range(len(source_list)):
        if source_list[i] > source_list[i-1]:
            result_list.append(source_list[i])
    print(result_list)


def __multiple__(a, b):
    return a*b


def __iter_gen__(start_value):
    const_count_cycle = 10
    c = 0
    for el in count(start_value):
        if c < const_count_cycle:
            c += 1
            print(el)
        else:
            break


def __iter_repeat__(my_list):
    c = 0
    for el in cycle(my_list):
        print(el)
        c += 1
        if c > 10: break


def fact(n):
    val = 1
    for i in range(1, n+1):
        val *= i
        yield val


def __task_seven__():
    print("********** Task 7 **********")
    n = 4
    for el in fact(n):
        print(el)


if __name__ == '__main__':

    __task_second__()

    print("********** Task 3 **********")
    print([el for el in range(20, 240) if (el % 20 == 0) or (el % 21 == 0)])

    print("********** Task 4 **********")
    list_number = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    print([el for el in list_number if list_number.count(el) < 2])

    print("********** Task 5 **********")
    gen_list = [el for el in range(100, 1001) if el % 2 == 0]
    print(reduce(__multiple__, gen_list))

    print("********** Task 6 **********")
    __iter_gen__(10)
    __iter_repeat__('Привет')

    __task_seven__()
