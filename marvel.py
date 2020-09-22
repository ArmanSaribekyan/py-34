from pprint import pprint


class Person:
    height = 50  # cm
    weight = 5  # kg

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.pocket = []

    def eat(self, food):
        self.weight += food

    def run(self, hours):
        self.weight -= hours * 1  # lose 1 kg/h

    def change_name(self, name):
        self.name = name

    def date(self, person):
        if not isinstance(person, Person):
            return
        self.mood = 'good'
        self.eat(1)
        person.mood = 'good'
        person.eat(1)


peter = Person('Peter', 'M')
mary = Person('Mary', 'F')

pprint(Person.__dict__)

pprint(peter.__dict__)
pprint(mary.__dict__)

peter.pocket.append('coin')

print(peter.pocket)
print(mary.pocket)

pprint(peter.__dict__)
pprint(mary.__dict__)

peter.date(mary)

print(peter.mood, mary.mood)
