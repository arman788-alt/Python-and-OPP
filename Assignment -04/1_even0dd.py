# Write a program that asks the user for a number and checks whether it is odd or even.


num = input("Enter a Number: ")
num = int(num)


if num%2==0:
    print(f"{num} is Even")

else:      
        print(f"{num} is Odd")