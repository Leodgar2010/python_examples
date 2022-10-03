# Задайте строку из набора чисел.
# Напишите программу, которая покажет
# большее и меньшее число. В качестве
# символа-разделителя используйте пробел.

import random

number_len = 10
number = int((round(random.random(), number_len)) * (10 ** number_len))
print(number)
lst = []
for i in range(len(str(number))):
    lst.append(str(number)[i])
print(f"Большее число: {max(lst)} Меньшее число: {min(lst)}")
