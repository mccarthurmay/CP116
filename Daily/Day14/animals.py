#our basic class will be an animal

class Animal():
    #constructor for class
    def __init__(self):
        #hunger is on a scale from 0-100
        self.hunger = 50
        #tiredness is on a scale from 0-100
        self.tiredness = 50
        if self.hunger >= 100:
            die(self)
        if self.tiredness >= 100:
            die(self)
    def eat(self):
        self.hunger -= 10

    def sleep(self):
        self.tiredness -= 10

    def move(self):
        self.hunger += 10
        self.tirendess += 10
    def die(self):
        print("dead")

#Mammal class - subclass of Animal
class Mammal(Animal):
    #overriding init of animal class with one that is more specific to mammals
    def __init__(self,fur_color):
        super().__init__()
        self.fur = fur_color

class Cat(Mammal):
    def __init__(self, fur_color, reg_num):
        suepr()._init__()
        self.reg = reg_num

class WingedAnimal(Animal):

    def fly(self):
        self.hunger += 30
        self.tiredness += 30

class Bat(WingedAnimal, Mammal):
    def _init__(self, fur_color):
        super()._init__(fur_color)


felix = Cat("black", 15254)
print(felix.reg, felix.hunger)
felix.move()
print(felix.reg, felix.hunger)
