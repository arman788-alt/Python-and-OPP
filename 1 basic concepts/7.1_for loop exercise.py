# Q1. Code to implement Continue statement in for-loop

clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("socks")
print(f"Washing {paired_socks}")

# Output:
# Washing shirt
# Washing pants
# Washing towel
# Washing ['socks']

                                    

# Q2. Code to implement range function in for-loop

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")

# Output:
# Day 1: Run 3.0 miles
# Day 2: Run 3.5 miles
# Day 3: Run 4.0 miles
# Day 4: Run 4.5 miles
# Day 5: Run 5.0 miles
# Day 6: Run 5.5 miles
# Day 7: Run 6.0 miles
    

# Example 1: Iterating over a list
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
    
# output:
# apple
# banana
# cherry

# Example 2: Iterating over a string
# for char in 'Python':
#     print(char)

# output:
# P
# y
# t
# h
# o
# n

# Example 3: Using enumerate to get index and value
# for index, num in enumerate([10, 20, 30]):
#     print(f'Index {index}: {num}')

# output:
# Index 0: 10
# Index 1: 20
# Index 2: 30

# Example 4: Iterating over a dictionary
# person = {'name': 'John', 'age': 30}
# for key, value in person.items():
#     print(f'{key}: {value}')
# output:
# name: John
# age: 30



# Example: 5 Calculating sum of numbers in a list
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
    
#     total += num 
    
    
# print(f'Total sum: {total}')
