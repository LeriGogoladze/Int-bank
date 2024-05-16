from Register_user import Register_user
from balance import add_balance, transaction
from user import get_user_info
from loan_calculator import calculate_loan

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
        try: 
            if Operation == '1':
                k = Register_user()
                print(f"successfully created {k["name"]} {k["surname"]}'s account {k["id"]} and funded {k["balance"]} lari")
            if Operation == '2':
                add_balance()
            if Operation == '3':
                transaction()
            if Operation == '4':
                iban = input("Enter user IBAN to show account details: ")
                get_user_info(iban)
            if Operation == '6':
                iban = input("Enter user IBAN to calculate loan :")
                calculate_loan(iban)
            elif Operation == '7':
                break
        except Exception as e:
            print(e) 
            continue

if __name__ == "__main__":
    main()        