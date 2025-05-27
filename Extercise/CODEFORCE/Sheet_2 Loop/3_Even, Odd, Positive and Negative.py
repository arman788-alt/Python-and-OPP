
n = int(input())

even = 0
odd = 0
positive = 0
negative = 0


for i in range(0,n):

    val = int(input())
    if val%2==0:
        even+=1
    if val%2==1:
        odd+=1
    if val>0:
        positive+=1
    if val<0:
        negative+=1



print("Even: ",even)
print("Odd: ",odd)
print("Positive: ",positive)
print("Negative: ",negative)