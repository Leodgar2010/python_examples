# list = [1,4,8,7,5]
# print (list)
# max = list [0]
# for i in list:
#     if i>max:
#         max = i 
# print (max)

list = []
for i in range (5):
    list.append(input ("Введите число: "))
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# d = int(input('Введите четвертое число: '))
# e = int(input('Введите пятое число: '))
# list = [a, b, c, d, e]
print(f'Максимальное число из введенных {max(list)}')
