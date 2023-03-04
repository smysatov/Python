from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data


def show_all():
    if not all_data:
        print('No Data')
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global id
    array = ['Family name', 'Name', 'Surname', 'phone number']
    string = ''
    for i in array:
        string += input(f" Enter {i} ") + " "
    id += 1
    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(f'{id} {string}\n')





def main_menu():
    play = True

    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       '4. Delete a record\n'
                       "5. Exit\n")

        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                pass
                # search_record()
            case '4':
                pass
                # delete_record()
            case "5":
                play = False
            case _:
                print("Try again!\n")


main_menu()
