import os
import sys
import json

argv_list = sys.argv
values_path = os.path.join(os.path.dirname(__file__), 'values.json')
tests_path = os.path.join(os.path.dirname(__file__), 'tests.json')
report_path = os.path.join(os.path.dirname(__file__), 'report.json')

# проверить количество
def check_quantity(list):
    l = len(list)
    if l == 1:
        print("Использованы пути по умолчанию (values.json, tests.json)")
        return False
    elif l == 2:
        print("Недостаточное количество аргументов. Укажите пути к файлам values.json и tests.json")
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
    global tests_path
    global values_path

    def internal_check_path(elem, name_path):
        elem_path = None
        inn_check_stat = True
        if os.path.isabs(elem): # если путь абсолютный
            p = os.path.split(elem)
            elem_path = os.path.join(p[0], p[1])
        else:
            if elem.endswith('.json'): # если указано имя файла
                elem_path = os.path.join(os.path.dirname(__file__), elem)
            else:
                inn_check_stat = False
                print(f'Укажите корректный путь к файлу {name_path}')
        return elem_path, inn_check_stat

    if check_quantity_result:
        sliced_list = list[1:3]
        values_path, check_stat1 = internal_check_path(sliced_list[0], 'values.json')
        tests_path, check_stat2 = internal_check_path(sliced_list[1], 'tests.json')
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

def flatten_list(my_list, item):

    def change_value(elem, item):
        if elem['id'] == item['id']:
            elem['value'] = item['value']
            # print(item['id'], '====')

    def inner_flatten_list(elem, item):
        try:
            if elem['values']:
                # print('00000 ', elem['values'])
                flatten_list(elem['values'], item)
            change_value(elem, item)
        except KeyError:
            change_value(elem, item)

    for l in my_list:
        inner_flatten_list(l, item)

if check_quantity_result and check_path_result:
    try:
        with open(values_path) as values_file, open(tests_path) as tests_file:
            values_json = json.load(values_file)
            report_json = json.load(tests_file)

            values_list = values_json['values']
            for i in values_list:
                # print(i['id'], i['value'])
                flatten_list(report_json['tests'], i)

        with open(report_path, 'w') as f:
            print('Сохранен report.json')
            json.dump(report_json, f, indent=2, ensure_ascii=False)

    except FileNotFoundError:
        print(f'Некоторых файлов не существует: {values_path}, {tests_path}')
    except OSError:
        print(f'Укажите корректный путь к файлу')

# python task3\task3.py
# python task3\task3.py values.json tests.json
# python task3\task3.py D:\_MyPython\PerformanceLabProject\task3\values.json D:\_MyPython\PerformanceLabProject\task3\report.json
