"""1)	Вам дана строка.
Выведите все подстроки, содержащие "cat"."""

import re

text = 'catcatcat cat catr gggg aaaa Cat catt dsfgert kklll; qwertyuioasdfghjkl zxcvbnm,'

match = re.findall(r"\b[cC]at\b", text)
print(match)


"""2)	Выведите строки, содержащие две буквы "z", между которыми ровно три символа."""

text_2= 'zqwez z123z zzeeezzz qwerrzdfdzqqq'

match_2 = re.findall(r'(z.{3}z)', text_2)
print(match_2)

"""3)	Номер должен быть длиной 10 знаков и начинаться с 8 или 9. 
Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python"""

text_3 = "81122334455, 91122334455, 1234567890, 700000000, 911111111"

match_3 = re.findall(r"[8-9]\d{10}", text_3)
print(match_3)

"""4)	Дана строка, выведите все вхождения слов, начинающиеся на гласную букву."""

text_4 = input("")
match_4 = re.findall(r'\b[aeiouAEIOU]\w*\b', text_4)
print(match_4)


"""5)	Дана строка. Вывести все числа этой строки, как отрицательные так и положительные."""

text_5 = "+1, -3, +2, +3, 11, 22, 124dfs1, eee1-1ee2-+2"

match_5 = re.findall(r"[-]?\d+", text_5)
print(match_5)

"""6)	В каждой строке замените все вхождения подстроки "human" на подстроку "computer" 
и выведите полученные строки."""

text_6 = "Hello human, Hello human"

match_6 = re.sub(r"human", "computer", text_6.rstrip())
print(match_6)

"""7)	Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28)."""

import datetime

match_7 = datetime.datetime.now().strftime('%Y-%m-%d')
print(match_7)

"""8)	Найти все слова, в которых есть хотя бы одна буква ‘b’"""

text_8 = 'oooobooo boooo booo ooooba oooooa kkkka llla aaaaaba aaa'
match_8 = re.findall(r'\b\w*b\w*\b', text_8)
print(match_8)
