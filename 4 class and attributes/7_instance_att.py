# Class Attributes vs instance attributes:

class Shop:
    shopping_mall = 'Jamuna'
    # cart = [] # cart is a class attribute

    def __init__(self, buyer):
       self.buyer = buyer
       self.cart = []  # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


    
       
mehjabeen = Shop('Mez jab een')
mehjabeen.add_to_cart('shoe')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)
 
nisho = Shop('nishi night er nisho')
nisho.add_to_cart('hat')
nisho.add_to_cart('watch')
print(nisho.cart)

apurvo = Shop('age purbo chilo')
apurvo.add_to_cart('chiruni')
print(apurvo.cart)





# পাইথনে অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং নিয়ে কাজ করার জন্য ক্লাস এট্রিবিউট এবং ইন্সট্যান্স এট্রিবিউট এর ব্যাপারে জানাটা ভীষণ জরুরি। 

# ক্লাস এট্রিবিউটঃ
# ক্লাস এট্রিবিউট বোঝার জন্য নিচের উদাহরনটা লক্ষ করি--


# class Shop:
#     cart = []
    
#     def __init__(self, buyer):
#         self.buyer = buyer
    
#     def add_to_cart(self, product):
#         self.cart.append(product)
        
# mamun = Shop("Mamun")
# mamun.add_to_cart("Shoes")
# mamun.add_to_cart("Shirt")
# print("After mamun added:", mamun.cart)

# mahmud = Shop("Mahmud")
# mahmud.add_to_cart('Cap')
# mahmud.add_to_cart("Watch")
# print("After mahmud added:", mahmud.cart)
# এই কোডটাকে যদি রান করি তাহলে এরকম আউটপুট পাবো


# After mamun added: ['Shoes', 'Shirt']
# After mahmud added: ['Shoes', 'Shirt', 'Cap', 'Watch']
# কিন্তু আউটপুট এবং কোড ২ টা যদি আমরা খেয়াল করি তাহলে দেখব যে মাহমুদ add_to_cart() করার পরে যদিও আমরা mahmud.cart এইভাবে ভ্যালুগুলোকে প্রিন্ট করছি তারপরও সেখানে আগের অবজেক্ট এর এড করা প্রোডাক্ট ও রয়ে গেছে এই জিনিসটাই হচ্ছে ক্লাস এট্রিবিউট অর্থাৎ 
# এই এট্রিবিউট টা এই ক্লাস এর প্রোপার্টি এই ক্লাস এর যেকোনো এট্রিবিউট দিয়ে যদি এই এট্রিবিউট এ কোনো চেঞ্জ হয় সেটা ডিরেক্ট এই এট্রিবিউট এই চেঞ্জ করবে


# ইন্সট্যান্স এট্রিবিউটঃ
# এখন দেখি ইন্সট্যান্স এট্রিবিউট কিভাবে কাজ করে

# class Shop:
    
#     def __init__(self, buyer):
#         self.buyer = buyer
#         self.cart = []
    
#     def add_to_cart(self, product):
#         self.cart.append(product)
        
# mamun = Shop("Mamun")
# mamun.add_to_cart("Shoes")
# mamun.add_to_cart("Shirt")
# print("After mamun added:", mamun.cart)

# mahmud = Shop("Mahmud")
# mahmud.add_to_cart('Cap')
# mahmud.add_to_cart("Watch")
# print("After mahmud added:", mahmud.cart)
# এই কোডটাকে যদি রান করি তাহলে এরকম আউটপুট পাবো

# After mamun added: ['Shoes', 'Shirt']
# After mahmud added: ['Cap', 'Watch']
# এইবার দেখুন যখন যেই অবজেক্ট যেটা যেটা add_to_cart এ এড করছে সেটা শুধু সেই অবজেক্ট এর আন্ডারেই এড হয়ছে




