from sys import argv


def __str_to_int__(str_param):
    try:
        integer = int(str_param)
        return integer
    except:
        return 0


def wages():
    print("********** Task 1 **********")
    if len(argv) > 3:
        path, working, rate, bonus = argv
        working = __str_to_int__(working)
        rate = __str_to_int__(rate)
        bonus = __str_to_int__(bonus)
        print(f"Ваша заработная плата будет: {working*rate+bonus}")
    else:
        print("Введено недосточное кол-во параметров: выработка в часах, ставка в час, премия")


if __name__ == '__main__':
    wages()
