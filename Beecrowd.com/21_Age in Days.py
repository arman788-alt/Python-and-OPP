num = int(input())

year = num//365

reminder = num%365

month = reminder//30

reminder = reminder%30

days = reminder

print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{days} dia(s)")




