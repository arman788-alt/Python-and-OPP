# Common and uncommon things and Inheritance

# base class, super class, parent class, common attribute + functionality class ,,jekhane others class er common jinis gulaa thakbe.
# derived class, child class, uncommon attribute + functionality class 

#Example 1
class Gadget: # gadget  hocche parent class,, jekhane child class er common attribute & method thakbe, etee duplication/repatation komee jabee:

    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running laptop: {self.brand}'


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'learning python and practicing'
    
class Phone(Gadget):#phone hocche child class , phone class e gadget class er sob property chole ashcee..mane parent class(gadget class) ke inherit korbe child class(phone class)
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)#parent class(gadget) er constructor ke call korte super key use hoy.
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass


# inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone.phone_call('01814440002', 'Hello Brother, Can you help mee?'))
print(my_phone.__repr__())




#Example : 01
# class shape:
#     def __init__(self,dim1,dim2):
#         self.dim1=dim1
#         self.dim2=dim2

#     def area(self):
#         print("I am area method of shape class")


# class triangle(shape):
#     def area(self):
#         area= 0.5 * self.dim1 * self.dim2
#         print("Area of Triangle :", area)


# class rectangle(shape):
#     def area(self):
#         area= self.dim1 * self.dim2
#         print("Area of rectangle :", area)
 
# t1 = triangle(20,30)
# t1.area()

# r1=rectangle(20,30)
# r1.area()



# Example 3
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):    #Now the Student class has the same properties and methods as the Person class.
#   pass

# x = Student("Mike", "Olsen")
# x.printname()





