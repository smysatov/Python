# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше
# заданного максимума)
# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]
from random import choices

mas = choices(range(10), k=10)
print(mas)
min_num = int(input())
max_num = int(input())
for i in range(len(mas)):
    if min_num <= mas[i] <= max_num:
        print(i)
