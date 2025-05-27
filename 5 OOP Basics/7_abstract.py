#Example 1
from abc import ABC, abstractmethod
# abstract base class
class Animal(ABC): #Animal ABC ke inherit kore, animal class ekhn ekta abstract class, jar khomota asee abstract method ke rakhar.

    @abstractmethod  #Note: enforce all derived class to have a eat method,, #abstract class amader force kore abstract method gulaa ke, inherit kora cls e implement korar jonno.,, abstract class ke inherit korle asbtract method gula ke o oy class e banaite hbe must.              
    def eat(self):
        print('I need food')
    
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('Hey na nana, I am eating banana')

    def move(self):
        print('Hanging on the branches')

layka = Monkey('lucky')
layka.eat()















#Example 2
# from abc import ABC, abstractmethod
# class shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Rectangle(shape):

#     def __init__(self, lenght, widht):
#         self.lenght = lenght
#         self.widht = widht
   
#     def area(self):
#         return self.lenght * self.widht
    
#     def perimeter(self):
#         return 2 * (self.lenght + self.widht)
    
#     def onnofun(self):
#         pass

# class circle(shape):

#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.1416 * self.radius ** 2
      
#     def perimeter(self):
#         return 2 * self.radius * 3.1416
    
    
# rect = Rectangle(2, 3)
# print("Area of rectangle", rect.area())
# print("perimeter of rectangle", rect.perimeter())

# cir = circle(4)
# print("Area of circle", cir.area())
# print("perimeter of circle", cir.perimeter())

