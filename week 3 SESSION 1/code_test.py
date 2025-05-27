lst = ["Empty" for _ in range(20)]
print(lst)



















# সিট ম্যাট্রিক্স তৈরি (6 rows, 5 columns)
# rows = 6
# cols = 5
# seats = [[0 for _ in range(cols)] for _ in range(rows)]

# # সিট প্রিন্ট ফাংশন
# def print_seats():
#     print("Seat Map:")
#     for i in range(rows):
#         for j in range(cols):
#             print(seats[i][j], end=" ")
#         print()

# # সিট বুকিং ফাংশন
# def book_seat():
#     row = int(input("Enter row number (0 to 5): "))
#     col = int(input("Enter column number (0 to 4): "))
    
#     if row < 0 or row >= rows or col < 0 or col >= cols:
#         print("❌ Invalid seat position!")
#     elif seats[row][col] == 1:
#         print("❌ Seat already booked!")
#     else:
#         seats[row][col] = 1
#         print("✅ Seat booked successfully!")

# # মেইন লুপ
# while True:
#     print_seats()
#     choice = input("Do you want to book a seat? (yes/no): ")
#     if choice.lower() == "yes":
#         book_seat()
#     else:
#         print("Thank you!")
#         break




