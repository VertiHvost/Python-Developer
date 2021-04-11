# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
# создаем списки для начальных точек координат отрисовки снежинок
x_list = []
y_list = []
length_list = []
for _ in range(N):  # заполняем списки
    x_list.append(sd.random_number(400, 400))
    y_list.append(sd.random_number(400, 400))
    length_list.append(sd.random_number(15, 30))

# sd.random_number(100, 700)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# TODO здесь ваш код
# def tochka(x, y):
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     x += 10
#     if y<0:
#         break
def my_snowflake(point, length):
    sd.snowflake(center=point, length=length)


  # передаем х и у
while True:  # отрисовываем снижинки и перемещаем
    for _ in range(N):
        # sd.clear_screen()  # отчистка экрана
        point = sd.get_point(x_list[_], y_list[_])
        my_snowflake(point, length_list[_])
        y_list[_] -= sd.random_number(1, 2)
        x_list[_] += sd.random_number(-2, 2)
        if y_list[_] < 0:
            break
        # point2 = sd.get_point(x_list[_+1], y_list[_+1])
        # sd.snowflake(center=point2, length=length_list[_+1])
        # y_list[_+1] -= sd.random_number(1, 2)
        # x_list[_+1] += sd.random_number(-2, 2)
        # if y_list[_+1] < 0:
        #     break


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
