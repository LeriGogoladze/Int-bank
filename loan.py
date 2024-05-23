from validation import check_iban_format as check_iban
from db import db
import csv

class Loan:
    def __init__(self) -> None:
        pass
    
    def calculate_loan(iban):

        current_user = None

        ok,error = check_iban(iban)
        if ok:
            for user in db:
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
                    interest_rate = current_user["interest_rate"]
                    total_interest = int(loan_amount) * interest_rate/100
                    print(f"Total interest per year is- {total_interest},total pay back - {int(loan_amount) + total_interest}")
                    yes_no = input("Would you take a loan? Ente Y/N:")
                    if yes_no.upper() == 'Y':
                        current_user["balance"] += int(loan_amount)  
                        print(f"Your balance is filled with {int(loan_amount)} GEL")
                        
                        #calculates loan schedule per month and generates csv file
                        calculate_payments(12,int(loan_amount),interest_rate)
                        print("loan schedule file is generated")
        else:
            print(error)

def calculate_payments(period_in_months,loan,interest):

    if interest <= 0:
        print("Interest rate must be more than 0 !")
        return

    beginning_balance = loan	
    ending_balance = 0
    monthly_intersest = interest/100/period_in_months

    data_list = [["Month", "Beginning Balance", "Interest","Principal","Ending Balance"]]

    for month in range(1,period_in_months+1):   
        row_list = []
        
        monthly_payment = loan * (monthly_intersest*(1+monthly_intersest)**period_in_months)/((1+monthly_intersest)**period_in_months-1)
        Interest_amount = beginning_balance*monthly_intersest
        principal = monthly_payment - beginning_balance*monthly_intersest
        ending_balance = beginning_balance - principal 
        if ending_balance < 0:
            ending_balance = 0
        
        row_list.append(month)
        row_list.append(beginning_balance)
        row_list.append(Interest_amount)
        row_list.append(principal)
        row_list.append(ending_balance)

        beginning_balance -= principal 
        
        data_list.append(row_list)

    with open('loan_schedule.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(data_list)