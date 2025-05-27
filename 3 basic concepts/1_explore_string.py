# String Immutable and string methods
# string is a sequence of characters

name = 'Sakib\'s Khan' #escape 
name2 = "sakib khan"

# for multiline string
name3 = """
    Sakib khan
    number one
"""


print(name)


for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

# mutable means changeable 
# immutable means you can not change it
# name2[0] = 'R' #element not changable
# print(name2)
# if 'khan' in name2:
#     print('exists')

# print(name2.upper())






# স্ট্রিং হলো ক্যারেক্টারের সিকুয়েন্স।
# ক্যারেকটারের সিকুয়েন্স কে সিংগেল ('...') অথবা ডাবল কোটেশনের  ("...") মধ্যে রাখলে সেটি স্ট্রিং হিসেবে বিবেচিত হয়।

# myString= 'I am Phitron'
# উপড়ের স্ট্রিং এ 'P' এর ইনডেক্স কত?
# আমি জানি, অবশ্যই আপনাদের উত্তর হবে 5, উত্তর অবশ্যই সঠিক। কিন্ত 'P' এর আরেকটি ইনডেক্স রয়েছে, সেটি হলো -7 (minus seven). 

# অর্থ্যাৎ, n সাইজের পাইথন স্ট্রিং এর n তম ক্যারেকটারের ইনডেক্স হবে -১ , তার আগের ক্যারেকটারের -২ ... এভাবে চলতে থাকবে।
# স্ট্রিং কে খুবে সহজে slice করা যায়, যেমন 'I am Phitron' স্ট্রিং থেকে যদি আমরা 'Phitron' অংশটুকু পেতে চাই তাহলে myString[5:12] লিখলেই পেয়ে যাব।

# এই কাজটি অবশ্য Backward বা নেগেটিভ ইনডেক্স ব্যবহার করেও করে দেখতে পারেন। 


# Note: কিন্ত একটি কাজ কোনো ভাবেই করতে পারবে না , সেটি হলো স্ট্রিং এর কোনো ইলিমেন্ট চেঞ্জ করা। যেমন , myString[5]='T' লিখে রান করলে ইরোর খাবেন