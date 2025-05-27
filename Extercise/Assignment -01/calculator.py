# Perform basic arithmetic operations (addition, subtraction, multiplication, division).

def addition(num1,num2):

    result = num1+num2
    print(f"{num1} + {num2} = {result}")


def substraction(num1,num2):

    result = num1-num2
    print(f"{num1} - {num2} = {result}")



def multiplication(num1,num2):

    result = num1*num2
    print(f"{num1} * {num2} = {result}")


def divison(num1,num2):

    result = num1/num2
    print(f"{num1} / {num2} = {result}")





while True:
    
    print("What do you want to do?")
    print("1 for addition")
    print("2 for substraction")
    print("3 for multiplication")
    print("4 for addision")
    print("5 for break for calcualtion")

    choice = int(input("Choice anyone: "))
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))


    if choice == 1:

       addition(num1,num2)
    
    elif choice == 2:
        substraction(num1,num2)

    elif choice == 3:
        multiplication(num1,num2)
    
    elif choice == 4:
        if num2 == 0:
            print("sorry num2 is 0")
        else:
            divison(num1,num2)

    elif choice == 5:
        break
    
    else:
        print("invalid choice")





    






