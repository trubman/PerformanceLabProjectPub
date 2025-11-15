# numbers.txt, numbers2.txt, numbers3.txt
file_path = input('Введите наименование файла с расширением (пример: file.txt) ')

with open(file_path, "r") as file:
    nums = []
    for line in file:
        nums.append(int(line))
    # print(nums)

    # найти медиану (одну из середины?)
    mediana = sorted(nums)[len(nums) // 2]
    # суммировать шаги, где для элемента потребуется abs(элемент - медиана) шагов
    steps = sum(abs(i - mediana) for i in nums)

    if steps < 20:
        print(steps)
    else:
        print('20 ходов недостаточно для приведения всех элементов массива к одному числу')

