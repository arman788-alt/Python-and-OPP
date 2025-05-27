# list, array, collection is same (simple terms)
# Lists are used to store multiple items in a single variable.
# list jekeno type er data store korte pare.
# List items are ordered, changeable, and allow duplicate values.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# index =   0   1   2   3   4  5   6   7   8   9  
numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]
# index = -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 
 
#Access List Items:
print(numbers[3], numbers[-3])

# list( start : end ) # start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[1:7])

# list(start : end : step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[4:])#ending index mention na korle by default ending  porjonto jabe
print(numbers[:5])#starting index mention na korle by default starting index theke hbe
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) #shortcut to reverse a list


# Check if Item Exists:
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")



thislist = ["apple", "banana", "cherry"]

for i in thislist:
    if i == "apple":
        print("yes,apple in this list")











# লিস্ট এ আমরা এরের মতো করে চিন্তা করতে পারি তবে C/C++ এর এরের তুলনায় পাইথনের লিস্ট এ কিছু ভিন্নতা আছে।

# পাইথন এ এইভাবে লিস্ট কে ডিফাইন করা হয়

# numbers = [1, 2, 3, 4, 5]
# এবং লিস্টে ২ ধরনের ইন্ডেক্সিং রয়েছে শুরু থেকে শেষ পর্যন্ত ইন্ডেক্সিং হচ্ছে এরকম 0, 1, 2 ... n-1 আবার উল্টা দিক থেকেও এটার ইন্ডেক্সিং সম্ভব এই ইনডেক্স টা এইভাবে হয় -1, -2, -3 ... -n 

# এই ইনডেক্সগুলো ইউস করে এইভাবে ইলেমেন্ট গুলোকে এক্সেস করতে পারি

# numbers[0]  # এটার ভ্যালু ১
# numbers[-1] # এটার ভ্যালু ৫

# কোনো একটা লিস্টকে আমরা এইভাবে স্লাইস করে ফেলতে পারি

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[2:6])
# #output: [3, 4, 5, 6]
# এটার সিন্ট্যক্সটা এরকম list[start : end] যেখানে স্টার্ট থেকে শুরু করে end-1 পর্যন্ত ভ্যালু নিয়ে আরেকটা লিস্ট এটা আমাদের রিটার্ন করবে 

# আরেকটা সিনট্যাক্স হচ্ছে list[start : end : step] এখানে আমরা step ডিক্লেয়ার করে দিতে পারি নিচের উদাহরণটি দেখলে এটা ক্লিয়ার হয়ে যাবে


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[0:8:2])
# #output: [1, 3, 5, 7]
# আমরা এই স্টেপ এর টেকনিকটাকে উল্টাভাবে প্রিন্ট এর জন্যেও ব্যবহার করতে পারি 


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[8:2:-1])
# #output: [8, 7, 6, 5, 4]
# এখন তোমাদের কাজ হচ্ছে ইনডেক্স গুলো চেঞ্জ করে করে আউটপুট পর্যবেক্ষন করে বোঝার চেষ্টা করা কি ঘটছে।

# আমরা এখানে স্টার্ট বা এন্ড  ইনডেক্স স্পেসিফিকভাবে ডিফাইন না করে দিলে এটা বাই ডিফল্ট স্টার্ট বা ইন্ড ইনডেক্স নিয়ে নেয় যেমন এটা ৩ নাম্বার ইনডেক্স থেকে শেষ পর্যন্ত প্রিন্ট করছে
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[3:])
# #output: [4, 5, 6, 7, 8]

# একইভাবে এটা শুরু থেকে ৫-১ ইনডেক্স পর্যন প্রিন্ট করবে
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[:5])
# #output: [1, 2, 3, 4, 5]

# তেমনি কোনো কিছু ম্যানশন না করে numbers[:] এইভাবে লিখলে পুরো লিস্ট টাই চলে আসবে

# তেমনি আমরা যদি এইভাবে লিখি তাহলে পুরো লিস্ট টাই রিভার্স হয়ে যাবে numbers[::-1] এখানে আমরা start, end কোনটাই দেয়নি শুধু স্টেপ ডিক্লেয়ার করছি। 

# এরকম আরো মজার কিছু জিনিস জানতে এই লিংক থেকে সবকিছু দেখে ফেলো।



