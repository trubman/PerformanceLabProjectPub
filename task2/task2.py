import os
import sys
import csv
from collections import namedtuple
from fractions import Fraction

argv_list = sys.argv
circle_path = None
dot_path = None

# проверить количество
def check_quantity(list):
    l = len(list)
    if l == 1:
        print("Введите аргументы с наименованием файла с расширением (пример: file.csv)")
        return False
    elif l == 2:
        print("Недостаточное количество аргументов. Укажите пути к файлам circle.csv и dot.csv")
        return False
    elif l == 3:
        return True
    else:
        print("Избыточное количество аргументов. Использованы первые два")
        return True

check_quantity_result = check_quantity(argv_list)

# проверить тип пути
def check_path(list):
    check_stat = True
    global circle_path
    global dot_path

    def internal_check_path(elem, name_path):
        elem_path = None
        inn_check_stat = True
        if os.path.isabs(elem): # если путь абсолютный
            p = os.path.split(elem)
            elem_path = os.path.join(p[0], p[1])
        else:
            if elem.endswith('.csv'): # если указано имя файла
                elem_path = os.path.join(os.path.dirname(__file__), elem)
            else:
                inn_check_stat = False
                print(f'Укажите корректный путь к файлу {name_path}')
        return elem_path, inn_check_stat

    if check_quantity_result:
        sliced_list = list[1:3]
        circle_path, check_stat1 = internal_check_path(sliced_list[0], 'circle.csv')
        dot_path, check_stat2 = internal_check_path(sliced_list[1], 'dot.csv')
        if check_stat1 and check_stat2:
            check_stat = True
        else:
            check_stat = False
    else:
        check_stat = False

    if check_stat:
        return True
    else:
        return False

check_path_result = check_path(argv_list)

circle_names = ['x_center', 'y_center', 'x_rad', 'y_rad']
circle_data = namedtuple('circle_data', circle_names)
dot_data_list = []

if check_quantity_result and check_path_result:
    try:
        with open(circle_path) as circle_file, open(dot_path) as dot_file:
            circle_reader = csv.DictReader(circle_file)
            dot_reader = csv.DictReader(dot_file)
            for row in circle_reader:
                circle_data.x_center = Fraction(row['x_center'])
                circle_data.y_center = Fraction(row['y_center'])
                circle_data.x_rad = Fraction(row['x_rad'])
                circle_data.y_rad = Fraction(row['y_rad'])
            counter = 0
            for row in dot_reader:
                dot_names = ['x', 'y']
                dot_data = namedtuple('dot_data', dot_names)
                dot_data.x = Fraction(row['x'])
                dot_data.y = Fraction(row['y'])
                if counter < 100:
                    dot_data_list.append(dot_data)
                    counter += 1
    except FileNotFoundError:
        print(f'Некоторых файлов не существует: {circle_path}, {dot_path}')
    except OSError:
        print(f'Укажите корректный путь к файлу')


def check_position(dot, center, rad):
    value = ((dot.x - center[0]) ** 2 / rad[0] ** 2) + ((dot.y - center[1]) ** 2 / rad[1] ** 2)
    if value < 1:
        return 1 # inside
    elif value == 1:
        return 0 # on
    else:
        return 2 # outside

for dot in dot_data_list:
    print(check_position(dot, (circle_data.x_center, circle_data.y_center), (circle_data.x_rad, circle_data.y_rad)))

# python task2\task2.py circle.csv dot.csv

