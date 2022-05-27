class Account:
    name="Absa"
    def __init__(self,account_number,account_name,account_pin,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.account_pin=account_pin
        self.balance=balance
    def withdraw(self,amount):
        current_balance=self.balance-amount
        return f"Dear {self.account_name},your new balance is{current_balance}"

    
    def deposit(self,amount2):
        current_balance2=self.balance+amount2
        return f"Dear {self.account_name}, your new balance is{current_balance2}"

    
    
        
