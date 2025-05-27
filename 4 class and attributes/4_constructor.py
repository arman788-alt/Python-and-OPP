#  Constructors and __init__ in python

class Phone:
    manufactured = 'China'
    
    # constructor
    def __init__(self, owner, brand, price):
        self.owner = owner #samsung অবজেক্ট এর self মানে হচ্ছে samsung অবজেক্টটা নিজেই 
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)


my_phone = Phone('Arman', 'Oppo', 9800)
print(my_phone.owner, my_phone.brand, my_phone.price)
my_phone.send_sms('01814440002', 'Hi, I am from Bd, save bangladeshi students')


her_phone = Phone('Al-Amin', 'iphone', 120000)
print(her_phone.owner, her_phone.brand, her_phone.price)

dad_phone = Phone('abbbu ', 'Nokia', 3000)
print(dad_phone.owner, dad_phone.brand, dad_phone.price)





# method er bitor pass keyword mane khali bujay


# এতক্ষণ পর্যন্ত আমরা যেই Phone ক্লাস নিয়ে কাজ করছিলাম সেখানে একটা সমস্যা ছিল আমরা ফোন ক্লাস এর যতগুলো অবজেক্ট ই ডিক্লেয়ার করি কিনা তাদের সবার প্রোপার্টির মান একই থাকছে কারন আমরা ক্লাস এর মধ্যে এই প্রোপার্টির মানগুলো সেট করে ফেলসি। 
# কিন্তু ক্লাস তৈরির মেইন উদ্দেশ্য কিন্তু এটা ছিলোনা আমাদের মেইন উদ্দেশ্য হচ্ছে আমরা সেম ক্লাস দিয়ে ভিন্ন ভিন্ন ভ্যালুর অবজেক্ট তৈরি করব অর্থাৎ ক্লাসটাকে একটা টেম্পলেট হিসেবে ব্যবহার করব 

# ঠিক এই কাজটা করার জন্য কন্সট্রাক্টর ব্যবহার করা হয়। যখনই আমরা কোনো অবজেক্ট ডিক্লেয়ার করি তখন বাই ডিফল্ট সেই ক্লাস এর কন্সট্রাক্টর কল হয় এবং আমরা এই কন্সট্রাক্টর এর মাধ্যমে কোনো একটা অবজেক্ট এর প্রোপার্টি ভ্যালু এর মান সেট করতে পারি যেমন 

# class Phone:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
    
#     def call(self):
#         pass
    
# samsung = Phone("Samsung", "90000")
# iphone = Phone('Apple', '150000')
# print(samsung.brand) #output: Samsung
# print(iphone.brand) #output: Apple

# এখনে লক্ষ করি samsung এবং iphone নামে আমরা ২ টা অবজেক্ট ক্রিয়েট করছি Phone ক্লাস ইউস করে এবং Phone("Samsung", "90000") এর মাধ্যমে আমরা ফোন ক্লাস এর কন্সট্রাক্টর কে কল করেছি
# যেটা কিনা পাইথন এ def  __init__() এইভাবে ডিক্লেয়ার করা হয়। এই কন্সট্রাক্টর এর মধ্যে ভালুগুলোকে পাস করার মাধ্যেমে brand এবং price নামে ২ টা ক্লাস ভেরিয়েবল তৈরি হয়েছে যাদের মান হিসেবে কন্সট্রাক্টর এর প্যারামিটার এর মান এসাইন হয়েছে। 

#self use:
# এবং এইযে আমরা self ইউস করছি এই সেলফ টা তার সেই অবজেক্টটা নির্দেশ করে যেই অবজেক্ট থেকে এটাকে কল করা হয়েছে যেমন samsung অবজেক্ট এর self মানে হচ্ছে samsung অবজেক্টটা নিজেই এবং  iphone অবজেক্ট এর self মানে হচ্ছে iphone অবজেক্টটা নিজেই 