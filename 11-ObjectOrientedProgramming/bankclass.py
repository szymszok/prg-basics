class bank:
    def __init__(self,account):
        self.account = account
        self.balance = 0

    def display(self):
        print(f'Bank Account No. : {self.account}')
        print(f'Balance: PLN {self.balance}')

    def deposit(self,money):
        self.balance += money
    
    def withdraw(self,money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("You don't have enought funds")
