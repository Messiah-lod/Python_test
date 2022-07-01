from abc import ABC, abstractmethod


class Matrix:
    # public
    def __init__(self, lst):
        try:
            self.__m_list = list(lst)
        except:
            raise Exception("Not a LIST has been passed to the constructor")
        if isinstance(lst, str):
            raise Exception("Not a LIST has been passed to the constructor")

    def __str__(self):
        result_str = ""
        for el in self.__m_list:
            m_str = " ".join([str(e) for e in el])
            result_str += (m_str + "\n")
        return result_str

    def __add__(self, other):
        if len(self.__m_list) != len(other.__m_list):
            raise Exception("The matrices have different sizes")
        for i in range(len(self.__m_list)):
            if len(self.__m_list[i]) != len(other.__m_list[i]):
                raise Exception("The matrices have different sizes")
        result_lst = []
        for i in range(len(self.__m_list)):
            element_list = []
            for j in range(len(self.__m_list[i])):
                element_list.append(self.__m_list[i][j] + other.__m_list[i][j])
            result_lst.append(element_list)

        return result_lst

    # private
    __m_list = []


class Clothes(ABC):
    # protected
    _name = ""

    # public
    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Clothes):
    # public
    def __init__(self, size):
        self._name = "Coat"
        self.__V = size

    @property
    def sum_cloth(self):
        return self.__V/6.5 + 0.5

    # private
    __V = 0

    @property
    def name(self):
        return self._name


class Suit(Clothes):
    # public
    def __init__(self, height):
        self._name = "Suit"
        self.__H = height

    @property
    def sum_cloth(self):
        return 2*self.__H + 0.3

    # private
    __H = 0


class Cell:
    # public
    def __init__(self, count_cells):
        self.__m_count_cells = count_cells

    def __add__(self, other):
        return self.__m_count_cells + other.__m_count_cells

    def __sub__(self, other):
        result = self.__m_count_cells - other.__m_count_cells
        if result <= 0:
            raise Exception("The difference is less than zero")
        return result

    def __mul__(self, other):
        return self.__m_count_cells * other.__m_count_cells

    def __truediv__(self, other):
        return round(self.__m_count_cells / other.__m_count_cells)

    def make_order(self, count_row):
        result_str = ""
        for i in range(self.__m_count_cells):
            if i != 0 and i % count_row == 0:
                result_str += "\n"
            result_str += "*"
        return result_str

    # private
    __m_count_cells = 0


if __name__ == '__main__':
    print("******* Task 1 ********")
    mx1 = Matrix([[1, 4, 5], [7, 3, 1], [5, 22, 0]])
    mx2 = Matrix([[11, 2, -5], [43, 1, 17], [22, 2, -88]])
    mx_res = Matrix(mx1 + mx2)
    print(mx_res)

    print("******* Task 2 ********")
    coat = Coat(5)
    suit = Suit(7)
    print("Объем необходимой ткани: " + str(coat.sum_cloth + suit.sum_cloth))

    print("******* Task 3 ********")
    my_cell1 = Cell(14)
    my_cell2 = Cell(7)
    print(Cell(my_cell1 + my_cell2).make_order(4))
    print("------------------")
    print(Cell(my_cell1 - my_cell2).make_order(5))
    print("------------------")
    print(Cell(my_cell1 * my_cell2).make_order(10))
    print("------------------")
    print(Cell(my_cell1 / my_cell2).make_order(3))

