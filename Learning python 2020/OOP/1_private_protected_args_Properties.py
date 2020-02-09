class Character:
    MAX_SPEED = 100
    DEAD_HEALTH = 0

    def __init__(self, race, damage=10):
        self.__race = race  # it is private attribute: is visible only inside class body
        self.damage = damage
        self._health = 100  # it is protected attribute: is also visible inside heir class bodies
        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


unit = Character('Ork')
print(unit._Character__race)  # calling a private attribute without properties
unit.hit(20)
print(unit._health)  # calling a protected attribute without properties
print('-------------------------------------------------------------------')
print(unit.race)
print(unit.health)
# unit.health = 0  # AttributeError: can't set attribute
print('-------------------------------------------------------------------')
print(unit.current_speed)
unit.current_speed = 72
print(unit.current_speed)

