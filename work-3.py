# # Дан список. Выведите те его элементы, которые встречаются в списке
# # только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# lst = [int (i) for i in ((input ("Введите значения через пробел "))).split()]
# print (lst)
# lst2 = []
# count = 0
# for i in lst:
#     for j in lst:
#         if i == j:
#             count += 1
#     if count == 1:
#         lst2.append(i)
#     count = 0
# print(lst2)
import time

# Дан список чисел.
# Выведите все элементы списка, которые больше предыдущего элемента.
# lst = [1, 2, 5, 6, 7, 2, 3, 4, 6]
# for i in range(1, len(lst)):
#     if lst[i] > lst[i - 1]:
#         print(lst[i], end=" ")
# Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора псевдослучайных чисел.
# from datetime import *
#
#
# def k():
#     return(datetime.now().microsecond)
# a=int(input("Введите размерность: "))
# res = int(k()/10**(6-a))
# print (res)
# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# lst = ['Строка1', 'Строка2', 'Строка12']
# a = str(2)
# k = False
# for i in lst:
# # if a in i:
# #     k = True
#     if i.find (a) > -1:
#         k = True
# print (k)
# Напишите программу, которая определит
# позицию второго вхождения строки
# в списке либо сообщит, что её нет.
lst = ['Строка1', 'Строка2', 'Строка12', 'Строка2', 'Строка2']
a = 'Строка6'
count = 0
for i in range(len(lst)):
    if a == lst[i]:
        count += 1
    if count == 2:
        print(i)
if count == 0:
    print("Строки нет")
# Дан список чисел. Определите,
# сколько в нем встречается различных чисел
# lst = [1,2,2,3,3,4,5,6,6]
# result = []
# for i in lst:
#     if i not in result:
#         result.append (i)
# print (len(result))
# Даны два списка чисел. Найдите все
# числа, которые входят как в первый,
# так и во второй список и выведите
# их в порядке возрастания.
# lst = [2,6,3,1,7]
# lst2 = [5,7,1,2]
# result = []
# for i in lst:
#     for j in lst2:
#         if i == j:
#             if i not in result:
#                 result.append (i)
# result.sort ()
# print (result)
# Вам дан английский текст. Закодируйте
# его с помощью азбуки Морзе:
# MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#           'D': '-..', 'E': '.', 'F': '..-.',
#           'G': '--.', 'H': '....', 'I': '..',
#           'J': '.---', 'K': '-.-', 'L': '.-..',
#           'M': '--', 'N': '-.', 'O': '---',
#           'P': '.--.', 'Q': '--.-', 'R': '.-.',
#           'S': '...', 'T': '-', 'U': '..-',
#           'V': '...-', 'W': '.--', 'X': '-..-',
#           'Y': '-.--', 'Z': '--..'}
# text = "YOU CANNOT PASS"
# for i in text:
#    if i == " ":
#        print (end = '')
#    else:
#        print (MORSE [i], end = '')
# Для каждого слова исходного текста выведите
# одно целое число — номер вхождения этого слова в текст.
# Числа выведите через пробел. Количество чисел должно
# совпадать с количеством слов в исходном тексте.
# text = 'раз раз раз как меня слышно Повторяю раз раз раз Повторяю'
# 1 2 3 1 1 1 1 4 5 6 2
# a = {}
# b = text.split()
# for i in b:
#     if i in a:
#         a[i] += 1
#     else:
#         a[i] = 1
#     print(a[i], end=" ")


