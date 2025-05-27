# 1
# Customer
# Employee
# Admin

from abc import ABC
from cards import card
class User(ABC):#ABC ক্লাস কে ইনহেরিট করার মাধ্যমে User ক্লাস কে Abstract ক্লাস হিসেবে তৈরি করা হয়েছে

    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone



class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.cart = card() #add to card korte. 

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name) #ekahne item hisebe object return korbe: item_name,price,quantity
        if item is not None:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("Item not found")

    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")    
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")#total_price( ) মেথডে  @property ডেকোরেটর ব্যবহার করা হয়েছে ।


    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()
        
class Employee(User):#User ক্লাস কে ইনহেরিট কওরে Employee ক্লাস লিখে ফেলি-

    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


# emp = Employee("rahim", "rahim@gmail.com", 1279787, "Dhaka", 23, "Chef", 12000)
# print(emp.name)

class Admin(User):#অনুরুপ ভাবে Admin ক্লাস তৈরি কওরে এতে add_employee( ) , view_employee( ) নামের ২ টি মেথড এ্যাড কওরে ফেলি-

    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
    
    def view_menu(self, retaurent):
        retaurent.menu.show_menu()
















