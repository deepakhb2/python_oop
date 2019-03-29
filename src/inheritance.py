class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print("{} attacks {}!".format(self.name, other_guy.name))
        print("{} loses {} health points!".format(other_guy.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)

class Boxer(Fighter):
    def heal(self):
        self.health += 10

boxer_deepak = Boxer("Deepak")
print(boxer_deepak)
print(boxer_deepak.damage)
print(boxer_deepak.health)

boxer_deepak.heal()

print(boxer_deepak)
