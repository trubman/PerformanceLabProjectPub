# https://ru.stackoverflow.com/questions/1341240/%D0%9A%D0%B0%D0%BA-%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%B4-%D0%B4%D0%BB%D1%8F-%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8-%D0%BD%D0%B0-python
# https://ru.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic

n1, m1, n2, m2 = map(int, input('Введите длину массива (n) и интервал движения (m) двух массивов в формате: n1 m1 n2 m2 ').split())

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

func(n1, m1, result)
func(n2, m2, result)

str_result = ''.join(map(str, result))

print(str_result)

