# Определите среднее значение всех элементов
# последовательности,
# авершающейся числом 0.
from statistics import mean

a = 1;
lst = []
while (a != 0):
    a = int(input("Введите число: "))
    lst.append(a)
print(mean(lst))
