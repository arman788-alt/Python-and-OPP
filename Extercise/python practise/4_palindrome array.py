N = int(input())
ar = []

for i in range(N):
    A = list(map(int,input().split()))
    ar.append(A)

    

rev = ar[::-1]
if ar == rev:
    print("YES")
else:
    print("NO")