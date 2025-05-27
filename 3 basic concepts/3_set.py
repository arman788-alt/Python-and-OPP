# Set and set methods in python
# সেট মিউটেবল




# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate
numbers = [12, 56 , 98, 98, 78, 56 , 12 , 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(12)
numbers_set.add(12)
numbers_set.add(12)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)
# numbers_set[1] = 5
for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B)
print( A | B) #AUB



# এই মডিউলে আমরা পাইথনের সেট ডেটা স্ট্রাকচার সম্পর্কে জানব।
# আগের মডিউলে দেখেছি, লিস্ট ডিক্লেয়ার করতে হয় [ ] ব্যবহার করে, টাপল ডিক্লেয়ার করা হয় ( ) ব্যবহার করে, এই মডিউলে দেখব সেট ডিক্লেয়ার করা হয় { } ব্যবহার করে-

# mySet={3,5,6,7,8,2,2,3}
# print(mySet)
# কোডটি রান করে আউতপুটের দিকে লক্ষ্য করি-
# mySet সেটে ২ দুইবার, ৩ দুইবার ছিল। কিন্ত আউটপুটে একবার করে আসল !! আরেকটি ব্যাপার , ইলিমেন্ট গুলো সর্ট হয়ে আসল !!
# তার মানে, সেট হলো ইউনিক ডেটার কালেকশন, অর্থ্যাৎ , সেটে কোনো ডুপ্লিকেট ভ্যালু থাকবে না ।


# সেট মিউটেবল, কিন্ত এসাইনমেন্ট অপারেশন এক্সেপ্ট করে না, add( ) , remove( ) ফাংশন ব্যবহার করে ডেটা এ্যাড, ডিলিট করা যায়। সেই সাথে কিছু সেট অপারেশন যেমন |(Union), &(Intersection) ইত্যাদি ব্যবহার করা যায়-

# mySet = {3,5,6}
# yourSet = {6,7,8}
# ourSet = mySet & yourSet
# print(ourSet)