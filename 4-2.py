# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# - с помощью математических формул нахождения корней квадратного уравнения
# - с помощью дополнительных библиотек Python
from math import sqrt

a, b, c = 1, 2, 1
# float(input "Введите a: "),float(input "Введите b: "),float(input "Введите c: ")
D = b ** 2 - (4 * a * c)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(round((x1), 3), round((x2), 3))
elif D == 0:
    x = -(b / (2 * a))
    print(round((x), 3))
else:
    print('Вещественных корней нет')
