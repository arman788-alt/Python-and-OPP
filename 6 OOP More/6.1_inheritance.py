# Class Composition. inheritance vs composition


# inheritance provides you "is a" relation

class Animal: 
    pass

# Dog is a animal
class Dog(Animal): #Animal cls e joto property thakbe sob Dog, Tiger class er moddhe thakbe.
    pass

# Tiger is a animal
class Tiger(Animal):
    pass



class Furniture:
    pass

# chair is a furniture
class Chair(Furniture):
    pass

# table is a furniture
class Table(Furniture):
    pass

# bed is a furniture
class Bed(Furniture):
    pass