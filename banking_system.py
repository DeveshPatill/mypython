class Account():
    def __init__(self):
        pass

    def __init__(self,name,balance,account_no):
        self.name=name
        self.balance=balance
        self.account_no=account_no

    def credit(self,amount):
        self.balance += amount
        print("rs. ",amount,"was credited from your account")
        print("total balance = ",self.finalbalance())

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited from your account")
        print("total balance = ",self.finalbalance())


    def finalbalance(self):
        return self.balance

acc=Account("devesh",10000,1234)
print(acc.name,acc.balance,acc.account_no)
acc.credit(20000)
acc.debit(1000)