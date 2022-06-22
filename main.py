from enum import Enum
import time


class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight:
    # public
    def running(self):
        self.__color = Color.RED
        print(self.__color)
        time.sleep(7)
        self.__color = Color.YELLOW
        print(self.__color)
        time.sleep(2)
        self.__color = Color.GREEN
        print(self.__color)
        time.sleep(5)

    def get_color(self):
        return self.__color

    # private
    __color = Color.RED


class Road:
    # public
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self):
        return self.__length * self.__width * self.__weight_per_square * self.__layer_thick

    def set_weight_square(self, m_weight):
        self.__weight_per_square = m_weight

    def set_layer_thick(self, m_layer):
        self.__layer_thick = m_layer

    # protected
    _length = 0
    _width = 0
    # private
    __layer_thick = 5
    __weight_per_square = 25


class Worker:
    # public

    # private
    __name = ""
    __surname = ""
    # protected
    _position = ""
    _income = {"wage": 0, "bonus": 0}

    @property
    def position(self):
        return self._position


class Position(Worker):
    # public
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self._income["wage"] = 0
        self._income["bonus"] = 0

    #       print(self._income)

    def set_position(self, position, wage, bonus):
        self._position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    def get_full_name(self):
        return self.__name + " " + self.__surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


class Direction(Enum):
    FORWARD = 1
    LEFT = 2
    BACK = 3
    RIGHT = 4


class Car:
    def __new__(cls, *args, **kwargs):
        if cls is Car:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls, *args, **kwargs)

    # public
    def go(self, speed):
        print(self._name + " is go!")
        self._speed = speed

    def stop(self):
        print(self._name + " is stop!")
        self._speed = 0

    def turn(self, direction):
        if direction == Direction.FORWARD:
            print(self._name + " is running forward!")
        elif direction == Direction.LEFT:
            print(self._name + " is running left!")
        elif direction == Direction.RIGHT:
            print(self._name + " is running right!")
        elif direction == Direction.BACK:
            print(self._name + " is running back!")

    def show_speed(self):
        print(self._speed)

    def get_info(self):
        print("***** Car info *****")
        print("Name: " + self._name)
        print("Color: " + str(self._color))
        print("Speed: " + str(self._speed))
        print("Is police: " + str(self._is_police))

    # protected
    _speed = 0
    _color = Color.RED
    _name = ""
    _is_police = False
    # private


class TownCar(Car):
    def __init__(self, color=Color.GREEN):
        self._name = "TownCar"
        self._color = color

    def show_speed(self):
        if self._speed > 60:
            print("Speed exceeded")
        print(self._speed)


class SportCar(Car):
    def __init__(self, color=Color.GREEN):
        self._name = "SportCar"
        self._color = color


class WorkCar(Car):
    def __init__(self, color=Color.GREEN):
        self._name = "WorkCar"
        self._color = color

    def show_speed(self):
        if self._speed > 40:
            print("Speed exceeded")
        print(self._speed)


class PoliceCar(Car):
    # public
    def __init__(self, color=Color.RED):
        _color = color
        self._name = "PoliceCar"
        self._is_police = True


class Stationery:
    # public
    @staticmethod
    def draw():
        print("Запуск отрисовки")
    # protected
    _title = ""


class Pen(Stationery):
    # public
    def __init__(self):
        self._title = "Pen"

    def draw(self):
        print("Запуск отрисовки " + self._title)
    # protected


class Pencil(Stationery):
    # public
    def __init__(self):
        self._title = "Pencil"

    def draw(self):
        print("Запуск отрисовки " + self._title)
    # protected


class Handle(Stationery):
    # public
    def __init__(self):
        self._title = "Handle"

    def draw(self):
        print("Запуск отрисовки " + self._title)
    # protected


if __name__ == '__main__':
    print("******* Task 1 *******")
    trafficLight = TrafficLight()
    trafficLight.running()

    print("******* Task 2 *******")
    road = Road(5000, 20)
    print(road.weight())

    print("******* Task 3 *******")
    engineer = Position("Ivan", "Petrov")
    engineer.set_position("engineer", 10000, 5000)
    print("Full name: " + engineer.get_full_name())
    print("Position and income: " + engineer.position + ", " + str(engineer.get_total_income()))

    accountant = Position("Maria", "Fedotova")
    accountant.set_position("accountant", 10000, 5000)
    print("Full name: " + accountant.get_full_name())
    print("Position and income: " + accountant.position + ", " + str(accountant.get_total_income()))

    print("******* Task 4 *******")
    car1 = TownCar()
    car1.go(80)
    car1.get_info()

    car2 = SportCar()
    car2.get_info()

    car3 = WorkCar()
    car3.turn(Direction.LEFT)
    car3.go(100)
    car3.show_speed()
    car3.get_info()
    car3.stop()

    car4 = PoliceCar()
    car4.get_info()

    print("******* Task 5 *******")
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
