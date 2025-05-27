# N = int(input())
# ar = []

# for i in range(N):
#     A = list(map(int,input().split()))
#     ar.append(A)

# sum = 0
# for  _,val in enumerate(ar):
#     sum += val

# print(sum)
    

N = int(input())
ar = []

for i in range(N):
    A = list(map(int, input().split()))
    ar.append(A)

total_sum = 0
for sublist in ar:
    for val in sublist:
        total_sum += val

print(total_sum)
