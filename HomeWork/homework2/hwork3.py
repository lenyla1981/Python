
#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n=int(input('Введите число n: '))
k=0
res=1
while res<n+1:
    print(res, end=' ')
    k+=1
    res=2**k