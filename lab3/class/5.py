class bank_acc:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)

    def deposit(self):
        income = int(input('put money to deposit\n'))
        self.balance += income 
        print('current balance: {}'.format(self.balance))
    
    def withdraw(self):
        take_out = int(input('take out the sum\n'))
        if take_out > self.balance:
            print("You don't have enough money")
        else:
            self.balance -= take_out
            print('current balance: {}'.format(self.balance))

name, money = input().split()
one = bank_acc(name, money)
one.deposit()
one.withdraw()
