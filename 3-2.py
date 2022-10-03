# Дан список чисел. Выведите все элементы
# списка, которые больше предыдущего элемента
lst = [1,3,2,5,4,6]
result = []
for i in range (1,len(lst)):
    if lst [i] > lst [i-1]:
        result.append (lst [i])
print (result)

