from datetime import datetime


class Life:
    birthdate = datetime.now()
    weight = 1
    height = 1
    position = 0

    def breath(self):
        print('Ohh')

    def move(self, value):
        self.position += value
        print('Life move')

    def eat(self, food):
        if isinstance(food, int):
            self.weight += food

    def __ge__(self, other):
        if not isinstance(other, Life):
            raise
        return self.weight < other.weight


class Primate(Life):
    weight = 3
    height = 2


class Man(Primate):
    def eat(self, food, cooked=False):
        print('man eat')
        if isinstance(food, int):
            if cooked:
                self.weight += food*2
            else:
                self.weight += food

    def move(self, value):
        print('Man move')
        super().move(value)


class Spider(Life):
    def eat(self, food):
        print('spider eat')
        if isinstance(food, int):
            self.weight += food * 1.5

    def weave(self):
        return 'Net'

    def move(self, value):
        print('Spider move')
        super().move(value)


class SpiderMan(Man, Spider):
    def move(self, value):
        print('SpiderMan move')
        super().move(value)


peter = SpiderMan()
peter.move(10)
miles = SpiderMan()
print(SpiderMan.mro())

print(peter <= miles)
