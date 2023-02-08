# Требуется найти в массиве A[1..N] самый
# близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5
n = int(input('Количество элементов: '))
x = int(input('Заданное число: '))
array = []
for _ in range(n):
    array.append(int(input()))
print(array)
num = array[0]
count = abs(x - num)
for i in range(1, len(array)):
    if count > abs(array[i] - x):
        count = abs(array[i] - x)
        num = array[i]
print(num)
