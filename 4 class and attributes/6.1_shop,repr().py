class shop:
    def __init__(self, name):
        self.name = name
        self.products = [] #instance attribute
        self.balance = 500
    
   
    def add_product(self, name, price):
        Product = product(name, price) #instance or object same kotha
        self.products.append(Product)


    def __repr__(self):

        for EachProduct in self.products:
            print(f"Product: {EachProduct} ")
        return f"The Shop name is: {self.name}"
    

                                      
class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} {self.price};"


shop1 = shop("starteck")

shop1.add_product('Iphone', 150000)
shop1.add_product('realme', 350000)
shop1.add_product('dekstop', 150000)



shop2 = shop('Shopno')
shop2.add_product('Aluu', 120)
shop2.add_product('teel', 150)
shop2.add_product('daal', 250)

print(shop1.products)
# print(shop2.products)
print(shop1)
print(shop2)

# _repr_ :: sudhu object dhore print korle oi object er class e jevabe repr method dewa thakbe sevabe print korbe.





