"""Задание 2.
Описать класс, реализующий десятичный счетчик, который может
увеличивать или уменьшать свое значение на единицу в заданном
диапазоне. Предусмотреть инициализацию счетчика значениями по
умолчанию и произвольными значениями. Счетчик имеет два метода:
увеличения и уменьшения, — и свойство, позволяющее получить его
текущее состояние. Написать программу, демонстрирующую все
возможности класса."""

class Counter:

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def increase(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            return 'Вы вышли за приделы MAX'

    def decrease(self):
        if self.start > self.end:
            self.start -= 1
            return self.start
        else:
            return 'Вы вышли за приделы MAX'

my_count = Counter(start=3, end=5)
print(my_count.increase())
print(my_count.increase())
print(my_count.increase())

new_count = Counter(start=10, end=7)
print(new_count.decrease())
print(new_count.decrease())
print(new_count.decrease())
print(new_count.decrease())
