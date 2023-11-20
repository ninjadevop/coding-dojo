#class ninja
class Ninja :
    def __init__ (self,first_name,last_name,pet,treats,pet_food):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        self.treats=treats
        self.pet_food=pet_food

    def walk(self):
        self.pet.play()  # walk() - walks the ninja's pet invoking the pet play() method
    def feed(self):  
        self.pet.eat()   # feed() - feeds the ninja's pet invoking the pet eat() method
    def bathe(self):
        self.pet.noise()   # bathe() - cleans the ninja's pet invoking the pet noise() method