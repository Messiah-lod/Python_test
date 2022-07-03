import datetime


class Data:
    # public
    def __init__(self, str_data):
        if not isinstance(str_data, str):
            raise Exception("The passed parameter is not a string")
        self._m_str_data = str_data

    @classmethod
    def convert_data(cls, str_data):
        lst_str = str_data.split("-")
        return [int(x) for x in lst_str]

    @staticmethod
    def is_valid_data(str_data):
        lst_int_data = Data.convert_data(str_data)
        if len(lst_int_data) != 3:
            return False
        print(lst_int_data)
        if lst_int_data[0] < 1 or lst_int_data[0] > 31 or \
                lst_int_data[1] < 1 or lst_int_data[1] > 12 or \
                lst_int_data[2] < 1:
            return False
        return True

    # private
    _m_str_data = ""


class Division(Exception):

    def __init__(self, first, second):
        try:
            self.__m_first = int(first)
            self.__m_second = int(second)
        except ValueError:
            print("Вы ввели не число")

    def div_except(self):
        result = 0
        try:
            result = self.__m_first / self.__m_second
        except ZeroDivisionError:
            print("Деление на ноль")
        return result

    # private
    __m_first = 0
    __m_second = 0


class ValidNumber:
    @staticmethod
    def is_valid_number(number):
        is_valid = True
        try:
            number = int(number)
        except:
            try:
                number = float(number)
            except:
                print("ведено не число")
                is_valid = False
        return is_valid


class Warehouse:
    def add_object(self, obj, count=1, dep="main"):
        if isinstance(count, str):
            print("input error value")
            return
        for i in range(count):
            self.__object_warehouse[self.__id] = [obj, dep]
            self.__id += 1

    def get_object(self):
        return self.__object_warehouse.items()

    def move_departament(self, name_warehouse, dep):
        for item in self.__object_warehouse.items():
            if item[1][0]._name == name_warehouse:
                self.__object_warehouse[item[0]] = [self.__object_warehouse[item[0]][0], dep]

    __object_warehouse = {}
    __id = 1


class Equipment:
    _weight = 0
    _width = 0
    _length = 0
    _name = ""

    def __str__(self):
        return f"Оборудование: {self._name}, вес: {self._weight}, ширина: {self._width}, длина: {self._length}"


class Printer(Equipment):
    def __init__(self, name):
        self._name = name
        self._weight = 10
        self._width = 10
        self._length = 10
        self._format_list = "A3"

    _format_list = ""


class Scanner(Equipment):
    def __init__(self, name):
        self._name = name
        self._weight = 20
        self._width = 20
        self._length = 20
        self._type_scan = "Планшетный"

    _type_scan = ""


class Xerox(Equipment):
    def __init__(self, name):
        self._name = name
        self._weight = 30
        self._width = 30
        self._length = 30
        self._speed_xerox = 80

    _speed_xerox = 0


class ComplexNumber:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __add__(self, other):
        return self.__a + other.__a, self.__b + other.__b

    def __mul__(self, other):
        a = self.__a * other.__a - self.__b * other.__b
        b = self.__a * other.__b + self.__b * other.__a
        return a, b

    def __str__(self):
        return f"{self.__a}+{self.__b}j"

    __a = 0
    __b = 0


if __name__ == '__main__':
    print("*********** Task 1 ***********")
    print(Data.convert_data("05-04-2020"))
    print(Data.is_valid_data("05-04-2020"))
    print(Data.is_valid_data("38-13-2020"))

    print("*********** Task 2 ***********")
    m_div = Division(8, 0)
    print(m_div.div_except())

    print("*********** Task 3 ***********")
    user_input_lst = []
    user_input = " "
    while user_input:
        user_input = input("Введите число, которое будет сохранено в список: ")
        if ValidNumber.is_valid_number(user_input):
            user_input_lst.append(user_input)
    print(user_input_lst)

    print("*********** Task 4 - 6 ***********")
    warehouse = Warehouse()
    warehouse.add_object(Printer("набор принтеров"), 5)
    warehouse.add_object(Scanner("секретарю"))
    warehouse.add_object(Xerox("удаленный работник"), dep="home")
    for el in warehouse.get_object():
        print(el)
    warehouse.move_departament("секретарю", "office5")
    print("***********")
    for el in warehouse.get_object():
        print(el)

    print("*********** Task 7 ***********")
    one = ComplexNumber(10, 5)
    two = ComplexNumber(1, -5)
    print(one + two)
    print(one * two)
