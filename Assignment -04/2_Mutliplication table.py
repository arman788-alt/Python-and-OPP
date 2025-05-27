# Create a program that prints the multiplication table for any number entered by the user using a for loop.
# 2*1=2
# 2*2=4
# 2*3=6

num = int(input("Enter a number: "))
print(f"Mutliplcation of {num}")

for i in range(1,11):
    print(f"{num} * {i} = ",num*i)

