def create_random_list (list_lenght,number_lenght):
    from random import random
    lst = []
    for i in range(0, list_lenght):
        lst.append(int((round((random()), number_lenght)) * (10**number_lenght)))
    return(lst)
def piramid(array, a, b):
	larg = b
	l = 2 * b + 1
	root = 2 * b + 2

	if l < a and array[b] < array[l]:
		larg = l

	if root < a and array[larg] < array[root]:
		larg = root

	if larg != b:
	    array[b], array[larg] = array[larg], array[b]
	    piramid(array, a, larg)

def Heap(array):
	a = len(array)

	for b in range(a // 2 - 1, -1, -1):
		piramid(array, a, b)

	for b in range(a-1, 0, -1):
		array[b], array[0] = array[0], array[b] # swap
		piramid(array, b, 0)

array = create_random_list(99,2)
print("Исходный список: ", array)
Heap(array)
a = len(array)
print ("Отсортированный список: ", array)
