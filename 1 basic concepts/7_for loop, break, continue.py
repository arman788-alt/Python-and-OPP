# nums jodi array hoi
# for( int i = 0; i < 5; i++){
#   int num = nums[i]
# }

# numbers = [5, 10, 15, 20, 25]
# sum = 0
# for num in numbers:
#     print(num)
#     sum = sum + num
#     if sum > 20:
#         print('bigger sum', sum)
# print(sum)


text = 'Pagla Howar'
for char in text:
    print(char)

# nums = [1, 2, 3 4, 5, 6, 7, 8, 9, 10]
# print(range(1, 10))



# The range() Function::---->>>>>>
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.
# range([start], stop[, step])
    

# for x in range(6):
#   print(x)
# # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.


# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):



# # Using the start parameter:
# for x in range(2, 6):
#   print(x)

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):


# # Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
#   print(x)





for i in range(1, 10, 2):
    print(i)
#ekhane 2 hocche por por koto ghor kore agabe seta ..manee step argument;




#     সি , সি ++ এ ফর লুপে যেমন ইনিশিয়ালাইজেশন , কন্ডিশন , ইনক্রিমেন্ট , ডিক্রিমেন্ট ইউজ করা হয় , পাইথন এ এইগুলার প্রয়োজন নাই আসলে ।
# এখানে range নামে একটা মেথড ইউজ করি আমরা সেখানে initialization , ইনক্রিমেন্ট , ডিক্রিমেন্ট দেওয়া যায় আর অটোমেটিক কন্ডিশন apply হয়ে যায় 


# range([start], stop[, step])
# রেঞ্জ মেথড এর কিছু এক্সাম্পল খেয়াল করি 

# # Example 1: range with only stop argument
# for i in range(5):
#     print(i)  # Output: 0, 1, 2, 3, 4

# # Example 2: range with start and stop arguments
# for i in range(2, 5):
#     print(i)  # Output: 2, 3, 4

# # Example 3: range with start, stop, and step arguments
# for i in range(1, 10, 2):
#     print(i)  # Output: 1, 3, 5, 7, 9
    


# এখন কিছু ফর লুপের এক্সাম্পল খেয়াল করি 

# for loop:

# # Example: Print numbers from 1 to 5 using a for loop
# for num in range(1, 6):
#     print(num)
    
# Output:
# 1
# 2
# 3
# 4
# 5
    

# for loop with if elif statement:------->>>>>>

# # Example: Print numbers from 1 to 10 and classify them as even or odd using a for loop with if-elif statement
# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")

# Output:
    
# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd
# 6 is even
# 7 is odd
# 8 is even
# 9 is odd
# 10 is even
    

# for loop with continue statement:------->>>>>

# # Example: Print numbers from 1 to 5, skipping even numbers using a for loop with continue statement
# for num in range(1, 6):
#     if num % 2 == 0:
#         continue
#     print(num)


# Output:
# 1
# 3
# 5

# for loop with break statement::------------->>>>>>

# # Example 1: Print numbers from 1 onwards until reaching a number greater than 5 using a for loop with break statement
# for num in range(1, 10):
#     print(num)
#     if num > 5:
#         break
    
# Output:
# 1
# 2
# 3
# 4
# 5
# 6


# Exapmle2:

# for letter in 'geeksforgeeks':
#     # break the loop as soon it sees 'e' or 's'
#     if letter == 'e' or letter == 's':
#         break

# print('Current Letter :', letter)
    
# Output: 
# Current Letter : e



# for loop with string::------------->>>>>>>>>

# # Example: Iterate over each character in a string
# word = "Python"

# for char in word:
#     print(char)


# Output:

# P
# y
# t
# h
# o
# n
    

# # Loop through the letters in the word "banana"::

# for x in "banana":
#   print(x)

# output:
# b
# a
# n
# a
# n
# a





# for loop with list::------------>>>>>>
    
# # Example: Iterate over each element in a list
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)
    

# Output:

# 1
# 2
# 3
# 4
# 5


# friends = ['nobel', 'ashir', 'rabi', 'naz']
# for friend in friends:
#     print(friend)


##Exit the loop when x is "banana"::

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


##Exit the loop when x is "banana", but this time the break comes before the print
                                
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
    


# for i in range(1, 100):
#     if(i == 99):
#         break
#     print(i)
    

# # Do not print banana::

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# output:
# apple
# cherry






# Nested Loops::---------->>>>>>
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example:1
# Print each adjective for every fruit:

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# output:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry


# Example:2
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)


# Output :

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3 



# Python for loop Enumerate::---------->>>>>>>>
# In Python, the enumerate() function is used with the for loop to iterate over an iterable while also keeping track of the index of each item.



# Example:1
array = ['arman', 'rakib', 'ashraf']

for index, element in enumerate(array):
    print(index, element)


# The pass Statement::
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# Example
# for x in [0, 1, 2]:
#   pass


# Python for loop in One Line::

# Numbers =[x for x in range(11)]
# print(Numbers)

# Output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    


