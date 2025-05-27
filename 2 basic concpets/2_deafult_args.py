 # Default parameters and args in python

# Arbitrary Arguments, *args::
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

#1
def sum(num1, num2, num3=0, num4=0, num5=0):
    result = num1 + num2 + num3+ num4 + num5
    return result

total = sum(11, 5, 6)
# print('total: ', total)


#2
# args
def all_sum(num1, num2, *numbers):
    print("value of args: ",numbers)# agrs er value gulu touple akare thake.
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum

total = all_sum(45, 46, 89, 11, 81, 5, 2, 77)
print('all sum: ', total)

#3
def do_a_lot(*args):
    print(args)


def my_name():
    print("My name is Arman")



#4
# If the number of arguments is unknown, add a * before the parameter name:

# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

#   output: Linus



#5
# Keyword Arguments::
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# Example:
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
    
#output: The youngest child is Linus


















# পাইথনে প্যারামিটার হিসেবে আমরা ডিফল্ট প্যারামিটার এড করতে পারি যেমন-


# def sum(a, b, c = 0):
#     return a + b + c 

# result = sum(5, 4) #output 5 + 4 + 0 = 9
# result2 = sum(5, 4, 3) #output 5 + 4 + 3 = 12

# এখানে c = 0 লিখার মাধ্যমে আমরা একটা ডিফল্ট প্যারামিটার ডিক্লেয়ার করছি c = 0 এর মানে আমরা যদি এই প্যারামিটার এ কোনো ভ্যালু পাস করি তাহলে c এর মান পাস করা ভ্যালুটা হবে কিন্তু যদি আমরা পাস না করি তাহলে c এর মান 0 থাকবে 

# Note: এখন যদি কখনো আমাদের এরকম প্রয়োজন পরে যে আমরা কতগুলো প্যারামিটার পাস করব সেটা আমরা জানিনা সেক্ষেত্রে আমরা args ব্যবহার করতে পারি । args ব্যবহারের জন্য প্যারামিটার এর নামের পুর্বে * এড করে দিতে হয়। 


# def sum(*args):
#     sum = 0
#     for num in args:
#         sum = sum + num 

# result = sum(5, 4)   #output 5 + 4 = 9// Some code
# args ব্যবহারে ভ্যালুগুল একটা টাপল (টাপল সম্পর্কে আমরা পরবর্তিতে বিস্তারিত জানব) হিসেবে আসে। যেটার উপরে লুপ চালিয়ে আমরা ভ্যালুগুলোকে এক্সেস করতে পারি। 