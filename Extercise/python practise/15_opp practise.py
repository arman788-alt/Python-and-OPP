# class gadget:

#     def __init__(self, brand, price, memory, made):
#         self.brand = brand
#         self.price = price
#         self.memory = memory
#         self.made = made

#     def run(self):
#         return f"running this"

# class laptop(gadget):

#     def __init__(self, brand, price, memory, made, display):
#         self.display = display
#         super().__init__(brand, price, memory, made)

#     def run(self):
#          return f"running laptop: {self.brand}"



# class phone(gadget):
        
#         def __init__(self, brand, price, memory, made, ssd):
#              self.ssd = ssd
#              super().__init__(brand, price, memory, made)
        
#         def calling(self, text, number):
#              self.text = text
#              self.number = number
#              return f"sending sms to : {self.number} with : {self.text}"
        

# class camera:
#      def __init__(self, pixel):
#           self.pixel = pixel
    

# my_phone = phone('realme', 15000, '64gb' 'india' , 212)

# my_phone.calling('hello', '01814440002')


# my_laptop = laptop('AsusZenbook', '560000', '512gb', 'china', '14inch')

# print(my_laptop.brand, my_laptop.display)
# print(my_laptop.run())


# class family:
#     def __init__(self, address):
#         self.address = address

# class school:
#     def __init__(self, id, cls):
#         self.id = id
#         self.cls = cls
# class sports:
#     def __init__(self, game):
#         self.game = game

# class fvrt:
#     def __init__(self, item):
#         self.item = item 

# class student(family, school, sports, fvrt):
#     def __init__(self, address, id, cls, game, item):
#         family.__init__(self,address )
#         school.__init__(self, id, cls)
#         sports.__init__(self, game)
#         fvrt.__init__(self, item)


# arman = student('Rajabonshoo', 430,  9, 'cricket', 'mango' )

# print(arman.address)
# print(arman.cls)
    
        
#MULTI LEVEL INHERITANCE::

# class vehicle:
#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price
#     def run(self):
#         pass

# class Bus(vehicle):
#     def __init__(self, name, price, seat):
#         self.seat = seat
#         super().__init__(name, price)


# class MiniBus(Bus):
#     def __init__(self, name, price, seat, Ac, color):
#         self.Ac = Ac
#         self.color = color
#         super().__init__(name, price, seat)
#     def run(self):
#         print('Class from MiniBus: ',self.name, self.price, self.seat, self.Ac, self.color)



# class Truck(vehicle):
#     def __init__(self, name, price, weight):
#         self.weight = weight
#         super().__init__(name, price)
#     def run(self):
#         print('Class from Truck: ',self.name, self.price, self.weight)


# class MiniTruck(Truck):
#     def __init__(self, name, price, weight, temperature):
#         self.temperature = temperature
#         super().__init__(name, price, weight)
#     def run(self):
#         print('Class from MiniTruck: ',self.name, self.price, self.weight, self.temperature)


# VipBus = MiniBus('Brtc', 1200000, 80, True, 'Bluee')
# VipBus.run()

# tata = MiniTruck('Tata', 170000, '5Ton', 26)
# tata.run()
# print(tata.name, tata.price)


# class student:

    
#     def __init__(self, name, id, address):
#         self.name = name
#         self.__id = id
#         self.__address = address
    

#     def __showDetails(self):
#         print('Name : ', self.name)
#         print('ID : ', self.__id)
#         print('ADDRESS : ', self.__address)
    
#     def access_privateData(self):
#           self.__showDetails()


# obj = student('Arman', 430, 'uttara')
# obj.access_privateData()

# obj.name = 'ashraf'#change the public attribute name
# obj.access_privateData()

        

#Public, Private, Protected::

# class bank:
#     def __init__(self, name, initial_deposit, branch):
#         self.name = name
#         self.__balance = initial_deposit
#         self._branch = branch
    

#     def depostite(self, amount):
#         self.__balance += amount
#         return self.__balance
        
    
#     def get_balance(self):
#         return self.__balance
    
#     def withdrow(self, amount):
#         if amount < self.__balance:
#             self.__balance = self.__balance - amount
#             return amount
#         else :
#             return f'Etoo takaa tmr accountn e naai'


# janata = bank('Arman', 10000, 'Uttara')

# print(janata.name)
# janata.name = 'Arafat'
# print(janata.name)

# print(janata.depostite(200))

# print(janata.get_balance())

# print(janata.withdrow(1700))
# print(janata.get_balance())
# print(janata.withdrow(20000000))


class animals:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print('I make sound from animals')

class cat(animals):
    def __init__(self, name)->None:
        super().__init__(name)

    def make_sound(self):
        print("meow meow")


class dog(animals):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("gheow gheow")

class pakhi(animals):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("kuuu kuuu")

class goat(animals):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("meee meee")




cat = cat('memeee')
# cat.make_sound()

dog = dog('babuuu')


pakhi = pakhi('chorii')

goat = goat('rajaa')



animals = [cat, dog, pakhi, goat]

for animal in animals:
    print(animal.make_sound())


    
    

