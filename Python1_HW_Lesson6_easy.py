# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = int(speed)
        self._color = color
        self._name = name
        self._is_police = float(is_police)

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_is_police(self):
        return self._is_police

    def car_go(self):
        print('Машина поехала...')

    def car_stop(self):
        print('Машина остановилась...')

    def car_turn(self, direction):
        print(f'Машина повернула {direction}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

# town_car = TownCar(120, 'Черный', 'Бентли', False)
# town_car.car_stop()
# town_car.car_turn('налево')
# print(town_car.get_color())

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

# Изначально предусмотрел в задаче 1
