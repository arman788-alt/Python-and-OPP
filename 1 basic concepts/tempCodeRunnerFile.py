
def addition(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}\n')

def subsraction(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}\n')

def multiplication(num1, num2):
    result = num1 * num2
    print(f'{num1} * {num2} = {result}\n')

def division(num1, num2):
      if num2 == 0:
          print(f'Sorry zero is not divided by {num1}\n')
      else: 
          
        result = num1 /num2
        print(f'{num1} / {num2} = {result}\n')


    

while True:

    print('1 for addition')
    print('2 for subsraction')
    print('3 for multiplication')
    print('4 for division')
    print('Enter Q or q for Exit the calculation\n')
       

