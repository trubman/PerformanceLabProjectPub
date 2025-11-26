# https://ru.stackoverflow.com/questions/1341240/%D0%9A%D0%B0%D0%BA-%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%B4-%D0%B4%D0%BB%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8-%D0%BD%D0%B0-python
# https://ru.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
import sys
from collections import namedtuple

argv_list = sys.argv

# проверить количество
def check_quantity(list):
    l = len(list)
    if l < 5:
        print("Недостаточно аргументов. Введите длину массива (n) и интервал движения (m) двух массивов в формате: n1 m1 n2 m2")
        return False
    elif l == 5:
        return True
    else:
        print("Избыточное количество аргументов. Использованы первые четыре в формате: n1 m1 n2 m2")
        return True

check_quantity_result = check_quantity(argv_list)

# проверить тип
def check_type(list):
    check_stat = True
    if check_quantity_result:
        sliced_list = list[1:5]
        for i in sliced_list:
            li = None
            try:
                li = int(i)
                if li <= 0:
                    print(f'{i} - меньше или равно 0')
                    check_stat = False
            except ValueError:
                print(f'{i} - не является целым числом')
                check_stat = False

    if check_stat:
        return True
    else:
        print("Неподходящий тип данных в качестве аргумента. Допустимо: целое положительное число больше 0")
        return False

check_type_result = check_type(argv_list)

names = ['n1', 'm1', 'n2', 'm2']
Data = namedtuple('Data', names)
result = []

def func(n, m, res):
    i = 1
    while True:
        res.append(i)
        # print(i, end='')
        # вдохновлялся примером с применением модульной арифметики на stackoverflow
        i = 1 + (i + m - 2) % n
        if i == 1:
            break

if check_quantity_result and check_type_result:
    count = 0
    for i in argv_list[1:5]:
        setattr(Data, names[count], int(i))
        count += 1

    func(Data.n1, Data.m1, result)
    func(Data.n2, Data.m2, result)

    str_result = ''.join(map(str, result))
    print(str_result)

# python task1\task1.py 6 3 5 4 = 13514253
# python task1\task1.py 4 2 6 4 = 123414