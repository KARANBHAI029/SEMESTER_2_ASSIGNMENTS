class BankAccount:
    def __init__(self, num, bal):
        self.num = num
        self.bal = bal
    
    def dep(self, amt):
        self.bal += amt
    
    def wth(self, amt):
        if amt <= self.bal:
            self.bal -= amt
    
    def show(self):
        print(self.num, self.bal)

ba = BankAccount("123", 5000)
ba.dep(1000)
ba.wth(2000)
ba.show()
