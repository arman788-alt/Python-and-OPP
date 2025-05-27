# ques1: Create a Product class and a Shop class.

# class shop:
#     def __init__(self, buyer):
#         self.buyer = buyer
#         self.card = []

#     def add_to_cart(self, item_name):
#         self.card.append(item_name)
    
#     def customer(self):
#         for i in self.card:
#             print(f'Buyer name: {self.buyer} he buy those product: {i}')


# class product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def Product_price(self):
#         self.total = self.price * self.quantity
#         return self.total

# shopno = product('nodules', 140, 3)
# print(shopno.Product_price())

# arman = shop('Arman')
# arman.add_to_cart('Tel')
# arman.add_to_cart('Mangsho')
# arman.add_to_cart('Moshla')
# arman.add_to_cart('piyaj')

# arman.customer()




# ques2: Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
# class product:
#     def __init__(self, buyer):
#         self.buyer = buyer
#         self.card = []
#     def add_product(self, item):
#         self.card.append(item)

# class shop(product):
#     def __init__(self, buyer):
#         super().__init__(buyer)
    
#     def add_productss(self):
#         for i in self.card:
#             print(f'product name: {i}')


# arman = shop('arman')
# arman.add_product('alu')
# arman.add_product('teel')
# arman.add_productss()
        