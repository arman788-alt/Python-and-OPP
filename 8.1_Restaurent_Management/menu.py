# 3
class Menu:
    def __init__(self):
        self.items = []  # items er database

    def add_menu_item(self, item): #ekhane item holo ekti object(footItem class): jekhane item_name, price, quantity thakbe.
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)

        if item: # or: item is not None
            self.items.remove(item)
            print(f"{item.name} Item deleted")
        else:
            print("item not found")

    def show_menu(self):
        print("*****Menu*****")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
