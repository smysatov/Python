# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# data = open('tel.txt', 'r+')
# data.writelines("Hello world" + "\n")


# print (data.readline())
# data.close ()


fileName = 'tel.txt'


def writeFile(file_name):  # записываем в файл
    with open(file_name, 'a') as data:
        data.write("Sidorov, Petr, Ivanovich, +926474747477" + '\n')


def readFile(file_name):  # читаем из файла
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result


def findUsers(userList):  # ищем в файле
    name = 'Ivan,'
    for user in userList:
        if user[1] == name:
            print(user[3])


def changeUsers(userList):  # вносим изменения в список, либо удаляем

    with open(userList, "rt") as file:
        data = file.read()
        data = data.replace('+7125478541', '+1234567')

    with open(userList, "wt") as file:
        file.write(data)


# writeFile(fileName)
print(type(readFile(fileName)))
print(readFile(fileName))
# findUsers(readFile(fileName))

print(changeUsers(fileName))
