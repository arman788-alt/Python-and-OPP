num = (input())


sum_of_digit = 0

for i in num:
    sum_of_digit+= int(i)**3


if int(num) == sum_of_digit:
    print("Armstrong number")
else:
    print("Not Armstrong number")


    