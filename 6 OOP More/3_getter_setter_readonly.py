# Getter Setter and Read only property Using Property Decorator

# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    # getter without any setter is read only attribute
    @property # age method ke attribute akare use korte chaile property docoretor use korte hoy.
    def age(self):
        return self._age

    # getter 
    @property # same 
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value

samsu = User('Kopa', 21, 12000)

#print(samsu.__money) #priavte proterty hide thakbe,errorType: object has no attribute '__money'
# print(samsu.age()) 

print(samsu.age) #@property dororetor use korar fole, age function ke attribute hisebe use kora jabe.
print(samsu.salary) # same
samsu.salary = 4500
print(samsu.salary)