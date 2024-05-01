from Register_user import Register_user
from Variablies import EX_INPUT_BALANCE
def main():      
    while True:
        Operation = input(''' ::::::Operations::::::: 
        1.Register_User
        2.
        3.
        4.Exit
        Choose Operation:: ''')
        try: 
            if Operation == '1':
                k = Register_user()
                print(f"successfully created {k["name"]} {k["surname"]}'s account {k["id"]} and funded {k["balance"]} lari")
            elif Operation == '4':
                break
        except:
            print(EX_INPUT_BALANCE) 
            continue

if __name__ == "__main__":
    main()        