class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add(self, n, b):
        self.accounts[n] = b
    
    def trans(self, n, amt):
        if n in self.accounts:
            self.accounts[n] += amt
    
    def withdraw(self, n, money):
        if n in self.accounts:
            if self.accounts[n] >= money:
                self.accounts[n] -= money
            else:
                print("Insufficient balance.")
        else:
            print("Account does not exist.")
    
    def show(self):
        print(self.accounts)

b = Bank()

name = input("Enter account name: ")
balance = int(input("Enter initial balance: "))
b.add(name, balance)

print("After adding account:")
b.show()

amount = int(input("Enter amount to deposit: "))
b.trans(name, amount)

print("After deposit:")
b.show()

withdraw_amount = int(input("Enter amount to withdraw: "))
b.withdraw(name, withdraw_amount)

print("After withdrawal:")
b.show()
