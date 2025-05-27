
# create file
with open("Example.txt", "w") as file:
    file.write("My name is arman")
    file.close()


# Write within file
with open("Example.txt", "w") as file:
    file.write("My name is Arafat.")
    file.write("I am student of cse This file is for testing purposes.Good Luck!.")
    file.close()

# Read from the file
with open("Example.txt", "r") as file:

    # print(file.read(2))
    print(file.read())


# write multiple line in file
lines = ["Hello", "My name is Arman", "I am study at northern University"]
with open("Example.txt", "w") as file:

    for line in lines:
        file.write(line + "\n")


with open("Example.txt", "r") as file:

    # print(file.read(2))
    # print(file.readline())
    print(file.read())

print("<<---------------------------------->>")

# print line by loop:
with open("Example.txt", "r") as file:

    for line in file:
        print(line)
    



   


        








