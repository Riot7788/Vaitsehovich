""" Задание 1:  Создать класс с двумя переменными.
                Добавить функцию вывода на экран и функцию изменения этих переменных.
                Добавить функцию, которая находит сумму значений этих переменных,
                и функцию которая находит наибольшее значение из этих двух переменных"""
class TestWitchTwo:

    def __init__(self,
                 var_num_one=1,
                 var_num_second=1
                 ) -> None:
        self.var_num_one = var_num_one
        self.var_num_second = var_num_second


    def display_info(self) -> None:
        print(f'Первая переменная: {self.var_num_one} \n'
              f'Вторая переменная: {self.var_num_second} ')


    def summa(self):
        print(f'Cумма переменных: {self.var_num_one + self.var_num_second}')



    def what_more(self):
        if self.var_num_one > self.var_num_second:
            print(f'Первая переменная значение:({self.var_num_one}) больше второй')
        else:
            print(f'Вторая переменная значение:({self.var_num_second}) больше первой')


T1 = TestWitchTwo(4,10)
T1.display_info()
T1.summa()
T1.what_more()