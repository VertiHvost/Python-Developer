# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

point_0 = sd.get_point(300, 30)


def draw_branches(point, angle, length):
    if length < 1:
        return

    a = sd.random_number(0, 20)
    b = sd.random_number(0, (30 * 40))
    delta = 30
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)

    if length < 5:
        v1.draw(color=sd.COLOR_GREEN, )
    else:
        v1.draw(width=2)
    new_point = v1.end_point
    new_length = length * .75 + a / 100

    draw_branches(point=new_point, angle=angle + (delta + b / 100), length=new_length)
    draw_branches(point=new_point, angle=angle - (delta + b / 100), length=new_length)
    return


draw_branches(point=point_0, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции

# sd.random_number()

sd.pause()
