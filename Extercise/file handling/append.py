with open("newFile.txt", "a") as file:
    file.write("first ")
    file.close()

with open("newFile.txt", "a") as file:
    file.write("arman ")
    file.close()


# with open("newFile.txt", "r") as file:
#     content = file.read()
#     print(content)


import os
os.remove("newFile.txt")


with open("newFile.txt", "r") as file:
    content = file.read()
    print(content)





