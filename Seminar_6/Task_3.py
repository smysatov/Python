# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.

# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.

mas = [1, 2, 3, 2, 3, 4, 4, 4, 4]
print(mas)
print(sum([mas.count(i) // 2 for i in set(mas)]))
