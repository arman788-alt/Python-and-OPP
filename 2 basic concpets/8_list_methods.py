numbers = [12, 45, 98, 68]
numbers.append(56)#list er last e add hobe
print(numbers)

numbers.insert(0, 71)#index 0 te 71 insert hbe
numbers.insert(2, 81)
print(numbers)

if 98 in numbers: 
    numbers.remove(98)#lsit e 98 thakle remove hobe
if 8 in numbers:
    numbers.remove(8)  
print(numbers)

last = numbers.pop() #last element delete hobe, seta last variable e insert hbe
print(last, numbers) 

thisList = [12,32,32,45,54,"arman"]
thisList.pop(2)#2 no index er value dlt hbe
print(thisList)


# index = numbers.index(45)
if 68 in numbers:
    index = numbers.index(68)
    print(index) #index of 68

sorted = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)




#sort acending order:
# list = [3,2,4,6,7,9,10,11]
# list.sort()

#sort Descending order:
# list = [3,2,4,6,7,9,10,11]
# list.sort()
# list.reverse()
# print(list)


























#Example:
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')
# 2

# fruits.count('tangerine')
# 0

# fruits.index('banana')
# 3

# fruits.index('banana', 4)  # Find next banana starting at position 4
# 6

# fruits.reverse()
# fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# fruits.append('grape')
# fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# fruits.sort()
# fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# fruits.pop()
# 'pear'



# Array Methods::
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.




# পাইথন এ অনেকগুলো লিস্ট মেথড আছে যেমন --

# append()
# এটা লিস্ট এর শেষে কোনো ভ্যালুকে ইন্সার্ট করে 
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)
# # output: [1, 2, 3, 4, 5, 6]

# insert()
# কোনো নির্দিষ্ট ইনডেক্স এ যদি ইন্সার্ট করতে চাই তাহলে এই ফাংশনটি ইউস করা হয়, যেমন যদি আমরা ২ নাম্বার ইনডেক্স এ ১০০ ইন্সার্ট করতে চাই তাহলে
# numbers = [1, 2, 3, 4, 5]
# numbers.insert(2, 100)
# print(numbers)
# # output: [1, 2, 100, 3, 4, 5]

# remove()
# কোনো একটা ইলেমেন্ট পাস করলে সেটা লিস্ট থেকে রিমুভ করে দিবে যেমন
# numbers = [1, 2, 3, 4, 5]
# numbers.remove(3)
# print(numbers)
# # output: [1, 2, 4, 5]
# রিমুভ এর জন্য ভ্যালু টা অবশ্যই লিস্ট এ থাকতে হবে

# pop()
# লিস্টের কোনো ইনডেক্স এর নির্দিষ্ট ইনডেক্স এর ভ্যালুকে পপ করা যায় pop(i) এইভাবে যদি কোনো ইনডেক্স না দেওয়া হয়ে তাহলে list.pop() লাস্ট এর ইলেমেন্টটাকে রিমুভ করে দিবে 

# index()
# এই ফাংশনে কোনো একটা ভ্যালু দিলে সেটার ইনডেক্স রিটার্ন করে numbers.index(5) ৫ ভ্যালুটা যেই ইনডেক্স এ আছে সেটা রিটার্ন করবে

# এরকম আরো অনেক মেথড আছে যেগুলো তুমি এই লিংক থেকে দেখে নিতে পারো