#The word "polymorphism" means "many forms",   
#and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# poly --> many (multiple)
# morph --> shape

# Advantage: 

class  Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow') #override hobee,,Advantage of polymorphism: jodi binno binno class er under e binno binno name e function nam dey jegula mone rakha kothin big project e...tai eki name function thakle subidha pawa jay.

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('beh beh beh')

    

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shephard')
shepard.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('gora gori')

animals = [don, shepard, mess, less]
for animal in animals:
    animal.make_sound()#ekhane ekoi method er opor difference difference rupp dicche. orthat ekoi jinis er binno binno rupp nicche etake polymorphism bole.
                       #function name ekoi but kaj kore binno binno

# or
# for animal in [don, shepard, mess, less]:
#     animal.make_sound()






















# class animal:
#     def __init__(self):
#         pass


#     def sound(self):
#         print("Animal sound")


# class dog(animal):
#     pass

   
# kukur = dog()
# kukur.sound()
