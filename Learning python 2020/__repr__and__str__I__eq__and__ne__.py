class Character:
    def __init__(self, race, damage=10):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __str__(self):
        return f"{self.race} with damage= {self.damage}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        else:
            return False

    # def __ne__(self, other):
    #     pass


c = Character('Elf')
print(repr(c))      # Character('Elf', 10)
print(c)            # Elf with damage= 10
d = eval(repr(c))
print(type(d))      # <class '__main__.Character'>
print(d)            # Elf with damage= 10
print(c == d)       # return False without dunder method __eq__(self, other). Comparing only memory location
# print(c == d)     # return True with our dunder method __eq__(self, other)
