#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
import simple_draw as sd

snowdrops_down = []


def list_snowfall(N):
    """Координаты отрисовки снежинок"""
    x_list = []
    y_list = []
    length_list = []
    i_list = []
    for _ in range(N):
        x_list.append(sd.random_number(0, 600))
        y_list.append(sd.random_number(600, 2000))
        length_list.append(sd.random_number(15, 30))
        i_list.append(sd.random_number(1, 100))


def draw_snowdrops_with_a_color(point, length, color):
    """Отрисовываем све снежинки цветом 'color' """
    sd.snowflake(center=point, length=length, color=color)


def shift_snowdrops(x_list, y_list, length_list, _):
    """ Двигаем снежинки """
    point = sd.get_point(x_list[_], y_list[_])
    point2 = sd.get_point(x_list[_ - 1], y_list[_ - 1])
    draw_snowdrops_with_a_color(point2, length_list[_ - 1], color=sd.COLOR_WHITE)
    y_list[_] -= sd.random_number(1, 4)
    x_list[_] += sd.random_number(-2, 2)
    draw_snowdrops_with_a_color(point, length_list[_], color=sd.background_color)


def number_of_the_finished_references(N):
    global snowdrops_down
    var = snowdrops_down.append(N)
    return var

def delete_snowdrops(N):
    pass
