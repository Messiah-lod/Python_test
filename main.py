def __task_1__():
    print("******  Task 1  ******")

    def __division__(m_divisible, m_divisor):
        if m_divisor == 0:
            raise Exception("Division by zero")
        else:
            return m_divisible / m_divisor

    try:
        divisible = int(input("Введите делимое: "))
    except Exception:
        print("Делимое не является числом и было принято равным нулем")
        divisible = 0

    try:
        divisor = int(input("Введите делитель : "))
    except Exception:
        print("Делитель не является числом и было принято равным нулем")
        divisor = 0

    try:
        result = __division__(divisible, divisor)
    except Exception:
        result = 0

    return result


def __task_2__(name, surname, year, city, email, number):
    print("******  Task 2  ******")

    result = lambda m_name, m_surname, m_year, m_city, m_email, m_number: \
        f"Имя пользователя: {m_name}, фамилия пользователя: {m_surname}, родился в {m_year} году, в городе {m_city}. " \
        f"Для связи с {m_name} возможно использовать следующие варианты: e-mail: {m_email} или тел.: {m_number}"

    return result(m_name=name, m_year=year, m_surname=surname, m_city=city, m_number=number, m_email=email)


def __task_3__():
    print("******  Task 3  ******")

    def __my_func__(m_first, m_second, m_third):
        tmp_list = [m_first, m_second, m_third]
        max1 = max(tmp_list)
        tmp_list.remove(max1)
        max2 = max(tmp_list)
        return max1 + max2

    return f"Сумма максимальных чисел равна: {__my_func__(0, 4, -38)}"


def __task_4__(m_first, m_second):
    print("******  Task 4  ******")
    m_first = float(m_first)
    if m_first <= 0:
        return 'Введен не верный формат первого числа'
    m_second = int(m_second)
    if m_second >= 0:
        return 'Введен не верный формат второго числа'

    def __my_func__(x, y):
        print(f"Реализация возведения в степень первым методом через оператор **: {float(x**y)} ")
        y = abs(y)
        result = 1
        for i in range(y):
            result *= x
        result = 1/result
        print(f"Реализация возведения в степень вторым методом через цикл: {result} ")
        return

    __my_func__(m_first, m_second)
    return


def __task_5__():
    print("******  Task 5  ******")
    print("Для остановки суммирования введите символ S")
    print("Введите несколько чисел через пробел: ")
    const_stop_symbol = "s"
    user_input = ""
    is_break = False
    result = 0
    while const_stop_symbol != user_input:
        str_number = input()
        list_number = str_number.split()
        for sym in list_number:
            if sym == const_stop_symbol:
                is_break = True
                break
            try:
                number = int(sym)
            except Exception:
                print(f"Пользовательский ввод '{sym}' не является числом и был приравнен к нулю")
                number = 0
            result += number
        print(f"Сумма всех введенных числе до спец символа равна: {result}")
        if is_break:
            break

    return


def __int_func__(m_str):
    return m_str.capitalize()


def __task_6__(m_str):
    print("******  Task 6  ******")
    result = __int_func__(m_str)
    return result


def __task_7__():
    print("******  Task 7  ******")
    user_str = input("Введите строку: ")
    list_word = user_str.split()
    result_str = ""
    for word in list_word:
        word = __int_func__(word)
        result_str = " ".join([result_str, word])
    print(result_str)
    return


if __name__ == '__main__':
    print(__task_1__())
    print(__task_2__("Иван", "Петров", "1571", "Ватикан", "IP@vatican.com", "65-645-658-98-96"))
    print(__task_3__())
    __task_4__(5.8, -9)
    __task_5__()
    print(__task_6__("text"))
    __task_7__()
