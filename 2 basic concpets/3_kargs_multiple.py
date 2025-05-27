#Topic: (advanced) kargs, multiple return from a function

def full_name(first, last):
    name = f'full name is: {first} {last}'
    return name

# take parameters in order(serial wise)
# name = full_name('Alu', 'kodu')

#serial wise chara
name = full_name(last='kodu', first='alu')
print(name)



# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f' {first} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='Taher', last='Ali', title="Hujur", title2="Shayokh", last2='taheri')
print(name)

# def function_name(num1, num2, *args, **kargs):




# আমরা যদি কখনো পাইথন ফাংশন থেকে মাল্টিপল ভ্যালু রিটার্ন করতে চাই তাহলে সেটাকে আমরা কমা সেপারেটেড ভ্যালু হিসেবে রিটার্ন করতে পারি সেক্ষেত্রে এটা টাপল আকারে রিটার্ন করবে এবং আমরা চাইলে লিস্ট বা ডিকশানারি আকারেও ভ্যালুগুলোকে রিটার্ন করতে পারি 
# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    # return [sum, mult, remain]
    return sum, mult, remain


everything = a_lot(55, 21)
print(everything)#touple akare return korbe












# args প্যারামিটার এর ক্ষেত্রে আমাদেরকে ভ্যালুগুলো সিরিয়াল অনুযায়ী দিতে হতো। আমরা চাইলে প্যারামিটার গুলোকে কি ভ্যালু পেয়ার আকারেও দিতে পারি যেটাকে kargs বলে যেমনঃ-

# def func( **kwargs):
#     print(f"apple: {kwargs['apple']}")
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')

# result = func(apple = 5, orange= 4)
# যখন আমরা প্যারামিটার kwargs হিসেবে পাস করি তখন সেটা একটা ডিকশনারি (ডিকশনারির ব্যাপারে আমরা পরবর্তিতে জানব)  আকারে থাকে এটা থেকে ভ্যালু এক্সেস করতে হলে kwargs['key_name'] এইভাবে এক্সেস করতে পারি। আমরা চাইলে উপরের উদাহরণের মতো কী, ভ্যালু আকারেও ভ্যালু এক্সেস করতে পারি। 

# আমরা যদি কখনো পাইথন ফাংশন থেকে মাল্টিপল ভ্যালু রিটার্ন করতে চাই তাহলে সেটাকে আমরা কমা সেপারেটেড ভ্যালু হিসেবে রিটার্ন করতে পারি সেক্ষেত্রে এটা টাপল আকারে রিটার্ন করবে এবং আমরা চাইলে লিস্ট বা ডিকশানারি আকারেও ভ্যালুগুলোকে রিটার্ন করতে পারি 


# def func( a, b, c):
#     return a, b, c # return as tuple (a, b, c)
#     return [a, b, c] # return as list [a, b, c]
#     return {'a': a, 'b': b} # return as dictionary





