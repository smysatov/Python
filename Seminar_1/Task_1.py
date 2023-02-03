# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут
# длиной m километров? При решении этой задачи
# нельзя пользоваться условной инструкцией if и циклами.

n = int(input("Enter how many km the car drives in a day \n"))
m = int(input("Enter the distance in km \n"))
print(-(-m // n))
