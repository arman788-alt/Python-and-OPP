# Protected Access Modifier:

# The members of a class that are declared protected are only accessible to a class derived/child from it. 
# Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class. 

class Student:

    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):

        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):

              # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.displayDetails()


# Output
# Name:  R2J
# Roll:  1706256
# Branch:  Information Technology

# In the above program, _name, _roll, and _branch are protected data members and _displayRollAndBranch() method is a protected method of the super class Student. 
# The displayDetails() method is a public member function of the class Geek which is derived from the Student class, the displayDetails() method in Geek class accesses the protected data members of the Student class. 