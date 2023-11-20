from ninjaclass import Ninja
#class pet
class Pet :
    def __init__(self,name,type,tricks,health,energy):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy

    def sleep(self):
        self.energy+=25

    def eat(self):
        self.energy+=5
        self.health+=10

    def play(self):
        self.health+=5

    def noise(self):
        print(f'the sound of {self.name}')

class dog(Pet):
    def __init__(self, name, type, tricks, health, energy,age):
        super().__init__(name, type, tricks, health, energy)
        self.age=age

        
cat=Pet("taymour","cat","ykhabech",100,100)
oussema=Ninja("oussema","helali",cat,"croket","salami")

oussema.walk()
oussema.feed()
oussema.bathe()

Dog=dog('bobby','dog','danger',100,100,5)