from db import db,add_customer_in_db
from validation import check_iban_format

class Customer:
    def __init__ (self,name,surname,account):
        self.name = name
        self.surname = surname
        self.account = account.account_number
        self.balance = account.balance
        self.interest_rate = account.interest_rate 

    def add_new_customer_in_db(self,customer):
        add_customer_in_db(customer)
      
    def get_account_info(iban):
        current_user = None
        ok,error = check_iban_format(iban)
        if ok:
            for user in db:
                if iban in user.values():
                    current_user = user
                    break   
            if not current_user:
                print(f"user with IBAN- '{iban}' not found!!")
            else:
                print(f"user name is '{current_user["name"]}',surname - '{current_user["surname"]}, balance- '{current_user["balance"]}''")  
        else:
            print(error)


    
