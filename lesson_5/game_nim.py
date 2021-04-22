from random import randint

_holder = []


def put_stones():
    '''рассположить камни для начала игры'''
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))


def take_from_bunch(position, quantity):
    """сколько берем из кучки"""
    if 0 <= position <= len(_holder):
        _holder[position - 1] -= quantity


def get_bunches():
    """количество камней в кучке"""
    return _holder


def is_gameover():
    """Условия для выигрыша"""
    return sum(_holder) == 0
