#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

max = int(input("Введите максимальное число массива: "))
min = int(input("Введите минимальное число массива: "))
array_1 = [-5, 9, 0, 30, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

for i in range(len(array_1)):
    if min <= array_1[i] <= max:
        print(i)