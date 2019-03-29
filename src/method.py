class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage

deepak = Fighter('Deepak')
you = Fighter('You')

print(deepak.name)
print(you.name)

you.attack(deepak)

print(deepak.health)
