# Error handling
# Types of Error:
# 1.compile time Error: syntax error 
# 2.logical Error: Logical error হল এমন ভুল, যেখানে কোড ঠিকভাবে চলে কিন্তু ভুল ফলাফল দেয়।
# 3.Run time Error: Run time error হচ্ছে প্রোগ্রাম চালানোর সময় ঘটে যাওয়া ভুল।
# Example:
# a = 5
# b = 0
# print(a/b)


# Exception Handling কী?
# প্রোগ্রাম চলাকালীন সময়ে যদি কোনো Error (ভুল) হয়, তখন Python সেটিকে Exception বলে। যদি এই Exception গুলো আমরা না সামলাই, তাহলে প্রোগ্রাম ক্র্যাশ করে যায়।

# ✅ Exception Handling ব্যবহার করে আমরা এই Error গুলো সুন্দরভাবে ধরে ফেলতে পারি এবং ইউজারকে একটি বোঝার মতো বার্তা দেখাতে পারি।






# Summary: Execution korar try koro try block er bitor, ar nah parle mane error ashle except block er bitor asho.


# try:
#     # এখানে এমন কোড থাকবে যেটায় ভুল (error) হতে পারে
# except:
    # যদি উপরের try ব্লকে কোনো ভুল হয়, তাহলে এই অংশ চালানো হবে



# Example:1 Zero Division Error
# try:
#     result = 10 / 0
#     print(result)
# except:
#     print("Wrong। You can't devide by zero")





# Example:2 User Input Handling
# try:
#     num = int(input("Enter A number: "))
#     print("You given:", num)
# except:
#     print("Invalid input! Please enter numbers only.।")






# Example :3
# try:
#     # result = 45/0
#     result = 45/5
# except:
#     print('error happened')
# finally:
#     print('finally here')
# print('Done')





# Example:4 finally ব্লকে এমন কোড রাখা হয় যেটা সবসময় চালানো হবে, ভুল হোক বা না হোক।

# try:
#     x = int(input("Enter A number: "))
# except:
#     print("Wrong input!")
# finally:
#     print("This line will always run.")

# print("done")



# Example:5

# while True:
    
#     try: 
       
#        num1 = int(input("Enter number1: "))
#        num2 = int(input("Enter number2: "))
#        result = num1/num2
#        print(result)
#     except Exception as e:
#         print(f"Actual/specific Error: {e}")
#     finally:
#        print("This line will always run.")

#     print("\nMade by Arman\n")




# Example:6 নির্দিষ্ট Error ধরো by custom exception.
try:
    print("Open")
    a = int(input("Enter A number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("result:", result)

    num2 = int(input("Enter a Number: "))
    print(num2)

  
except ZeroDivisionError as e:
    print("Error: Cannot divide by 0!",e)

except ValueError as e:
    print("Incorrect: Please enter the correct number.।",e)

except Exception as e:
    print(e)

finally:
    print("Closed")

print("made by inception BD")
























