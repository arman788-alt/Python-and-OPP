class A:
     def __init__(self, num1):
         self.num1 = num1
     
     # > sign operator overloading
     def __gt__(self, other):
          if(self.num1 > other.num1):
               return 'obj1 is greater than obj2'
          else:
               return 'obj2 is greater than obj1'
          
    # = sign operator overloading    
     def __eq__(self, other):
          if(self.num1 == other.num1):
               return 'Both are Equal'          
          else :
               return 'Both are Not Equal'
     
          


obj1 = A(20)
obj2 = A(11)

print(obj1 > obj2)

print(obj1 == obj2)
