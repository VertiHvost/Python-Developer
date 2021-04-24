# Загадываение числа
# Ввод предполагаемого числа
# Проверка числа коров
# Проверка кол - во быков
# Выход из игры


def the_hidden_number():
    import random
    '''Загадываение числа'''
    n = [i for i in range(10)]
    number = []
    for _ in range(4):
        a = n.pop(random.choice(range(len(n))))
        number.append(str(a))
    print(number[0])
    if number[0] == '0':
        number[0] = number[1]
        number[1] = '0'
    return print(number)


def entered_number():
    """Ввод числа с консоли и проверка на уникальность цифр"""
    list_nomber = []
    nomber = input("Введите четырехзначное число в котором цифры не повторяются")
    for i in nomber:
        if i not in list_nomber:
            list_nomber.append(i)
        else:
            return print('Вы ввели повторяющииеся цифры, попробуйте снова')
    if len(list_nomber) == 4:
        return print(int(nomber)), print('Все верно')
    else:
        print('Нужно ввести четырехзначное число')


def col_B_cnd_C(user_nomber, nomber):
    """Проверка количества коров быков"""
    for i in range(3):
        if user_nomber[i] == nomber[i]:
            user_nomber[i] = 'B'
    for y, i in enumerate(user_nomber):
        if i in nomber:
            user_nomber[y] = 'C'
    print(user_nomber)
