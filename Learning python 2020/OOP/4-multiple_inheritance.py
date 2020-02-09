class Animal:
    def set_health(self, health):
        print('set in animal')


class Carnivore(Animal):
    def set_health(self, health):
        super().set_health(health)
        print('set in carnivore')


class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        print('set in mammal')


class Dog(Mammal, Carnivore):
    def set_health(self, health):
        super().set_health(health)
        print('set in dog')


dog = Dog()
dog.set_health(10)


class Animal:
    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage


class Carnivore(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 4


c = Carnivore()
c.hit(10)
print(c.health)
