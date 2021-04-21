from game_nim import is_gameover, get_bunches, take_from_bunch, put_stones

put_stones()
user_number = 1
while True:
    print('Текущая позиция')
    print(get_bunches())
    print('Ход игрока {}'.format(user_number))
    pos = input('Откуда берем?')
    qua = input('Сколько берем?')
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1

print('Выиграл игрок номер', user_number)