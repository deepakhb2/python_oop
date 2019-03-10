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

deepak = Fighter('Deepak')
you = Fighter('You')

print(deepak)
print(you)

print(deepak.name)
print(you.name)

you.attack(deepak)

print(deepak.health)
