banknote = int(input())

print(banknote)

for i in [100,50,20,10,5,2,1]:
    print(f"{banknote//i} nota(s) de R$ {i},00")
    banknote = banknote%i










# 10% error this problem::
    
# banknote = int(input())

# hundred = (banknote//100)
# reminder = (banknote%100)

# fifty = (reminder//50)
# reminder =(reminder%50)



# twenty = (reminder//20)
# reminder =(reminder%20)

# ten = (reminder//10)
# reminder =(reminder%10)

# five = (reminder//5)
# reminder =(reminder%5)

# two = (reminder//2)
# reminder =(reminder%2)

# one = (reminder//1)
# reminder =(reminder%1)

# print(banknote)
# print(f"{hundred} nota(s) de R$ 100,00")
# print(f"{fifty} nota(s) de R$ 100,00")
# print(f"{twenty} nota(s) de R$ 100,00")
# print(f"{ten} nota(s) de R$ 100,00")
# print(f"{five} nota(s) de R$ 100,00")
# print(f"{two} nota(s) de R$ 100,00")
# print(f"{one} nota(s) de R$ 100,00")















