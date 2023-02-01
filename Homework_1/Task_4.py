# Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).
n = int(input('First size: '))
m = int(input('Second size: '))
k = int(input('Number of pcs wanted: '))
if k % n == 0 or k % m == 0:
    print('It is possible to break')
else:
    print('Not possible to break')
