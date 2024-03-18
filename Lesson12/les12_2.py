""" Задание 2
Создать базовый класс «Грузоперевозчик» и производные классы «Самолет»,
«Поезд», «Автомобиль». Определить время и стоимость перевозки для указанных
городов и расстояний"""

class Transportation:
    def __init__(self, time=float, price=float, distance=int, speed=int):
        self.time = time
        self.price = price
        self.distance = distance
        self.speed = speed


class Moscow(Transportation):
    def Moscow_Minsk(self):
        self.distance = 800
        self.time = self.distance / self.speed
        print('Маршрут: Москва - Минск. Расстояние: 800 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Moscow_Warsaw(self):
        self.distance = 1300
        self.time = self.distance / self.speed
        print('Маршрут: Москва - Варшава. Расстояние: 1300 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Moscow_St_Petersburg(self):
        self.distance = 700
        self.time = self.distance / self.speed
        print('Маршрут: Москва - Санкт-Петербург. Расстояние: 700 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Moscow_New_York(self):
        self.distance = 7500
        self.time = self.distance / self.speed
        print('Маршрут: Москва - New York City. Расстояние: 7500 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Moscow_Dubai(self):
        self.distance = 5300
        self.time = self.distance / self.speed
        print('Маршрут: Москва - Dubai. Расстояние: 7500 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')


class Minsk(Transportation):
    def Minsk_Moscow(self):
        self.distance = 700
        self.time = self.distance / self.speed
        print('Маршрут: Минск - Москва. Расстояние: 700 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Minsk_Warsaw(self):
        self.distance = 600
        self.time = self.distance / self.speed
        print('Маршрут: Минск - Варшава. Расстояние: 600 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Minsk_Petersburg(self):
        self.distance = 800
        self.time = self.distance / self.speed
        print('Маршрут: Минск - Санкт-Петербург. Расстояние: 800 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')


class Warsaw(Transportation):
    def Warsaw_Petersburg(self):
        self.distance = 1200
        self.time = self.distance / self.speed
        print('Маршрут: Варшава - Санкт-Петербург. Расстояние: 1200 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Warsaw_Minsk(self):
        self.distance = 600
        self.time = self.distance / self.speed
        print('Маршрут: Варшава - Минск. Расстояние: 600 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')

    def Warsaw_Moscow(self):
        self.distance = 1300
        self.time = self.distance / self.speed
        print('Маршрут: Варшава - Москва. Расстояние: 1300 км.')
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Примерное время в пути: {round(self.time)} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')


class Plain(Transportation):
    print('Самолёт:')

Pla_1 = Moscow(speed=700, price=0.5)
Pla_1.Moscow_New_York()

Pla_2 = Moscow(speed=700, price=0.5)
Pla_2.Moscow_Dubai()


class Train(Transportation):
    print('Поезд:')

Tra_1 = Minsk(speed=70, price=0.12)
Tra_1.Minsk_Petersburg()

Tra_2 = Minsk(speed=70, price=0.12)
Tra_2.Minsk_Warsaw()


class Car(Transportation):
    print('Автомобиль:')

Tra_1 = Warsaw(speed=120, price=0.2)
Tra_1.Warsaw_Petersburg()

Tra_2 = Warsaw(speed=120, price=0.2)
Tra_2.Warsaw_Moscow()
coo