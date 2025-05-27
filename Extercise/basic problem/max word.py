sentance = input().split(" ")

BigWord = sentance[0]

for i in sentance:

    if len(i)>len(BigWord):
        BigWord = i

print(f"BigWord in the sentance: {BigWord}")


