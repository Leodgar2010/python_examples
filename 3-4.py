# Задайте список. Напишите программу, которая
# определит, присутствует ли в заданном
# списке строк некое число
lst_lenght = int(input("Введите длину списка: "))
lst = []
a = False
for i in range(lst_lenght):
    lst.append(input("Введите элемент списка: "))
print(lst)
b = str(input('Введите число: '))
for i in lst:
    if b in i:
        a = True
print (a)
