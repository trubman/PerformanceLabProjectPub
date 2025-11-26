import os
import sys

argv_list = sys.argv
file_path = None

# проверить количество
def check_quantity(list):
    l = len(list)
    if l == 1:
        print("Введите аргумент с наименованием файла с расширением (пример: file.txt)")
        return False
    elif l == 2:
        return True
    else:
        print("Избыточное количество аргументов. Использован первый из них")
        return True

check_quantity_result = check_quantity(argv_list)

# проверить тип пути
def check_path(list):
    check_stat = True
    global file_path

    def internal_check_path(elem):
        elem_path = None
        inn_check_stat = True
        if os.path.isabs(elem): # если путь абсолютный
            p = os.path.split(elem)
            elem_path = os.path.join(p[0], p[1])
        else:
            if elem.endswith('.txt'): # если указано имя файла
                elem_path = os.path.join(os.path.dirname(__file__), elem)
            else:
                inn_check_stat = False
                print(f'Укажите корректный путь к файлу')
        return elem_path, inn_check_stat

    if check_quantity_result:
        sliced_list = list[1:2]
        file_path, check_stat = internal_check_path(sliced_list[0])

    else:
        check_stat = False

    if check_stat:
        return True
    else:
        return False

check_path_result = check_path(argv_list)

if check_quantity_result and check_path_result:
    try:
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
    except FileNotFoundError:
        print(f'Такого файла не существует: {file_path}')
    except OSError:
        print(f'Укажите корректный путь к файлу')

# python task4\task4.py numbers.txt
# python task4\task4.py numbers2.txt
# python task4\task4.py numbers3.txt
