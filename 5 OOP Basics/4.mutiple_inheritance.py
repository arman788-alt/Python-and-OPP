#Example 1
class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game) -> None:
        self.game = game

class Student(Family, School, Sports):#multiple inheritance advantage: ekhane family, school, sports class age theke template akare thakbe,..tokhon jeta proyojon sei onujay specific oigula oigula inehrite korte prbo student cls er bitor.
    def __init__(self, address, id, level, game) -> None:
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        Family.__init__(self, address)


#Example 2

# class watch:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def displayTime(self):
#         print("Displaying Time")


# class FitnessTracker:
#     def __init__(self, price):
#         self.price = price
    
#     def Track_step(self):
#         print("Tracking Step")

#     def Tracking_Calories(self):
#         print("Tracking Calories")


# class SmartWatch(watch, FitnessTracker): #multiple inheritance
#     def __init__(self, brand, model, price):
#         watch.__init__(self, brand, model)
#         FitnessTracker.__init__(self, price)
    
#     def Display(self):
#         print("Displaying")


# Apple = SmartWatch("Apple", "Ultra", 100000)
# Apple.Display()
# Apple.displayTime()
# Apple.Track_step()
# Apple.Tracking_Calories()