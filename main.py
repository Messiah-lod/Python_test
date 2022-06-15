import random
import pprint
import json


def __task_1__():
    print("******** task 1 ********")
    print("Введите данные. Все данные будут сохранены в файл task_1.txt. Для завершения ввода введите пустую строку.")
    while True:
        user_input = input()
        with open("task_1.txt", mode='a', encoding='utf-8') as f_obj:
            f_obj.write(user_input + "\n")
        if user_input == "":
            break


def __task_2__():
    print("******** task 2 ********")
    count_line = 0
    with open("task_2.txt", mode='r', encoding='utf-8') as f_obj:
        list_of_file = f_obj.readlines()

    for line in list_of_file:
        count_line += 1
        list_word = line.split()
        print(f"В {count_line} строке {len(list_word)} слов(а)")

    print(f"В файле {len(list_of_file)} строк")


def __task_3__():
    print("******** task 3 ********")
    with open("task_3.txt", mode='r', encoding='utf-8') as f_obj:
        list_of_file = f_obj.readlines()
    sum_bonus = 0
    for line in list_of_file:
        list_word = line.split()

        try:
            salary = float(list_word[1])
        except:
            salary = 0
        else:
            sum_bonus += salary

        if salary < 20000:
            print(f"{list_word[0]} имеет оклад меньше 20 000")

    print("Средняя величина доходов сотрудников равна:", sum_bonus / len(list_of_file))


def __task_4__():
    print("******** task 4 ********")
    with open("task_4_in.txt", mode='r', encoding='utf-8') as f_obj:
        list_of_file = f_obj.readlines()

    dict_language = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'
    }

    for line in list_of_file:
        list_word = line.split()
        list_word[0] = dict_language[list_word[0]]
        line = " ".join(list_word)
        print(line)
        with open("task_4_out.txt", mode='a', encoding='utf-8') as f_obj:
            f_obj.write(line + "\n")


def __task_5__():
    print("******** task 5 ********")
    with open("task_5.txt", mode='w', encoding='utf-8') as f_obj:
        list_number = [str(random.randint(0, 100)) for el in range(20)]
        f_obj.write(" ".join(list_number))

    with open("task_5.txt", mode='r', encoding='utf-8') as f_obj:
        data_of_file = f_obj.readline()
        list_data = data_of_file.split()
        result = 0
        for number in list_data:
            try:
                number = int(number)
            except:
                number = 0
            finally:
                result += number

    print("Сумма чисел из файла:" + str(result))


def __task_6__():
    print("******** task 6 ********")
    with open("task_6.txt", mode='r', encoding='utf-8') as f_obj:
        data_of_file = f_obj.readlines()
    #    print(data_of_file)
    result_dict = {}
    for line in data_of_file:
        line = line.split()
        count = 0  # счетчик номера записи
        key_word = ""  # ключ для словаря
        sum_classes = 0  # сумма занятий

        for word in line:
            str_num_classes = ""  # число часов занятия

            for symbol in word:
                if count == 0 and symbol.isalpha():
                    key_word += symbol
                elif symbol.isdigit():
                    str_num_classes += symbol

            count += 1

            try:
                digit_num_classes = int(str_num_classes)
            except:
                digit_num_classes = 0

            sum_classes += digit_num_classes

        result_dict[key_word] = sum_classes
    print(result_dict)


def __task_7__():
    print("******** task 7 ********")
    with open("task_7.txt", mode='r', encoding='utf-8') as f_obj:
        data_of_file = f_obj.readlines()

    medium_profit = 0
    count_organization = 0
    dict_firm = {}

    for line in data_of_file:
        line = line.split()
        name_organization = ""
        profit = int(line[-2]) - int(line[-1])  # прибыль

        if profit > 0:
            medium_profit += profit
            count_organization += 1
        is_start_name = True

        for i in range(len(line)):
            if is_start_name:
                name_organization += (" " + line[i])
            if line[i].count('"') == 2 or line[i].find('"') == len(line[i]) - 1:
                is_start_name = False

        dict_firm[name_organization.lstrip()] = profit

    result_list = [dict_firm, {'average_profit': medium_profit/count_organization}]
    pprint.pprint(result_list)

    with open("task_7.json", mode='w', encoding='utf-8') as f_obj:
        json.dump(result_list, f_obj, ensure_ascii=False)


if __name__ == '__main__':
    __task_1__()
    __task_2__()
    __task_3__()
    __task_4__()
    __task_5__()
    __task_6__()
    __task_7__()
