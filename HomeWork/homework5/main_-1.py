#Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью 
#рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 


a = int(input('Введите число a \n'))
b = int(input('Введите числ b \n'))

def f(a, b):
    if b == 0:
      return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b-1)

res = f(a, b)
print(res)

