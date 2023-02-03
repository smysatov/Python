# Найдите сумму цифр числа.
i = int(input("Enter the number: "))
sum = 0
while (i > 0):
    sum = sum + i % 10
    i = i // 10
print('Сумма цифр: ', sum)
