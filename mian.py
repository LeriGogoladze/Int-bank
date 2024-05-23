from account import Account
from customer import Customer
from transaction import Transactions
from loan import Loan
from hystory import TransactionHystory
from db import get_customer_by_iban,add_balance

def main():      
    while True:
        Operation = input(''' ::::::Operations::::::: 
        1.Register_User
        2.Add_Balance
        3.Transfer_money
        4.Show account details  
        5.Show transaction history
        6.Loan calculator                                  
        7.Exit
        Choose Operation:: ''')
        
        if Operation == '1':
            user_input = [input('Enter owner name: '), input('Enter owner surname: '),int(input('Enter starting balance:'))]
            customer_name = user_input[0].title()
            customer_surname = user_input[1].title()
            balance = user_input[2]
            
            new_account = Account(balance)
            customer = Customer(customer_name,customer_surname,new_account) 
            customer.add_new_customer_in_db(customer)
            print(f"Account successfully created.Owner name- {customer.name},Owner surname- {customer.surname},IBAN - {customer.account} and funded {customer.balance} GEL.")      
        elif Operation == '2':
            iban = input("Input user account number: ")
            current_user = get_customer_by_iban(iban)
            if current_user != None:
                add_balance(iban)
        elif Operation == '3':
            sender = input("Write Your IBAN: ")
            reciver = input("Write ID of addressee: ")  
            Transactions(sender,reciver)
        elif Operation == '4':
            iban = input("Enter user IBAN to show account details: ")
            Customer.get_account_info(iban)
        elif Operation == '5':
            TransactionHystory.view_history()
        elif Operation == '6':
            iban = input("Enter user IBAN to calculate loan :")
            Loan.calculate_loan(iban)
        elif Operation == '7':
            break
    
if __name__ == "__main__":
    main()        