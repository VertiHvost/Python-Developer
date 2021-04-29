# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 40
# создаем списки для начальных точек координат отрисовки снежинок
x_list = []
y_list = []
length_list = []
i_list = []
for _ in range(N):  # заполняем списки
    x_list.append(sd.random_number(0, 600))
    y_list.append(sd.random_number(600, 2000))
    length_list.append(sd.random_number(15, 30))
    i_list.append(sd.random_number(1, 100))


# sd.random_number(100, 700)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# TODO здесь ваш код


def my_snowflake(point, length, color):
    sd.snowflake(center=point, length=length, color=color)


# передаем х и у
while True:  # отрисовываем снижинки и перемещаем
    sd.start_drawing()  # отчистка экрана
    for _ in range(N):
        if y_list[_] < i_list[_]:
            continue
        point = sd.get_point(x_list[_], y_list[_])
        point2 = sd.get_point(x_list[_ - 1], y_list[_ - 1])
        my_snowflake(point2, length_list[_ - 1], color=sd.COLOR_WHITE)
        y_list[_] -= sd.random_number(1, 4)
        x_list[_] += sd.random_number(-2, 2)
        my_snowflake(point, length_list[_], color=sd.background_color)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
