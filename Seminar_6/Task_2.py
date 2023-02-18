# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.

from time import time
from random import choices

# array_1 = list(map(int, input('Введите массив: ').split()))
mas = choices(range(3000), k=2000)
start = time()
# count = 0
# for i in range(1, len(array_1) - 1):
#     if array_1[i] == max(array_1[i - 1: i + 2]):
#         count += 1
# print(count)
print(len([i for i in range(1, len(mas) - 1) if mas[i] > mas[i - 1] and mas[i + 1]]))
print(time() - start)
