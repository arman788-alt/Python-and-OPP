from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name
      
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius*self.radius


r = Rectangle('Rectangle',  20, 15)
print(r.area())

c = circle('Circle', 40)
print(c.area())

# shape = [r, c]
# for s in shape:
#     print(s.area())

      
#ekhane method : area() function binno binno jaiga onujare binno binno rup nicche,,,orthat ekoi jinis er binno binno rupp nicche etake polymorphism bole.
                 #same name function but binno binno kaj kore.