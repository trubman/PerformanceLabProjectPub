import json

values_path = 'values.json'
tests_path = 'tests.json'
report_path = 'report.json'

with open(values_path) as values_file, open(tests_path) as tests_file:
    values_json = json.load(values_file)
    report_json = json.load(tests_file)


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

values_list = values_json['values']
for i in values_list:
    # print(i['id'], i['value'])
    flatten_list(report_json['tests'], i)


with open(report_path, 'w') as f:
    json.dump(report_json, f, indent=2, ensure_ascii=False)

