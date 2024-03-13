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


    def all_about_travel(self):
        self.time = self.distance / self.speed
        print(f'Цена состовляет: {self.price} руб. за 1 км.;')
        print(f'Средняя скорость: {self.speed} км/ч.;')
        print(f'Время в пути составит: {self.time} ч.;')
        print(f'Стоимость поездки: {self.distance * self.price} руб.')


    def M_M(self):
        print('Путь: Минск - Москва: 700км.')

    def M_W(self):
        print('Путь: Минск - Варшава: 600км.')

    def M_A(self):
        print('Путь: Минск - Астана: 3500км.')

class Plain(Transportation):
    print('Самолёт:')

Pla_1 = Transportation(speed=700, price=0.5, distance=3500)
Pla_1.M_A()
Pla_1.all_about_travel()

Pla_2 = Transportation(speed=700, price=0.5, distance=700)
Pla_2.M_M()
Pla_2.all_about_travel()

class Train(Transportation):
    print('Поезд:')

Tra_1 = Transportation(speed=70, price=0.12, distance=700)
Tra_1.M_M()
Tra_1.all_about_travel()


class Car(Transportation):
    print('Автомобиль:')

Tra_1 = Transportation(speed=120, price=0.2, distance=600)
Tra_1.M_W()
Tra_1.all_about_travel()