# Operator overloading and method overriding

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

    def exercise(self):#ei function ke obssoi override korte hbe nahole error dibe.
        raise NotImplementedError #function ke subclass cls theke override korar jonno force kore er maddhome.

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override : parrent cls er method jodi child cls o thake tahole override hoye jabe sei method.
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('gym e poisa diya hudai gham jorai')



    # + sign operator overload
    def __add__(self, other):#Those all are python dunder method/magic method
        return self.age + other.age #sakib.age + mushi.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    # > operator overload
    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer('sakib', 38, 68, 91, 'BD')
mushi = Cricketer('mushi', 36, 65, 78, 'BD')
# sakib.eat()
# sakib.exercise()

# plus sign overload
#print(45 + 63)
print( 'Sakib' + 'Rakib')
print([12, 98] + [5,6,7,1,2])

# operator overloading mainly class er object create korle ...multiple object add, sub, mul, etc korte chaile direct operator diye kaj kore nah, tokhon oy operator er jonno class er bitor overaload korte hoi.
print(sakib + mushi) #shakib.__add__(mushi),,,, sakib, mushi hocche object , object ke direct jug kora jaynh, tai class er bitor add function overload korechi. 
print(sakib * mushi) #shakib.__mul__(mushi)
print(len(sakib))
print(sakib > mushi)


# Python Operator Overloading
# In Python, we can change the way operators work for user-defined types.

# For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

# This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.


# Dunder/Magic method::
# Here are some of the special functions available in Python,

# Function	Description
# __init__() initialize the attributes of the object
# __str__()	returns a string representation of the object
# __len__()	returns the length of the object
# __add__()	adds two objects
# __call__() call objects of the class like a normal function


# Example: + Operator Overloading in Python

# To overload the + operator, we will need to implement __add__() function in the class.



# In the above example, what actually happens is that, when we use p1 + p2, 
# Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2).
# After this, the addition operation is carried out the way we specified.

# Similarly, we can overload other operators as well. 
# The special function that we need to implement is tabulated below.


# Operator	  Expression	        Internally(internall method)
# Addition	     p1 + p2	        p1.__add__(p2)
# Subtraction	 p1 - p2	        p1.__sub__(p2)
# Multiplication p1 * p2	        p1.__mul__(p2)
# Power	         p1 ** p2	        p1.__pow__(p2)
# Division	     p1 / p2	        p1.__truediv__(p2)
# Floor Division p1 // p2           p1.__floordiv__(p2)
# Remainder (modulo)	p1 % p2	    p1.__mod__(p2)
# Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
# Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
# Bitwise AND	p1 & p2	            p1.__and__(p2)
# Bitwise OR	p1 | p2	            p1.__or__(p2)
# Bitwise XOR	p1 ^ p2	            p1.__xor__(p2)
# Bitwise NOT	~p1                 p1.__invert__()


# Less than	p1 < p2	                p1.__lt__(p2)
# Less than or equal to	p1 <= p2	p1.__le__(p2)
# Equal to	p1 == p2	            p1.__eq__(p2)
# Not equal to	p1 != p2	        p1.__ne__(p2)
# Greater than	p1 > p2	            p1.__gt__(p2)
# Greater than or equal to p1 >= p2	p1.__ge__(p2)





