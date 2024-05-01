from Register_user import Register_user
from Variablies import EX_INPUT_BALANCE, EX_BASE_ERROR
from balance import add_balance, transaction
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
                print(f"successfully created {k["name"]} {k["surname"]}'s account {k["id"]} and funded {k["balance"]} lari")
            if Operation == '2':
                add_balance()
            if Operation == '3':
                transaction()
            elif Operation == '4':
                break
        except:
            print(EX_BASE_ERROR) 
            continue

if __name__ == "__main__":
    main()        