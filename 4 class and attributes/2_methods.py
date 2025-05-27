# Creating and Using Methods

def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text 

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)







# আমরা আগের মডিউল এ একটা সিম্পল ক্লাস ডিক্লেয়ার করেছিলাম যেখানে কিছু ক্লাস ভেরিয়েবল ডিক্লেয়ার করেছিলাম 
# আমরা একটা ক্লাস এর মধ্যে ভেরিয়েবল ছাড়াও মেথড ও ডিক্লেয়ার করতে পারি একটা মেথড কোনো একটা ভেরিয়েবল এর বিহেবিয়ার কে নির্দেশ করে 
# যেমন আমাদের Phone ক্লাস এর একটা বিহেবিয়ার হতে পারে Call তাহলে এই নামে আমরা একটা মেথড ডিক্লেয়ার করতে পারি এইভাবে

# class Phone:
#     price = 19000
#     color = 'blue'
#     brand = 'samsung'
    
#     def call(self):
#         print('Calling one person')
    
# myphone = Phone()
# myphone.call() #output: Calling one person

# এখানে call() নামে যেই ফাংশন এর মতো ডিক্লেয়ার করা হয়েছে ক্লাস এর মধ্যে এটাই মেথড।
# ফাংশন যখন কোনো একটা ক্লাস এর আন্ডারে ডিফাইন করা হয় তখন সেটাকে মেথড বলে এবং 
# এই মেথডটি প্রতিটি অবজেক্ট এর জন্য স্বতন্ত্রভাবে কাজ করে যেমন myphone.call() এর মাধ্যমে myphone নামের অবজেক্ট এর call মেথডকে কল করা হয়েছে। 

#Note: মনে রাখতে হবে পাইথনে মেথড ডিক্লেয়ার করার ক্ষেত্রে প্রথম প্যারামিটার হিসেবে self দিতে হবে

# এবং আমরা চাইলে একটা ক্লাস এর মধ্যে মাল্টিপল মেথডও ক্রিয়েট করতে পারি এইভাবে 


# class Phone:
#     price = 19000
#     color = 'blue'
#     brand = 'samsung'
    
#     def call(self):
#         print('Calling one person')
        
#     def send_message(self, message):
#         return f"Sending message: {message}"
    
# myphone = Phone()
# myphone.call() #output: Calling one person
# print(myphone.send_message("Hello World")) #output:Sending message: Hello World 

# একটা ফাংশন এর মতো করে আমরা মেথড এও প্যারামিটার নিতে পারি এবং মেথড থেকে কোনোকিছু রিটার্ন ও করতে পারি 