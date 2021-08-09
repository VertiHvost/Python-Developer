class organizer:

    def __init__(self):
        self.count = 6

    def __str__(self):
        return f'{self.count} осталось инструмента в органайзере'


class tooling:
    """Класс инструменты """

    def __init__(self):
        self.width = 0.5
        self.length = 20
        self.org = Org


class pen(tooling):
    """ручка с ластиком"""

    def __init__(self):
        super().__init__()
        self.length_rubber = 3

    def act(self):
        self.org.count -= 1
        print('забрали одну ручку')


class pencil(tooling):
    """карандаш"""

    def __init__(self):
        super().__init__()

    def act(self):
        self.org.count -= 1
        print('забрали один карандаш')


Org = organizer()
a = pencil()
b = pen()
a.act()
b.act()
print(Org)