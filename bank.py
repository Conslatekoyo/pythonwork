
from datetime import datetime
from itertools import count



class Account():
    name="Absa"
    def __init__(self,account_number,account_name,account_pin):
        self.account_number=account_number
        self.account_name=account_name
        self.account_pin=account_pin
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.date=datetime.now().strftime("%x %X")
        self.combinestatements=[]
        self.loan=0

    
    
    def deposit(self,amount):
        empty={'date':self.date,'amount':amount,'narration':'Deposit'}
        self.balance+=amount
        self.deposits.append(amount)
        print(self.deposits)
        print(empty)
        self.combinestatements.append(empty)
        print(self.combinestatements)
        return f"Dear {self.account_name}, your new balance is {self.balance}"

    def withdraw(self,amount):
        empty_two={'date':self.date,'amount':amount,'narration':'Withrawal'}
        if amount>self.balance:
            return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            remnant=self.balance-100
            self.withdrawals.append(amount)
            print(self.withdrawals)
            print(empty_two)
            self.combinestatements.append(empty_two)
            print(self.combinestatements)
            return f"Hello {self.name} you have withdrawn {amount}.Your new balance is {remnant}"


    def deposit_statements(self):
       for deposit in self.deposits:
           print(deposit ) 
       
    def deposit_withdrawals(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)

    def full_statement(self):
        for item in self.combinestatements:
            date= item['date']
            amount=item['amount']
            narration=item['narration']
            print(f"{date}_________{narration}______{amount}")
    def borrow(self,amount):
        count=sum(self.deposits)
        fuliza=(1/3)*count
        interest=(3/100)*amount
        if len(self.deposits)<10:
            return f"You ought to make more than ten deposits"
        elif amount<100:
            return f"You can only access a loan of more than sh 100"
        elif amount>fuliza:
            return f"You cannot access a loan greater than your balance"
        elif self.loan>0:
            return f"Pay your loan before you get to access a loan"
        else:
            self.loan+=amount
            self.loan+=interest
            return f"You have successfully borrowed {amount} and your interest is {interest} and your loan is {self.loan}"

    def loan_repayment(self,amount):
        if amount<self.loan:
            self.loan-=amount
            return f"You have paid {amount} for your loan and your balance is{self.loan}"
        elif amount>self.loan:
            amount-=self.loan
            self.balance+=amount
            return f"You have paid {amount} for your loan and your account balance is {self.balance}"

    def transfer(self,amount,account2_name):
        if amount>=self.balance:
            return "Sorry, you have insufficient balance"
        elif amount<=0:
            return "Sorry, your amount is invalid"
        else:
            self.balance-=amount
            return f"You have transfered {amount} to {account2_name} and your balance is {self.balance} "
        


        
            








        
    
    

    
    
    
