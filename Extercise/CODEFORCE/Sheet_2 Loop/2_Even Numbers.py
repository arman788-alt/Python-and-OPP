
n = int(input())

flag = False
for i in range(1,n+1):
    if i%2==0:
        print(i)
        flag = True

if flag == False:
    print(-1)


    
