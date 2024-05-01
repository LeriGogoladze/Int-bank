from user import check_iban_format as check_iban
from Variablies import DB

def calculate_loan(iban):
  
    current_user = None

    ok,error = check_iban(iban)
    if ok:
        for user in DB:
            if iban in user.values():
                current_user = user
                break   
        if not current_user:
            print(f"user with IBAN- '{iban}' not found!!")
        else:
            loan_amount = input("Enter loan amount: ")
            if not loan_amount.isdigit():
                print("Loan amount must be digit not string!")
            else:
                interest_rate = current_user["loan"]
                total_interest = int(loan_amount) * interest_rate/100
                print(f"Total interest per year is- {total_interest},total pay back - {int(loan_amount) + total_interest}")
                yes_no = input("Would you take a loan? Ente Y/N:")
                if yes_no.upper() == 'Y':
                    current_user["balance"] += int(loan_amount)  
                    print(f"Your balance is filled with {int(loan_amount)} GEL")
    else:
        print(error)
