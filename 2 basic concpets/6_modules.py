#import modules

from function import double_it as dt
#from kargs_multiple import full_name as name
#from deafult_args import *

# f_name = name('Tomato', 'Morich')
# print(f_name)
result = double_it(45)
result = dt(5)
print(result)




# Import::
# মনে করে আমাদের functions.py ফাইল এর মধ্যে একটা ফাংশন আছে sum() নামে এবং আমরা এই ফাইলটিকে আরেকটি ফাইল modules.py থেকে এক্সেস করতে চাচ্ছি তাহলে আমাদেরকে modules.py ফাইলের মধ্যে sum ফাংশনটাকে ইম্পোর্ট করতে হবে এইভাবে

# # functions.py
# def sum(a, b):
#     return a+b

# # modules.py
# from functions import sum

# result = sum(5, 6)
# এখানে একটা জিনিস মনে রাখতে হবে এইভাবে ইম্পোর্ট এর জন্য functions.py এবং modules.py ২ টা ফাইল ই একই ফোল্ডার এর মধ্যে থাকতে হবে যদি অন্য কোনো ফোল্ডার এর মধ্যে থাকে তাহলে সেটার পাথ সহ লিখতে হবে যদি ফাইল ফোল্ডার এইভাবে থাকে 

# folder

#     -functions.py

# modules.py 

# তাহলে modules.py এ ইম্পোর্ট পাথ হবে এরকম

# from folder.modules import sum

# যদি আমরা একই ফাইল থেকে মাল্টিপল ফাইল কে ইম্পোর্ট করতে চাই সেটা এইভাবে লিখা হয়

# from functions import sum, multiply
# এবং যদি আমরা functions.py ফাইল এর সবগুলো ফাংশন একসাথে ইম্পোর্ট করতে চাই তাহলে এইভাবে লিখতে হবে

# from functions import *