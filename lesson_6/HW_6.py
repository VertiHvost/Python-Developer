from random import randint

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def watch_TV(self):
        print('{} смотрел телек целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 10
        else:
            print('{} деньги кончились!'.format(self.name))

    def enter_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{}, въехал в дом!!!'.format(self.name), color='green')

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_TV()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(self.food, self.money)


citizen = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citisen in citizen:
    citisen.enter_the_house(house=my_sweet_home)

for day in range(1, 21):
    cprint('=================== день {} ==================='.format(day), color='yellow')
    for citisen in citizen:
        citisen.act()
    cprint('================ в конце дня =================')
    for citisen in citizen:
        print(citisen)
    print(my_sweet_home)
