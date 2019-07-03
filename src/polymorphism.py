class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

pet = Animal("Dot")
print(pet.name)
print(pet.talk())     #=> None

class Dog(Animal):
    def talk(self):
        return "WOOF"

dog = Dog("Dog")
print(dog.name)
print(dog.talk())

class Cat(Animal):
    def talk(self):
        return "Meow"

cat = Cat("Cat")
print(cat.name)
print(cat.talk())
