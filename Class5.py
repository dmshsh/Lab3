class bankacc:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,sum):
        self.balance+=sum
    def withdraw(self,sum):
        if sum>self.balance:
            print("Impossible")
        else:
            self.balance-=sum
acc=bankacc("bro",1000)
acc.deposit(123)
acc.withdraw(12)
print(acc.balance)    