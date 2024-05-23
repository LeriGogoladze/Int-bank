db = []

def add_customer_in_db(customer): 
    
    db.append({"iban": customer.account,
                "name": customer.name,
                "surname": customer.surname,
                "balance": customer.balance,
                "interest_rate": customer.interest_rate})
    
    print(db)

def get_customer_by_iban(iban): 
    for user in db:
        if iban in user.values():
            return user
        else:
            return None
        
def add_balance(user_iban):
        amount = input("Enter the amount you want to add to your balance: ")
        if not amount.isdigit():
            raise Exception("You must Enter numerical value!")
        for i in db:
            if user_iban in i.values():
                i["balance"] += int(amount)    
        print(db)