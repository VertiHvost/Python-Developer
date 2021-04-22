from game_nim import is_gameover, get_bunches, take_from_bunch, put_stones
from termcolor import cprint

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input('Откуда берем?')
    qua = input('Сколько берем?')
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', color='red')
    if is_gameover():
        break


print('Выиграл игрок номер', user_number)
