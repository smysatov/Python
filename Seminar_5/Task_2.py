# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 8
# 5 4 2 2 4 2 2 5

def max_to_min(list_1):
    min_list = min(list_1)
    max_list = max(list_1)
    return [min_list if i == max_list else i for i in list_1]


print(*max_to_min([int(i) for i in input().split()]))
