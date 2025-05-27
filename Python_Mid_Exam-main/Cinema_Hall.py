
# from chatgpt
class Star_Cinema:
    __hall_list = []  # private class attribute

    @classmethod
    def entry_hall(cls, hall_obj):
        cls.__hall_list.append(hall_obj)

    @classmethod
    def get_halls(cls):
        return cls.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().entry_hall(self)  # insert hall into Star_Cinema's hall list
        self.__seats = {}  # private
        self.__show_list = []  # private
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seats

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Invalid seat position ({row}, {col})!")
            elif self.__seats[show_id][row][col] == 1:
                print(f"Seat ({row}, {col}) already booked!")
            else:
                self.__seats[show_id][row][col] = 1
                print(f" Seat ({row}, {col}) booked successfully!")

    def view_show_list(self):
        print("\nRunning Shows:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID!")
            return

        print(f"\nAvailable seats for show ID {show_id}:")
        for i in range(self.__rows):  
            for j in range(self.__cols):
                if self.__seats[show_id][i][j] == 0:
                    

                    print(f"({i},{j})", end=" ")
            print()


# Sample usage
# if __name__ == '__main__':
hall1 = Hall(5, 5, 101)
hall1.entry_show("111", "Avengers", "12:00 PM")
hall1.entry_show("222", "Inception", "3:00 PM")

while True:
        
        print("\nStar Cinema System")
        print("1. View all shows")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            hall1.view_show_list()

        elif choice == '2':
            show_id = input("Enter show ID: ")
            hall1.view_available_seats(show_id)

        elif choice == '3':
            show_id = input("Enter show ID: ")
            n = int(input("How many seats to book? "))
            seats_to_book = []
            for _ in range(n):
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                seats_to_book.append((row, col))
            hall1.book_seats(show_id, seats_to_book)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")




# class Star_Cinema:
#     _hall_list = [] 

#     def entry_hall(self, hall):
#         self._hall_list.append(hall)


# class Hall(Star_Cinema):
#     def __init__(self, rows, cols, hall_no):
#         self.__seats = {}
#         self.__show_list = []
#         self._rows = rows
#         self._cols = cols
#         self.hall_no = hall_no
#         self.entry_hall(self)


#     def entry_show(self, id, movie_name, time):
#         show_info = (id,movie_name,time)
#         self.__show_list.append(show_info)
#         seatMat = [[0 for i in range(self._cols)] for j in range(self._rows)]
#         self.__seats[id] = seatMat



#     def view_available_seats(self, id):
#         show_exists = False
#         for show in self.__show_list:
#             if show[0] == id:
#                 show_exists = True
#                 print(f"!!----- Available Seats for Show -- {id}")
#                 for row in self.__seats[id]:
#                     for seat in row:
#                         print("0" if seat == 0 else "1", end=" ")
#                     print()
#                 break

#         if not show_exists:
#             print("Show ID not found.")



#     def book_seats(self, id, seat_list):
#         show_exists = False
#         for show in self.__show_list:
#             if show[0] == id:
#                 show_exists = True
#                 for row, col in seat_list:
#                     if row < 0 or row > self._rows or col < 0 or col > self._cols:
#                         print(f"Invalid seat [{row}, {col}]. Seat is out of range.")
#                     elif self.__seats[id][row][col] == 0:
#                         self.__seats[id][row][col] = 1
#                         print(f"Seat [{row}, {col}] booked successfully.")
#                     else:
#                         print(f"Seat {row}, {col} is already booked.")
#                 break

#         if not show_exists:
#             print("Show ID not found.")


   
#     def view_show_list(self):
#         print(f"!!------Show List for Hall :{self.hall_no}-------!!")
#         cnt=1
#         for show in self.__show_list:
#             print(f"\n\t----Show : {cnt}----\n Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")
#             cnt+=1
 

# row, col = map(int, input("Enter Row And Col: ").split())
# hallno = int(input("Enter hall no : "))
# hall = Hall(row, col, hallno)

# while True:

#     print("!!-----Cinema Booking System------------!!")
#     print("1.Add Show Information")
#     print("2.View all shows today")
#     print("3.Book seat for a show")
#     print("4.View available seats for a show")
#     print("5. Exit")


#     op = int(input("Enter Option: "))

#     if op == 1:
#                 h_id = input("Enter the hall id : ")
#                 movie = input("Enter the movie name : ")
#                 time = input("Enter the time of movie : ")
#                 hall.entry_show(h_id,movie,time)
#                 print()
#                 print("Add Show Information done.")
    

#     elif op == 2:
#         print("!!------- View Show Data --------!!")
#         for show in Star_Cinema._hall_list:
#             show.view_show_list()  

#     elif op == 3:
#         print(" !!---Book seat for a show---!!")
#         show_id = input("Enter the ID of the show: ")
#         num_seat = int(input("Enter the number of seats to book: "))
#         seatBook = []
#         for _ in range(num_seat):
#             row = int(input("Enter the row of the seat: "))
#             col = int(input("Enter the column of the seat: "))
#             seatBook.append((row, col))
#         hall.book_seats(show_id, seatBook)
              
        

#     elif op == 4:
#         print("!!----View available seats for a show ----!!")
#         show_id = input("Enter the show id: ")
#         hall.view_available_seats(show_id)


#     elif op == 5:
#         break

#     else:
#         print("Inavalid Option!")

