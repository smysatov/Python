# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

string = input()
string = set(string.lower().split())
print(len(string))
