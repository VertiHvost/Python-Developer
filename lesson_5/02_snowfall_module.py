# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


def falling_snowflake():
    snowflakes_length = [sd.random_number(10, 101) for _ in range(20)]
    snowflakes_point = {i: [sd.random_number(0, 500), 500, i] for i in range(20)}
    old_points_arr = [[snowflakes_point[key][0], snowflakes_point[key][1]] for key, val in snowflakes_point.items()]
    while True:
        sd.start_drawing()
        for i in range(20):
            if len(old_points_arr) < 20:
                sd.snowflake(center=old_points_arr[i], length=snowflakes_length[i], color=sd.background_color)
            x, y, delay = snowflakes_point[i]
            if delay < 1:
                point = sd.get_point(x, y)
                sd.snowflake(center=sd.Point(old_points_arr[i][0], old_points_arr[i][1]),
                             length=snowflakes_length[i], color=sd.background_color)
                sd.snowflake(center=point, length=snowflakes_length[i])
                if y < 20:
                    snowflakes_point[i][1] = 500
                    continue
                snowflakes_point[i][1] -= 9
                snowflakes_point[i][0] += sd.random_number(-10, 10)
                old_points_arr[i] = [x, y]
            snowflakes_point[i][2] -= .2
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


def main():
    falling_snowflake()
    sd.pause()


if __name__ == '__main__':
    main()