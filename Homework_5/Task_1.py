# Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.
def stepen(a, b):
    if b == 0:
        return 1
    if b < 0:
        return stepen(a, b + 1) * 1 / a
    return stepen(a, b - 1) * a


a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
print('a в степени b = ', stepen(a, b))
