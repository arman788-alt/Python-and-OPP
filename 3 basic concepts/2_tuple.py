# A tuple is a collection which is ordered and unchangeable.
# tuples and tuples methods in python
# tuples vs list: লিস্টের সাথে টাপলের সবচেয়ে বড় অমিল হলো লিস্ট মিউটেবল (পরিবর্তনযোগ্য) কিন্ত টাপল ইমিউটেবল ( অপরিবর্তনযোগ্য)। 



def multiple():
    return 3, 4
print(multiple())

things = 'pen','tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'

if 'phone' in things:
    print('exists')
for item in things:
    print(item)

# things[0]='wagon'
# print(things)

items = ('book', 'monitor')

# ignore
print(len(things))
mega = ([2, 3,4], [6,8,9,5])
print(type(mega))
print(mega[0])
mega[0][1]=666
print(mega)


# list er bitor touple append kortesi and sheta for loop diye access kortesi
lst = []
lst.append((2,3))

for row,col in lst:
    print(row,col)

# for i in lst:
#     print(i[0],i[1])



# আগের মডিউলে আমরা লিস্ট সম্পর্কে জেনেছি। এই মডিউলে জানব লিস্ট এর কাছাকাছি একটী ডেটা স্ট্রাকাচার, টাপল সম্পর্কে।

# টাপল হলো কমা দিয়ে সেপারেট করা অবজেক্টের লিস্ট। তার মানে টাপলের ইলিমেন্ট হিসেবে আমরা নাম্বার,স্ট্রিং,লিস্ট ... ইত্যাদি যে কোনো কিছু রাখতে পারি। বোঝাই যাচ্ছে টাপলের সাথে লিস্টের বেশ সাদৃশ্য রয়েছে, যেমন ইনডেক্সিং, লুপিং অপারেশন গুলো লিস্টের মতোই। একটী টাপল ডিক্লেয়ার করে ফেলি-

# myTuple=['Hello',[1,2,3],17]
# লিস্টের সাথে টাপলের সবচেয়ে বড় অমিল হলো লিস্ট মিউটেবল (পরিবর্তনযোগ্য) কিন্ত টাপল ইমিউটেবল ( অপরিবর্তনযোগ্য)। এর জন্য নিচের কোড স্নিপেট টি রান করলে ইরোর আসবে-

# myTuple=['Hello',[1,2,3],17]

# myTuple=[0]='World'
# কিন্ত, মজার ব্যাপার হলো টাপলের কোনো ইনডেক্সে যদি মিউটেবল ইলিমেন্ট থাকে তাকে কিন্ত আমরা পরিবর্তন করতে পারব। যেমন-

# myTuple=[1][0] = 5


