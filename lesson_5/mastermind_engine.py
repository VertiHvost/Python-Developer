import random


def number():
    """Задумываем четырехзначное число"""
    nomber_list = []
    a = [int(x) for x in range(10)]
    for _ in range(4):
        b = a.pop(random.choice(range(len(a))))
        nomber_list.append(str(b))
    if nomber_list[0] == '0':
        nomber_list[0] = nomber_list[1]
        nomber_list[1] = '0'
    return nomber_list


def counting_cows_and_bulls(list_cattle):
    """Считает количество коров и быков"""
    counting_cows = 0
    counting_bulls = 0
    for _ in list_cattle:
        if _ == 'B':
            counting_bulls += 1
        if _ == 'C':
            counting_cows += 1
    print('bulls:', counting_bulls, 'cows:', counting_cows)
