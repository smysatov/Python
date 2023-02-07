# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

list_nums = [1, 2, 3, 4, 5]
k = 4
print(list_nums)
for i in range(k):
    list_nums.insert(0, list_nums.pop(-1))
# result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
print(k, list_nums)
