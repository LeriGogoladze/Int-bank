from custom_error import InvalidBalanceException
from validation import account_number_gen

class Account:  
    def __init__(self,balance):           
        self.validate_balance(balance) 
        self.balance = balance
        self.interest_rate = 8.2
        self.account_number = self.generate_account_number() 

    def validate_balance(self, balance):
        if balance > 100: 
            raise InvalidBalanceException("Starting balance cannot exceed {} GEL")
    def generate_account_number(self): 
        return account_number_gen()




