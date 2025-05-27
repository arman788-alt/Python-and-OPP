# dunder or magic method
#   __repr__() method

# example: 1
class shop:
    def __init__(self, name):
        self.name = name #instance
    
    def __repr__(self):
         return f"Shop name is: {self.name}"

shop1 = shop("Showpno")
print(shop1.name)
print(shop1) # use of dunder method _repr_



# example: 2
class GFG:

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f'Name is {self.name}'

	def __repr__(self):
		return f'GFG(name={self.name})'


obj = GFG('GeeksForGeeks')

# print(obj.__str__()) #output: Shop name is: Showpno
# print(obj.__repr__()) #output: GFG(name=GeeksForGeeks)

print(obj)


# _repr_ :: sudhu object dhore print korle oi object er class e jevabe repr method dewa thakbe sevabe print korbe.


# Python-এর __repr__ মেথডের কাজ হলো কোনো অবজেক্টের string representation রিটার্ন করা, যা মূলত ডিবাগিং ও লগিংয়ের জন্য ব্যবহার করা হয়।

# __repr__ মেথড কী কাজ করে?
# যখন print(object) বা repr(object) কল করা হয়, তখন __repr__ মেথড রান হয়।

# এটি এমন একটি স্ট্রিং রিটার্ন করে যা অবজেক্ট সম্পর্কে স্পষ্ট তথ্য দেয়।

# মেথডটি সাধারণত এমনভাবে লেখা হয় যেন eval() ফাংশনের মাধ্যমে সেটি ব্যবহার করে অবজেক্টকে পুনরায় তৈরি করা যায়।

# যদি __str__ ডিফাইন করা থাকে, তাহলে print(object) করলে __str__ কল হবে, আর যদি __str__ না থাকে, তাহলে __repr__ ব্যবহৃত হবে।


# সংক্ষেপে __repr__ মেথডের কাজ:
# ✅ অবজেক্টের একটি informative representation প্রদান করে।
# ✅ ডিবাগিং ও লগিংয়ে সহায়তা করে।
# ✅ repr(object) ব্যবহার করলে __repr__ কল হয়।
# ✅ print(object) করলে __str__ না থাকলে __repr__ কল হয়।