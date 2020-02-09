import pickle


class Character:
    def __init__(self, race, armor, damage=10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    # calling when pickle.dump() is using. What will be included in pickled file
    def __getstate__(self):
        self.race = 'Ork'
        print('I\'m being pickled with these values: ', self.__dict__)
        return self.__dict__

    # calling when pickle.load() is using
    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')  # second argument in function get() is a default value that assigns if no 'race'
        self.damage = state.get('damage', 10)
        self.health = state.get('health', 100)
        self. armor = state.get('armor', 100)
        self. ammo = state.get('ammo', 258)
        print("I'm being unpickled with these values:", self.__dict__)
        # self.__dict__ = state


c = Character('Elf', 50)
c.hit(10)
print(c.health)

with open('game_state.bin', 'w+b') as f:
    pickle.dump(c, f)

c = None
print(c)
with open('game_state.bin', 'rb') as f:
    c = pickle.load(f)

print(c.health)
print(c.__dict__)

