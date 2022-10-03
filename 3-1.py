# Дан список. Выведите те его элементы, которые
# встречаются в списке только один раз. Элементы нужно
# выводить в том порядке, в котором они встречаются в списке.

lst = [1, 1, 2, 3, 4, 4]
result = []
count = 0
for i in lst:
    for j in range(len(lst)):
        if lst[j] == i:
            count += 1
    if count <= 1:
        result.append(i)
    count = 0;
print(result)
