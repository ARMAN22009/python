class Account:

    def __init__(self,bal,accno):
        self.balance=bal
        self.__accountno=accno #private attribute
       

    def debit(self,amount):
        self.balance=self.balance-amount
        print("Rs ", amount," was debited.")
        print("total balance is ",self.total_balance())

    def credit(self,amount):
        self.balance=self.balance+amount    
        print("Rs ",amount ,"was credited.")
        print("total balance is ",self.total_balance())

    def total_balance(self):
        return self.balance
print("Enter Balance and Account number.")
acc1=Account(int(input()),int(input()))

print("debitting account.")
acc1.debit(int(input()))

print("creditting account.")
acc1.credit(int(input()))

# print(acc1.accountno)  #account number will be displayed here which  should not be shared 
print(acc1.__accountno) #account nuber will not be displayed here as __ (double_underscore) is written at start


