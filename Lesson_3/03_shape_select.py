# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
shape_list = ['Треугольник', "Квадрат", "Пятиугольник", "Шестиугольник"]


for x, y in enumerate(shape_list, start=1):
    print(f'{x} : {y}')

_input =-1
while 1 > _input or _input > 4:
    _input = int(input('Возможные фигуры: '))
    if 0 < _input < 5:
        break
    print("Вы ввели некорректный номер фигуры!")

def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point


def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=3)
        point = end_point

start_point = [(250, 220, 150, _input+2)]
for _ in start_point:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    heads_start = _[3]
    polygon(point_start, heads_start, length_start)

sd.pause()
