#instance method:
# 1.instance method are methods which require an object of its class to be created before it can be called.
# 2.instance methods need a class instance and can access the instance through self.set
# 3.instance method takes more that one parameter, self, which point to instance of class when the method is called
# 4.The self parameter, instance methods can freely access attributes and other methods on the same object.

class myClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    #instance method
    def avg(self):
        print((self.a + self.b)/2)

m1 = myClass(20, 30)
m1.avg()

# Here a and b are instance variable and these get initialize when create an object for
# the myClass . if we want to call avg() method which is an instance method, we must create
# an object for the class