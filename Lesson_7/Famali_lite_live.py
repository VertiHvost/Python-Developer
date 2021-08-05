# -*- coding: utf-8 -*-
import random
from random import randint

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mess = 0

    def __str__(self):
        return 'грязь = {}, еды = {}, денег = {}'.format(self.mess, self.food, self.money)


class Husband():

    def __init__(self, name):
        self.name = name
        self.level_happiness = 100  # уровень счастья
        self.satiety = 30  # сытость
        self.Money = None
        self.Food = None

    def __str__(self):
        return 'Состояние {}: сытость = {}, счастье = {}'.format(self.name, self.satiety, self.level_happiness)

    def act(self):
        nomber = random.randint(1, 3)
        print(nomber)
        if nomber == 1:
            self.work()
        if nomber == 2:
            self.eat()
        if nomber == 3:
            self.gaming()

    def eat(self):
        self.Food -= randint(5, 30)
        self.level_happiness += 50
        print('{} покушал'.format(self.name))

    def work(self):
        self.Money += 150
        self.level_happiness += 10
        self.satiety -= 10
        print('{} пошел на работу'.format(self.name))

    def gaming(self):
        self.level_happiness += 30
        self.satiety -= 10
        print('{} поиграл в приставку'.format(self.name))


class Wife(House):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.level_happiness = 100  # уровень счастья
        self.satiety = 30  # сытость

    def __str__(self):
        return 'Состояние {}: сытость = {}, голод = {}'.format(self.name, self.satiety, self.level_happiness)

    def act(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


print('Жила интелегентная пара душа в душу, печалей не знала ')

home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    # masha.act()
    cprint(serge, color='cyan')
    # cprint(masha, color='cyan')
    cprint(home, color='cyan')
