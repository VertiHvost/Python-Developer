# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# x= int(input('Введите координаты начальной точки отрисовки x:'))
# y= int(input('Введите координаты начальной точки отрисовки y:'))


def draw_3_corner(start_point, angle_of_inclination, side_length, color_w):
    line_1 = sd.get_vector(start_point=start_point, angle=angle_of_inclination, length=side_length, width=3)
    line_1.draw(color=color_w)

    line_2 = sd.get_vector(start_point=line_1.end_point, angle=120, length=side_length, width=3)
    line_2.draw(color=color_w)

    line_3 = sd.get_vector(start_point=line_2.end_point, angle=240, length=side_length, width=3)
    line_3.draw(color=color_w)


def draw_4_corner(start_point, angle_of_inclination, side_length, color_w):
    line_1 = sd.get_vector(start_point=start_point, angle=angle_of_inclination, length=side_length, width=3)
    line_1.draw(color=color_w)

    line_2 = sd.get_vector(start_point=line_1.end_point, angle=90, length=side_length, width=3)
    line_2.draw(color=color_w)

    line_3 = sd.get_vector(start_point=line_2.end_point, angle=180, length=side_length, width=3)
    line_3.draw(color=color_w)

    line_4 = sd.get_vector(start_point=line_3.end_point, angle=270, length=side_length, width=3)
    line_4.draw(color=color_w)


def draw_5_corner(start_point, angle_of_inclination, side_length, color_w):
    line_1 = sd.get_vector(start_point=start_point, angle=angle_of_inclination, length=side_length, width=3)
    line_1.draw(color=color_w)

    line_2 = sd.get_vector(start_point=line_1.end_point, angle=72, length=side_length, width=3)
    line_2.draw(color=color_w)

    line_3 = sd.get_vector(start_point=line_2.end_point, angle=144, length=side_length, width=3)
    line_3.draw(color=color_w)

    line_4 = sd.get_vector(start_point=line_3.end_point, angle=216, length=side_length, width=3)
    line_4.draw(color=color_w)

    line_5 = sd.get_vector(start_point=line_4.end_point, angle=288, length=side_length, width=3)
    line_5.draw(color=color_w)


def draw_6_corner(start_point, angle_of_inclination, side_length, color_w):
    line_1 = sd.get_vector(start_point=start_point, angle=angle_of_inclination, length=side_length, width=3)
    line_1.draw(color=color_w)

    line_2 = sd.get_vector(start_point=line_1.end_point, angle=60, length=side_length, width=3)
    line_2.draw(color=color_w)

    line_3 = sd.get_vector(start_point=line_2.end_point, angle=120, length=side_length, width=3)
    line_3.draw(color=color_w)

    line_4 = sd.get_vector(start_point=line_3.end_point, angle=180, length=side_length, width=3)
    line_4.draw(color=color_w)

    line_5 = sd.get_vector(start_point=line_4.end_point, angle=240, length=side_length, width=3)
    line_5.draw(color=color_w)

    line_6 = sd.get_vector(start_point=line_5.end_point, angle=300, length=side_length, width=3)
    line_6.draw(color=color_w)


# draw_3_corner(start_point=sd.get_point(350, 100), angle_of_inclination=0, side_length=150, color_w=(255, 50, 0))
# draw_4_corner(start_point=sd.get_point(100, 350), angle_of_inclination=0, side_length=150, color_w=(255, 50, 0))
# draw_5_corner(start_point=sd.get_point(350, 350), angle_of_inclination=0, side_length=130, color_w=(255, 50, 0))
# draw_6_corner(start_point=sd.get_point(100, 100), angle_of_inclination=0, side_length=100, color_w=(255, 50, 0))


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def start_shape(start_point, angle_of_inclination, side_length):
    start = sd.get_vector(start_point=start_point, angle=angle_of_inclination, length=side_length, width=3)
    return start


def paint_shape(n, start_point, side_length):
    angel = 0
    angle_start = 360 / n
    draw_line(start_point=start_point, angle_of_inclination=start, side_length=side_length)

    for i in range(n):
        start += corner
        print(start)
        return draw_line(start_point=start_point, angle_of_inclination=start, side_length=side_length)


treugolnik(n=5, start_point=sd.get_point(300, 350), side_length=150)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
