text = input()

text = text.split(" ")


count_word = {}

for word in text:
    if word in count_word:
        count_word[word]+=1
    else:
        count_word[word]=1

print(count_word)


