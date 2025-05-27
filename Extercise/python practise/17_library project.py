class User:
    def __init__(self, id,name, password):
        self.name = name 
        self.id = id
        self.password = password
        self.borrowBooks = []
        self.returnBooks = []




class Book:
    def __init__(self,catagory,name,id,quan):
        self.catagory = catagory
        self.name = name
        self.id = id
        self.quan = quan


class Library:
    def __init__(self,owner,name):
        self.owner = owner
        self.name = name
        self.Books = []
        self.User = []

    
    def addUser(self,id,name, password):
        user = User(id,name,password)
        self.User.append(user)
        print(f"{name} is added")
        return user
    

    def addBook(self,catagory,name,id,quan):
        book = Book(catagory,name,id,quan)
        self.Books.append(book)
        print(f"{book.name} is added")
    

    def borrowBooks(self,user,id):
        for book in self.Books:
            if book.id==id:
                if book in user.borrowBooks:
                    print(f"{book.name} is already borrowed")
                    return
                
                elif book.quan<1:
                    print(f"{book.name} no copy available")
                    return
                else:
                    book.quan-=1
                    user.borrowBooks.append(book)
                    print(f"{book.name} borrowed Successfully")
                    return
        print(f"\tbook is not found")
    

    def returnBooks(self,user,id):
        for book in self.Books:
            if book.id == id:
                if book in user.borrowBooks:
                    user.borrowBooks.remove(book)
                    user.returnBooks.append(book)
                    print(f"{book.name} rerturn succesfully")
                    return
        


                

pl = Library("Arman", "phoitron Library")
admin = pl.addUser(1,"admin", "admin")

sajjad = pl.addUser(2,"sajjad", "sajjad")
pybook = pl.addBook("sci-fiction", "math",101,20)



currentUser = admin


while True:

    if currentUser == None:
        print("Longin or Registration: L/R")
        option = input()
        if option=='R':
            id = int(input("\tEnter your id:"))
            name = (input("\tEnter your name:"))
            password=input("\tEnter your password:")
            user = pl.addUser(id,name,password)
            currentUser = user
        

        else:
            id = int(input("\tEnter your id:"))
            password=input("\tEnter your password:")

            flag = False

            for user in pl.User:
                if user.id == id and user.password == password:
                    flag=True
                    currentUser=user
                    break
            
            if flag==False:
                print("User not found")


    else:

        if currentUser.name=="admin":
            print("Option: ") 
            print("1.Book add") 
            print("2.show book") 
            print("3.show user")
            print("4.Logout")

            choice = input("Enter your choice: ") 
            
            if choice=="1":
                cata = input("\tEnter book catagory:")
                name = input("\tEnter your book name:")
                id=int(input("\tEnter book id: "))
                quan = int(input("\tEnter book quantity:"))

                pl.addBook(cata,name,id,quan)
            
            elif choice=="2":
                for book in pl.Books:
                    print(f"{book.name} {book.id} {book.quan}")
            
            elif choice=="3":
                for user in pl.User:
                    print(f"{user.name} {user.id}")
            
            

            
            elif choice=="4":
                currentUser=None
        


        else:
            #normal user
            print("Option:")
            print("1 : Borrow Book")
            print("2 : Return Book")
            print("3 : Show Books")
            print("4 : Show Borrowed Books")
            print("5 : Show Returned Books")
            print("6 : Logout")

            choice = input("Enter your choice:")

            if choice =="1":
                id=int(input("Enter id:"))
                pl.borrowBooks(currentUser,id)
            
            elif choice=="2":
                id=int(input("Enter id:"))
                pl.returnBooks(currentUser,id)
            
            elif choice=="3":
                for book in pl.Books:
                    if book in currentUser.borrowBooks:
                        print(f"{book.name} book is Reading Now-----")
                    elif book in currentUser.returnBooks:
                            print(f"{book.name} book is already Read-----")
                    else:
                        print(f"{book.name} book is not Reading-----")
                
            elif choice=="4":

                
                for book in currentUser.borrowBooks:
                    print(f"{book.name}, {book.id}")
            
            elif choice=="5":
                for book in currentUser.returnBooks:
                    print(f"{book.name}, {book.id}")

                    



            
            elif choice=="6":
                currentUser=None


            



            






















    



