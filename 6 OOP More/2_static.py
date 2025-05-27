# static attribute, static method and class method decorator

#Note:
# static attribute-->> (class attribute)
# static method--->> @staticmethod : class er opor direct use kora jay, instace /object create kora charay use kora jay.

# class method --->> @classmethod
# differences between static method and class method

class Shopping:
    cart = [] #class attribute or static attribute
    origin = 'china'
    
    def __init__(self, name, location) -> None:
        self.name = name  # instance attribute
        self.location = location # instance attribute


    def purchase(item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod #first parameter self lage na
    def multiply(a, b):
        # print(self.name)
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self, item):
        #print(self.name)
        print('hudai dekhi kintu kinmu just ac er hawa khaite aschi', item)


basundara = Shopping('basu en dhara', 'not popular location')
#basundara.purchase('lungi', 500, 1000)

basundara.hudai_dekhi('lungi') #instance er opor use hoise
# Shopping.purchase(2, 3, 3)


Shopping.hudai_dekhi('Lungi') #classmethod bole dile evabe object chara direct class er opore use kora jay.


Shopping.multiply(4,6) #static method : instance/object charay use kora jay, ar first parameter hisebe self dewa lage na.


# basundara.multiply(6,9)
# Shopping.purchase('alu', 400, 2)






# Syntax Python Static Method:: 

# class C(object):
#     @staticmethod
#     def fun(arg1, arg2, ...):
#         ...
# returns: a static method for function fun.




# Class method vs Static Method::

# The difference between the Class method and the static method is:
# A class method takes cls as the first parameter(self) while a static method needs no specific parameters(self).
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

# When to use the class or static method?::
# We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
# We generally use static methods to create utility functions.