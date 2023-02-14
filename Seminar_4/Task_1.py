# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# a a a b c a a d c d d

# string = input().split()
#
# for i in range(len(string)):
#     count = 1
#     for j in range(i + 1, len(string)):
#         if string[i] == string[j]:
#             string[j] += "_" + str(count)
#             count += 1
# print(*string)

string = input().split()
string_dict = {}.fromkeys(string, 0)
for i in string:
    print(f"{i}_{string_dict[i]}" if string_dict[i] else i, end=" ")
    string_dict[i] += 1
