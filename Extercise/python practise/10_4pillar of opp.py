# #simple inheritance

# class gadget:
#     def __init__(self, brand, price, color, made):
#         self.brand = brand
#         self.price = price
#         self.color = color
#         self.made = made
    
#     def brand_name(self):
#         print(f"Brand name: {self.brand}")

# class phone(gadget):
#     def __init__(self,brand, price, color, made, dual_sim):
#         self.dual_sim = dual_sim

#         super().__init__(brand, price, color, made)

#     def call(self, number, text):
#             print(f'Text: {text} {number}')


# class laptop(gadget):
#     def __init__(self, brand, price, color, made, ssd):
#         self.ssd = ssd
#         super().__init__(self, brand, price, color,made)

#     def coding(self):
#          print(f"I'm practising python with this brand: {self.brand}")

# class camera:
#      def __init__(self, pixel):
#           self.pixel = pixel
    
#      def change_lense(self):
#           pass


# # my_phone = phone('realme', 15000, 'blue', 'indian', True)
# # print(my_phone.brand)
# # print(my_phone.color)
# # print(my_phone.dual_sim)
# # print(my_phone.brand_name())
# # print(my_phone.call('01814440002', 'hey ashraf still use this number you?'))


# my_camera = camera('don')
# print(my_camera.pixel)



# #mutli level inheritance:
# class Vehicle:
#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price

# class Bus(Vehicle):
#     def __init__(self, name, price, seat, normal_cost):
#         self.seat = seat
#         self.normal_cost = normal_cost
#         super().__init__( name, price)
#     def bus_class(self):
#         print(f"inside from bus class: {self.name}, {self.price}, {self.seat}, {self.normal_cost}")


# class ACBUS(Bus):
#     def __init__(self, name, price, seat, normal_cost, temperature, ACBUS_seat_cost):
#         super().__init__( name, price, seat, normal_cost)
     
#         self.ACBUS_seat_cost = ACBUS_seat_cost
#         self.ACBUS_seat_extra_cost = ACBUS_seat_cost - normal_cost
#         self.temperature = temperature

#     def ACBUS_CLASS(self):
#         print(f"inside from ACBUS  class: {self.name}, {self.price}, {self.seat}, {self.normal_cost}, {self.temperature}, {self.ACBUS_seat_cost}, {self.ACBUS_seat_extra_cost}")

# class truck(Vehicle):
#     def __init__(self, name, price, weight):
#         self.weight = weight
#         super().__init__( name, price)

# class MiniTruck(truck):
#     def __init__(self, name, price,  weight):
#         super().__init__( name, price,  weight)



# # BRTC = ACBUS('BRTC', 1000000, 50, 500, 15, 950)
# # print(BRTC.ACBUS_seat_extra_cost)
# # print(BRTC.ACBUS_CLASS())


# # mini_truck = MiniTruck('Tata', '20 luck', '1000 kg')
# # print(mini_truck.price, mini_truck.name)
        

# class arman:
#     def __init__(self, A_phy, A_math):
#         self.A_phy = A_phy
#         self.A_math = A_math

# class sajjad:
#     def __init__(self, S_phy, S_math):
#         self.S_phy = S_phy
#         self.S_math = S_math
# class total(arman, sajjad):
#     def __init__(self, A_phy, A_math, S_phy, S_math ):
#         arman.__init__(self,A_phy, A_math)
#         sajjad.__init__(self, S_phy, S_math)

#     def sum(self):
#         self.sum = self.A_phy + self.A_math + self.S_phy + self.S_math
#         if self.sum > 120:
#             print('Yes pass')
#         else:
#             print('fail')

# get_marks = total(50, 40, 33, 3)
# print(get_marks.sum())
    


#ENCAPSULATION:
# class bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance#private
#         self.address = 'uttara'

#     def withdraw(self, amount):
#         if amount < self.__balance:
#             self.__balance = self.__balance - amount
#             return amount
#         else:
#             print('I your account no enough money:')
#     def deposit(self, amount):
#         self.__balance = self.__balance + amount
        
        

#     def getBalance(self):
#         return self.__balance


# janata = bank('Arman', 10000)
# # print(janata.balance)
# # janata.balance = 0
# # print(janata.balance)

# print(janata.address)
# janata.address = 'tongi'
# print(janata.address)
# print(janata.withdraw(30000))
# print(janata.withdraw(500))
# print(janata.getBalance())
# print(janata.deposit(50000))
# print(janata.getBalance())


