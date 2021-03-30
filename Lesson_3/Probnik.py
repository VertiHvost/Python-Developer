
import simple_draw as sd


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
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=1)
        point = end_point
        # t2 = sd.get_vector(t1.end_point, angle + 120, length, 5)
        # sd.line(start_point=t1.end_point, end_point=t2.end_point, color=sd.COLOR_YELLOW, width=1)
        # sd.line(start_point=t2.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)


# (point_start_x, point_start_y, length_start, type_of_polygon)
start_point = [(100, 100, 150, 3), (350, 100, 150, 4), (100, 350, 100, 5), (350, 350, 100, 6)]

for _ in start_point:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    heads_start = _[3]
    polygon(point_start, heads_start, length_start)


sd.pause()