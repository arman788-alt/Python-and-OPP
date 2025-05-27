num = int(input())


if num<2:
    print("Not prime number")

else:
    flag = True
    for i in range(2,num):
          
          if num%i==0:
            flag = False
            break
    

if flag:
    print("Prime number")  

else:
    print("Not prime number")

