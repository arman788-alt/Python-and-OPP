# Write a function that checks whether a given string is a palindrome.


def palindrome(str):
    reverse_str = str[::-1]

    if str==reverse_str:
        print(f"This {str} is palindrome")
    else:

        print(f"This {str} is Not palindrome")


string = input("Enter a string: ")

palindrome(string)






