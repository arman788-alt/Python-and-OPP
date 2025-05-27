
# try:
#     result = 45/"hello"
#     print(result)

# except Exception as e:
#     print(e)

# else:
#     print(f"final result is: {result}")
# finally:
#     print("No mater what either error or no error finally block will be execute")



try:

    with open("text.txt",'r') as file:
        content = file.read()
        print(content)


except Exception as e:

    print(e)

else:
    print(f"final result is: {content}")
finally:
    print("No mater what either error or no error finally block will be execute")