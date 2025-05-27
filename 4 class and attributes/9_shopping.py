#  Shopping checkout and price calculations

class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = [] #instance attribute

    def add_to_cart(self, item, price, quantity):

        product = {'item': item, 'price': price, 'quantity': quantity} 
        self.cart.append(product)
        
    
    def remove_item(self, item_name):
        for item in self.cart:
            if item['item'] == item_name:
                self.cart.remove(item)
                break # Break after removing the item to avoid modifying the list while iterating

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            #print(item)
            total += item['price'] * item['quantity'] #?
        print('total price', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money: {extra}')

swapan = Shopping('Alan Swapon')
swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice', 50, 5)

print(swapan.cart)
swapan.checkout(600)
swapan.checkout(1600)

# delete item
swapan.remove_item('dim')
swapan.remove_item('rice')

# print
print(swapan.cart)








# এখানে আমরা এড টু কার্ট এবং চেকআউট ফাংশনালিটি গুলো আমরা মেথড এর মাধ্যমে এড করছি এবং চেকয়াউট মেথড এর মধ্যে total বিলটা আমরা কার্ট এর উপর লুপ চালিয়ে সবগুলো প্রোডাক্ট এর প্রাইস এড করে বের করছি এবং সেই অনুযায়ী অন্যান্য অপারেশন করা হয়েছে

#homework
# এখানে তোমার কাজ হচ্ছে remove_item() ফাংশনালিটিটা এড করা যেখানে একটা প্রোডাক্ট এর নাম দিলে সেটাকে কার্ট থেকে রিমুভ করে দিব।