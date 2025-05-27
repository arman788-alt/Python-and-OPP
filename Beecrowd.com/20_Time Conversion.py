second = int(input())

h = second//3600
reminder = second%3600

min = reminder//60
reminder = reminder%60

sec = reminder

print(f"{h}:{min}:{sec}")



