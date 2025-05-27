# Private Access Modifier:

# The members of a class that are declared private are accessible within the class only, 
# private access modifier is the most secure access modifier. 
# Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. 

class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # private member function
    def __displayDetails(self):

        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # public member function
    def accessPrivateFunction(self): 

        # accessing private member function
        self.__displayDetails() #private member ke baire theke print korte prbo, kintu access korte prbo nh..mane value er maan change korte prbo nh


# creating object
obj = Geek("Arman Ullah", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()

# Output:
# Name:  R2J
# Roll:  1706256
# Branch:  Information Technology

# In the above program, __name, __roll and __branch are private members, __displayDetails() method is a private member function (these can only be accessed within the class) 
# and accessPrivateFunction() method is a public member function of the class Geek which can be accessed from anywhere within the program. The accessPrivateFunction() method accesses the private members of the class Geek.
 















#  Below is a program to illustrate the use of all the above three access modifiers (public, protected, and private) of a class in Python: 

# program to illustrate access modifiers of a class
# super class
class Super:

    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

  # public member function
    def displayPublicMembers(self):

        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):

        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):

        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):

        # accessing private member function
        self.__displayPrivateMembers()




# derived class
class Sub(Super):

      # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

      # public member function
    def accessProtectedMembers(self):

        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks !")

# calling public member functions of the class
# obj.displayPublicMembers()
# obj.accessProtectedMembers()
# obj.accessPrivateMembers()

# Object can access protected member
# print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)


# Public Data Member:  Geeks
# Protected Data Member:  4
# Private Data Member:  Geeks !
# Object is accessing protected member: 4
# In the above program, the accessProtectedMembers() method is a public member function of the class Sub accesses the _displayProtectedMembers() method which is protected member function of the class Super and the accessPrivateMembers() method is a public member function of the class Super which accesses the __displayPrivateMembers() method which is a private member function of the class Super.
 