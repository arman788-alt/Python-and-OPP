

char = input("character input: ").lower()

# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#     print(f"Vowel: {char}")

# else:
#     print(f"consonent: {char}")


if char in 'aeiou':
        print(f"Vowel: {char}")
else:
    print(f"consonent: {char}")

