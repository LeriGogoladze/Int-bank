from Register_user import Register_user
from Variablies import EX_INPUT_BALANCE, EX_BASE_ERROR
from balance import add_balance, transaction
from history import print_balance_history, print_transaction_history

def main():      
    while True:
        Operation = input(''' ::::::Operations::::::: 
        1.Register_User
        2.Add_Balance
        3.Transfer_money
        4.Exit
        Choose Operation:: ''')
        try: 
            if Operation == '1':
                k = Register_user()
                print(f"successfully created {k['name']} {k['surname']}'s account {k['id']} and funded {k['balance']} lari")
            if Operation == '2':
                add_balance()
                user_id = input("Enter your ID: ")
                print_balance_history(user_id)
            if Operation == '3':
                transaction()
                user_id = input("Enter your ID: ")
                print_transaction_history(user_id)
            elif Operation == '4':
                break
        except:
            print(EX_BASE_ERROR) 
            continue

if __name__ == "__main__":
    main()