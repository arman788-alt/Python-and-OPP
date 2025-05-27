""" 

"""
# define 
def double_it(num):
    result = num * 2
    print('inside the function.py file', result)
    return result

double_it(8)
double_it(88)

def sum(num1, num2):
    result = num1 + num2
    return result

total = sum(44, 39)
print('total value', total)

final = double_it(total)
print('final value', final)




# def sum(a, b):
#     return a + b
    
# result = sum(5, 4)
# print(result)

# # output: 9
# এখানে sum হচ্ছে ফাংশন নেম a, b হচ্ছে দুইটা প্যারামিটার এবং এদের যোগফল রিটার্ন স্টেটমেন্ট এর মাধ্যমে রিটার্ন করা হয়েছে।
# আমরা যদি কোনো ফাংশন থেকে কোনোকিছু রিটার্ন না করি তাহলে বাই ডিফল্ট সেটা None রিটার্ন করে 