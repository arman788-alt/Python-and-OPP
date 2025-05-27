# print('Now I need money')
# input()
# input('Give me some money: ')
# money = input('Give me some money: ')
# print("here is your money", money)


first_money= input('Kodom Ali, Dosto kichu taka dey: ')
second_money= input('Peyara begum, dosto kichu taka dey: ')

print(type(first_money))
# by default the input from user will be string type:
print('money I got from Kodom', first_money, 'and from peyara', second_money)

# Type casting:
first_money_int=int(first_money)
second_money_int = int(second_money)
# print(type(first_money_int))
# total = first_money + second_money
total = first_money_int + second_money_int
print('total money i got: ', total)

""" 
Google Search 
1. convert number to string: str
2. convert decimal number: float
3. python int vs float
"""

# পাইথন এ ইনপুট নেওয়া বাকি সকল প্রোগ্রামিং ল্যাঙ্গুয়েজ থেকে অনেক বেশি সহজ ।
# জাস্ট ইংলিশ কীওয়ার্ড input এই নামের function ইউজ করলেই ইনপুট নেওয়া যায় । 

#Note: তবে মাথায় রাখতে হবে যে ইনপুট ফাংশন সবসময় স্ট্রিং ফরমেট এ ডাটা স্টোর করে ।
# তাই একটা ইন্টেজার ইনপুট নিলেও সেটা স্ট্রিং হয়ে যাবে । 
# সেক্ষেত্রে টাইপকাস্টিং করে সেটাকে ইন্টেজার এ কনভার্ট করে নিতে হবে 

# first_money = input("Enter first amount : ")
# second_money = input("Enter second amount : ")
# print(first_money + second_money)

# output : 
# Enter first amount : 100
# Enter second amount : 200
# 100200

# after typcasting

# first_money = input("Enter first amount : ")
# second_money = input("Enter second amount : ")
# print(int(first_money) + int(second_money))

# output:
# Enter first amount : 100
# Enter second amount : 200
# 300