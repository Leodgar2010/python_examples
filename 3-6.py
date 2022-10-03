# Дан список чисел. Определите,
# сколько в нем встречается различных чисел
lst = [1,2,2,3,3,4,5,6,6]
result = []
for i in lst:
    if i not in result:
        result.append (i)
print (len(result))


