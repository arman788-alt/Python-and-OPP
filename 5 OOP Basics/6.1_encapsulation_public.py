# Various object-oriented languages like C++, Java, and Python control access modifications which are used to restrict access to the variables and methods of the class.
# Most programming languages have three forms of access modifiers, which are Public, Protected and Private in a class.
# Python uses the ‘_’ symbol to determine the access control for a specific data member or a member function of a class.
# Access specifiers in Python have an important role to play in securing data from unauthorized access and in preventing it from being exploited.
# A Class in Python has three types of access modifiers:

# Public Access Modifier
# Protected Access Modifier
# Private Access Modifier



# Public Access Modifier:
# The members of a class that are declared public are easily accessible from any part of the program. 
# All data members and member functions of a class are public by default. 

class Geek:

    # constructor
    def __init__(self, name, age):

        # public data members
        self.Name = name
        self.Age = age

    # public member function
    def displayAge(self):

        # accessing public data member
        print("Age: ", self.Age)


# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.Name)

# calling public member function of the class
obj.displayAge()



# Output
# Name:  R2J
# Age:  20

# In the above program, Name and Age are public data members and displayAge() method is a public member function of the class Geek.
#  These data members of the class Geek can be accessed from anywhere in the program.

