# Use a while loop to calculate the sum of all numbers from 1 to 100.

# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)


sum = 0
i = 1
while True:
    sum = sum + i
    if i==100:
        break
    
    i=i+1
    
print(sum)