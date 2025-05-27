class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.max_withdraw = 100000
        self.min_withdraw = 100
    
    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):

          if amount >0:
            self.balance+=amount
            print(f"Deposite your {amount} Tk now your total balance: {self.get_balance()}")
        
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Sorry you cannot less then {self.min_withdraw} TK")
        elif amount > self.max_withdraw:
            print(f"sorry you cannot more then {self.max_withdraw} TK")


dbl = Bank(10000000)
print(dbl.get_balance())
dbl.deposite(120)
dbl.deposite(40)
dbl.withdraw(10)
dbl.withdraw(9000)
dbl.withdraw(10000000)










