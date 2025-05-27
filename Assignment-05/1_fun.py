# Create a function that takes two numbers and returns their sum, difference, and product.


def fun(num1,num2):

    sum = num1+num2
    dif = num1-num2
    product = num1*num2

    return sum,dif,product



n1 = int(input("Enter a number1:"))
n2 = int(input("Enter a number2:"))

sum,dif,product = fun(n1,n2)
print(sum,dif,product)