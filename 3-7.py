# Даны два списка чисел. Найдите все
# числа, которые входят как в первый,
# так и во второй список и выведите
# их в порядке возрастания.
lst = [2,6,3,1,7]
lst2 = [5,7,1,2,4]
result = []
for i in lst:
    for j in lst2:
        if i == j:
            if i not in result:
                result.append (i)
result.sort ()
print (result)

