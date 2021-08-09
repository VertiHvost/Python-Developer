# -*- coding: utf-8 -*-

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
        self.ashed = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме денег: {self.money}, еды: {self.food}, кошачья еда: {self.cat_food}, грязи: {self.ashed}'


class Human:

    def __init__(self):
        self.fullness = 30
        self.happiness = 100
        self.house = home

    def __str__(self):
        return f'еда: {self.fullness}, счастье {self.happiness}'

    def depression(self):
        if self.house.ashed >= 90:
            self.happiness -= 5

    def hungry(self):
        self.fullness -= 10


class Husband(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):

        if (self.fullness <= 0) or (self.happiness <= 0):
            cprint(f'{self.name} умер...', 'red')
            return

        super().depression()
        super().hungry()

        dice = randint(1, 4)

        if self.house.money < 70:
            self.work()
        elif self.happiness < 30:
            self.gaming()
        elif self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.work()
        elif dice == 4:
            self.pet_the_cat()

    def pet_the_cat(self):

        if self.fullness < 20:
            self.eat()
            return

        elif alice.happiness < 30:
            self.work()
            return

        else:
            self.happiness += 5
            cprint(f'{self.name} гладил кота')
            return

    def eat(self):

        if self.fullness > 40:
            self.work()
        elif self.fullness > 30:
            self.gaming()
        elif self.house.food > 20:
            self.fullness += 20
            self.house.food -= 20
            cprint(f'{self.name} поел, теперь eго сытость:{self.fullness}')
        elif self.house.food < 30:
            cprint(
                f'{self.name} пытался поесть, но дома нет еды... Он расстроился и его счастье уменьшилось до {self.happiness}',
                'red')

    def work(self):
        if self.fullness < 30:
            self.eat()
        else:
            self.fullness -= 10
            self.house.money += 200
            self.happiness += 10
            cprint(
                f'{self.name} заработал 150 крышек, теперь денег дома:{self.house.money} он рад что все идет хорошо и его счастье вырастает до {self.happiness}')

    def gaming(self):
        if self.happiness > 40:
            self.act()
        elif self.fullness < 20:
            self.eat()
        elif alice.happiness < 30:
            self.work()
        else:
            self.happiness += 30
            cprint(f'{self.name} заигрался в танки, зато теперь его счастье:{self.happiness}')


class Wife(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):

        if (self.fullness <= 0) or (self.happiness <= 0):
            cprint('{} умерла...'.format(self.name), color='red')

        super().depression()
        super().hungry()

        dice = randint(1, 5)

        if self.house.food < 60:
            self.shopping()
        elif self.happiness < 30:
            self.buy_fur_coat()
        elif self.fullness < 40:
            self.eat()
        elif self.happiness < 30:
            self.buy_fur_coat()
        elif self.house.ashed > 70:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.buy_fur_coat()
        elif dice == 5:
            self.pet_the_cat()

    def pet_the_cat(self):

        if self.fullness < 20:
            self.eat()

        elif self.happiness > 100:
            self.clean_house()

        elif self.happiness > 5:
            cprint(f'{self.name} гладила кота')

    def eat(self):

        eat_count = randint(20, 30)

        if self.fullness > 40:
            self.shopping()

        elif self.house.food < 30:
            self.shopping()

        elif self.house.food > eat_count:
            self.fullness += eat_count
            self.house.food -= eat_count
            cprint(f'{self.name} поелa, теперь ee сытость:{self.fullness}')

        else:
            self.happiness -= 10
            cprint(
                f'{self.name} пыталась поесть, но дома нет еды... Она расстроилась и ее счастье уменьшилось до {self.happiness}',
                'red')

    def shopping(self):
        food_count = randint(30, 60)
        cat_food_count = randint(10, 20)

        if self.house.money > 400:
            food_count *= 3
            cat_food_count *= 2

        elif self.house.money > 250:
            food_count *= 2
            cat_food_count *= 2

        if (self.fullness < 20) and (self.house.food > 30):
            self.eat()

        elif self.house.food > 100:
            self.act()

        elif self.house.money <= food_count + cat_food_count:
            cprint(f'{self.name} хотела пойти в магазин, но деньги кончились', 'red')
            self.clean_house()

        elif (self.house.cat_food < 40) or (self.house.cat_food < 20):
            self.house.food += food_count
            self.house.cat_food += cat_food_count
            self.house.money -= cat_food_count + food_count
            self.happiness += 10

            cprint(f'{self.name} закупилась продуктами, теперь в холодильнике:{self.house.food}'
                   f',а так же захватила кошачью еду, теперь ее:{self.house.cat_food}, она рада что все хорошо и ее радость выросла до {self.happiness}')

        else:
            self.house.food += food_count
            self.house.money -= food_count
            self.happiness += 10
            cprint(f'{self.name} закупилась продуктами, теперь в холодильнике:{self.house.food}'
                   f', она рада что все хорошо и ее радость выросла до {self.happiness}')

    def buy_fur_coat(self):

        if self.house.money > 400:
            self.house.money -= 350
            self.happiness += 60
            cprint(f'{self.name} очень рада что купила шубу, теперь ее счастье:{self.happiness}')
            return

        elif self.house.money < 400:
            cprint(f'{self.name} очень хотела шубу, но у них пока нет денег на нее')
            self.pet_the_cat()

        elif self.happiness > 100:
            self.clean_house()

    def clean_house(self):

        if self.house.ashed > 90:
            self.house.ashed -= 100
            cprint(
                f'{self.name} весь день убиралась, зато теперь дома дома чище и ее счастье выросло до {self.happiness}')

        elif self.house.ashed < 90:
            self.act()

home = House()
serge = Husband(name='Сережа')
alice = Wife(name='Алиса')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    alice.act()
    cprint(serge, color='cyan')
    cprint(alice, color='cyan')
    cprint(home, color='cyan')
    home.ashed += 5