

str = input()

# dictionary
char_count = {}

for char in str:
    if char in char_count.keys():
        char_count[char]+=1
    

    else:
        char_count[char] = 1



print(char_count)




