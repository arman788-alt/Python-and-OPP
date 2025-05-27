# Count the number of vowels in a string.

str = input("Enter string: ")
count = 0

for i in str:

    if i == 'i' or i =='I' or i=='a' or i=='A' or i=='e' or i=='E' or i=='o' or  i=='O' or i=='u' or i=='U':
        count+=1
print(f"Total vowel count: {count}")

