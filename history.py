from Variablies import DB

def print_transaction_history(user_id):
    for user in DB:
        if user["id"] == user_id:
            print("Transaction History:")
            for transaction in user.get("transaction_history", []):
                print(transaction)
            return
    print("User not found.")

def print_balance_history(user_id):
    for user in DB:
        if user["id"] == user_id:
            print("Balance History:")
            for balance_event in user.get("balance_history", []):
                print(balance_event)
            return
    print("User not found.")

def view_history():
    history_type = input(''' Which history would you like to see?
        1. Balance History
        2. Transaction History
        Choose Operation:: ''')
    if history_type == '1':
        user_id = input("Enter your ID: ")
        print_balance_history(user_id)
    elif history_type == '2':
        user_id = input("Enter your ID: ")
        print_transaction_history(user_id)
    else:
        print("Invalid choice! Please enter either '1' or '2'.")