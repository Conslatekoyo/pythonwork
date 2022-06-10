class Account:
    name="Absa"
    def __init__(self,account_number,account_name,account_pin):
        self.account_number=account_number
        self.account_name=account_name
        self.account_pin=account_pin
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]

    
    
    def deposit(self,amount):
        self.balance+=amount
        self.deposits.append(amount)
        print(self.deposits)
        return f"Dear {self.account_name}, your new balance is {self.balance}"

    def withdraw(self,amount):
        if amount>self.balance:
            return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            remnant=self.balance-100
            self.withdrawals.append(amount)
            print(self.withdrawals)
            return f"Hello {self.name} you have withdrawn {amount}.Your new balance is {remnant}"


    def deposit_statements(self):
       for deposit in self.deposits:
           print(deposit ) 
       
    def deposit_withdrawals(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)
    
    

    
    
        
