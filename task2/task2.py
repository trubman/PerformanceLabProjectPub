# circle.txt, dot.txt
circle_path = input('Введите наименование файла с координатами эллипса (пример: file.txt) ')
dots_path = input('Введите наименование файла с координатами точек (пример: file.txt) ')

x_center = None
y_center = None
x_rad = None
y_rad = None
dots_list = []

with open(circle_path, "r") as circle_file, open(dots_path, "r") as dots_file:

    for line in circle_file:
        if "coordinate of the ellipse's center" in line:
            x_center = float(line[0])
            y_center = float(line[2])
        elif "coordinate of the ellipse's radius" in line:
            x_rad = float(line[0])
            y_rad = float(line[2])

    counter = 100
    for line in dots_file:
        if counter > 0:
            dots_list.append((float(line[0]), float(line[2])))
            counter -= 1

# print(x_center, y_center)
# print(x_rad, y_rad)
# print(dots_list)

def check_position(dot, center, rad):
    value = ((dot[0] - center[0]) ** 2 / rad[0] ** 2) + ((dot[1] - center[1]) ** 2 / rad[1] ** 2)
    if value < 1:
        return 1 # inside
    elif value == 1:
        return 0 # on
    else:
        return 2 # outside

for dot in dots_list:
    print(check_position(dot, (x_center, y_center), (x_rad, y_rad)))

