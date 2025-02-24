class account:
    def __init__(self,bln,acn):
        self.balance=bln
        self.account_no=acn
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("BDT. ",amount,"was debited")
        print("Total balance= ",self.get_balance())
    #credit method
    def credit(self,amount):
        self.balance+=amount
        print("BDT. ",amount,"was credited")
        print("Total balance= ",self.get_balance())
    def get_balance(self):
        return self.balance


acc1=account(10000,"12345")
acc1.debit(99)
acc1.credit(550)
acc1.credit(40000)
print("Balance=",acc1.balance,"Account No=",acc1.account_no)