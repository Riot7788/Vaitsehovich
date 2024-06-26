""" Задание 4:
 Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
 Каждая копилка имеет ограниченную вместимость, которая
 выражается целым числом – количеством монет(capacity -
 вместимость), которые можно положить в копилку. Класс должен
 поддерживать информацию о количестве монет в копилке,
 предоставлять возможность добавлять монеты в копилку и узнавать,
 можно ли добавить в копилку ещё какое-то количество монет,
 не превышая ее вместимость.
        Класс должен иметь следующий вид:
class MoneyBox:
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку

        При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только
если can_add(self, v) – True."""

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start_money = 0


    def can_add(self, v):
        return self.start_money + v <= self.capacity


    def add(self, v):
        if self.can_add(v):
            self.start_money += v


cointon = MoneyBox(101)
print(cointon.can_add(50))


cointon_2 = MoneyBox(10)
print(cointon_2.can_add(100))