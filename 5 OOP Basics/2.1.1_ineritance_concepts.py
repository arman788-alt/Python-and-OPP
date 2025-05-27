# base class, parent class
class BaseClass:
    pass

# derived class or child class
class DerivedClass(BaseClass):
    pass


"""
1. simple inheritance: parent class --> child class (Gadget ---> Phone) (Gadget --> Laptop)

2. Multi-level inheritance: Granda --> Parent --> child (Vehicle --> Bus ---> ACBus) (Vehicle --> Truck --> PickupTruck): example dadar shompotti tar baba peyechee r shee(child) tar babar and tar dadar 2jon ei shompotti pabe tar babar thekee.

3. Multiple inheritance: Student (Family, School, Sports)

4. Hybrid: Granda --> Father, Uncle, Aunty --> Child (Father, Uncle)
"""



# Python Inheritance:
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.



# so far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# Note: The __init__() function is called automatically every time the class is being used to create a new object.







# Benefits of inheritance are:

# Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class. The benefits of Inheritance in Python are as follows:

# It represents real-world relationships well.
# It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
# Inheritance offers a simple, understandable model structure. 
# Less development and maintenance expenses result from an inheritance.


# Different types of Python Inheritance:::

# There are 5 different types of inheritance in Python. They are as follows:

# Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
# Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.
# Multilevel inheritance: When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, 
# which in turn is inheriting from its parent class. 
    
# Hierarchical inheritance More than one derived class can be created from a single base.
# Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.




# SUPER()::
# The super() function is a built-in function that returns the objects that represent the parent class. 
# It allows to access the parent class’s methods and attributes in the child class.



class Father:
  a = 10
  b = 20
  def __init__(self):
    print(self.a + self.b)


class Son(Father):
   x = 100
   y = 200
   def __init__(self):
     super().__init__()
     print(self.x + self.y)


obj = Son()
