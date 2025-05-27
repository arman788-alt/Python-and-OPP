# Local and global scope in python

#Note:
#  you can access global variables inside a function without using the global keyword. However,
# if you want to modify a global variable inside a function, you need to use the global keyword.



# global variable
balance = 3000

def buy_things(item, price):
    # local scope variable
    # you can access global ariable without using the global keyword
    dream_phone = 'xphone' # local variable
    # if you want to modify a global variable, you have to use the global keyword
    global balance
    print(f'previous balance value', balance)
    balance = balance - price
    print( f'balance after buying {item}', balance)

    
#print(dream_phone)//not accesible
buy_things('sunglass', 1000)
print('global balance after buy', balance)



# Global Scope
# আমরা যদি কোনো একটা ভেরিয়েবল কে ফাংশন এর বাহিরে ডিক্লেয়ার করি তাহলে সেটাকে বলে গ্লোবাল ভেরিয়েবল গ্লোবাল ভেরিয়েবল কে আমরা প্রোগ্রাম এর সব যায়গা থেকে এক্সেস করতে পারি যেটাকে বলে গ্লোবাল স্কোপ তবে যদি আমরা স্পেসিফিক ভাবে গ্লোবাল ভেরিয়েবল এর উপর কোনো চেঞ্জ করতে চায় সেক্ষেত্রে global কীওয়ার্ড ব্যবহার ক্রয়তে হবে

# balance = 500

# def func():
#     print(balance) # Accessible

# func() 
# print(balance) # Accessible

# def chk():
#     balance = balance - 5 
#     # ইরর ত্রো করবে কারন balance টাকে প্রোগ্রাম নতুন ভেরিয়েবল মনে করবে তাই এটার সল্যুশন
#     # এইভাবে লিখা

# def chk():
#     global balance
#     balance = balance - 5
    
# chk()
# Local Scope
# কোনো একটা ভেরিয়েবল কে যদি আমরা কোন একটা ফাংশন এর ভিতরে ডিক্লেয়ার করি তাহলে সেটা লোকাল ভেরিয়েবল এবং এই লোকাল ভেরিয়েবল কে শুধুমাত্র সেই ফাংশন এর মধ্যে থেকেই এক্সেস করা সম্ভব অন্য কোথায় থেকে এটাকে এক্সেস করা যাবেনা এইযে ভেরিয়েবল টাকে শুধু লোকালি এক্সেস করা যাচ্ছে এটাকে বলে লোকাল স্কোপ 

# def func():
#     balance = 500
#     print(balance) #Accessible
    
# print(balance) # Not Accessible


