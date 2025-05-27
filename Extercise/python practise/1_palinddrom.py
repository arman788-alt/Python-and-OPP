# Read the input number as a string
N = input().strip()

# Reverse the string and convert it back to an integer to remove leading zeroes
reversed_N = int(N[::-1])

# Print the reversed number
print(reversed_N)

# Check if the original number is a palindrome and print the result
if N == N[::-1]:
    print("YES")
else:
    print("NO")
