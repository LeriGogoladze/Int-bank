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