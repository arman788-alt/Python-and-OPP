# Dictionary and Dictionary methods in python
# Dictionary মিউটেবল

numbers = [12, 56 , 98, 78, 56, 12, 26, 98]
person1 = ['Kala Chan', 'kalipur', 23, 'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set



# dictionary_Name : {key: value, key: value, key: value}

# Creating a dictonary
person = {'name': 'Kala Pakhi', 'address': 'Kaliapur', 'age': 23, 'job': 'facebooker'}
print(person)

#Accesing item
x = person['age']
print('age :', x)
print(person['job'])

#dictionary key, value method
print(person.keys()) 
print(person.values())

# adding new item
person['language'] = 'python'

# changing an item's value
person['name'] = 'sada pakhi'

# removing an item value
# pop method
person.pop('job')

# or del method
del person['age']
print(person)



employees = {
    101: {"name": "Karim", "position": "Manager", "salary": 50000},
    102: {"name": "Rahim", "position": "Developer", "salary": 40000},
    103: {"name": "Jarin", "position": "Designer", "salary": 35000}
}

print(employees[101])
print(employees[101]['salary'])
employees[101]['salary'] = 70
print(employees[101])






# Nested dictionary :
# ekta dictionary er bitor arekta dictionary create korle take nested dictionary bole..
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# special dictionary looping
for key, value in person.items():
    print('Key: ', key,  'Value: ', value)


# subject = 'Bangla'
# teacher = 'Abul miaa'

# dict = {}
# dict[subject] = teacher
# print(dict)



# EXAMPLE: 
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127 
#tel{'jack': 4098, 'sape': 4139, 'guido': 4127}
    
# tel['jack']
# 4098
    
# del tel['sape']
# tel['irv'] = 4127
# tel {'jack': 4098, 'guido': 4127, 'irv': 4127}
    
# list(tel)
# ['jack', 'guido', 'irv']
    
# sorted(tel)
# ['guido', 'irv', 'jack']
    
# 'guido' in tel
# True
# 'jack' not in tel
# False





# ই মডিউলে আমরা পাইথন ডিকশনারি সম্পর্কে জানব।  
# ডিকশনারি হলো key এবং value জোড়া হিসেবে ডেটা  ম্যানেজ করার উপায়। 

# myDictionary = {'name':'Ratin','age':27,'courses':['Database','Python','Django']}

# Dictionary মিউটেবল। ডিকশনারি থেকে ডেটা এক্সেস করার উপায়-
# print(myDictionary['name'])
    
    
# ডিকশনারি কে নিচের মত করে ইটারেট করা যাবে-
# myDictionary={'name':'Ratin','age':27, 'courses':['Database','Python','Django']}
    
# for key,val in myDictionary.items():
#     print(key,val)


# অবশ্য আমরা চাইলে ইটারেট করার সময় key এভয়েড করতে পারি -
# ডিকশনারিতে থাকা সবগুলো কী বা ভ্যালু আমরা পেতে চাইলে keys() , values() ফাংশন ব্যবহার করতে পারি।


