# simple function
# single return 
# return nothing means none return
# multiple return
# touple return
# list return
# dic return
# *args
# **kwrsgs



# def say_hello():
#     print("Hello")


# result = say_hello()
# print(result)


# def fun(name):
#     print(f"name: {name}")

# fun('Arman')


# def fun(name, Id=0):
#     # print(f"Name: {name} Id: {Id}")
#     return f"Name: {name} Id: {Id}"


# result = fun("Arman", 430)
# print(result)


# def all_name(*names):
#     # print(len(name))

#     for name in names:
#         print(f"Hello {name}")
#     return names

# result = all_name('Arman','Sajjad','akash')
# print(result)




# def student(**info):

#     for key,value in info.items():
#         print(f"{key}: {value}")
#     return info


# result = student(name='Arman', Id= 430, Section='E')
# print(result)



# def student(*info):
#     even_sum=0
#     odd_sum=0
#     for i in info:
#         if i%2==0:
#             even_sum+=i
#         else:
#             odd_sum+=i
#     return even_sum,odd_sum

    

# even,odd = student(1,2,3,4,5,6)
# print(even,odd)




# def student(info):

#     print(type(info))

#     return max(info),min(info)

    

# max,min = student([1,2,3,4,5,6])
# print(max,min)


# def student(info):


#     return tuple(info)

    

# r = student([1,2,3,4,5,6])
# print(r)


# balance = 1000
# def fun():

#     global balance
#     balance = balance - 200
#     print(balance)

# fun()

    








