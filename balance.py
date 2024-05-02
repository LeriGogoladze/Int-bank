# რომ იმუშაოს [{"id": "TB001", "name": "davit", "surname": "darjania", "balance": 20, "loan": 0}]
# ასეთი სახით უნდა იყოს ჩაწერილი მონაცემთა ბაზა variables - ში უნდა იყოს DB
from Variablies import DB
def add_balance():
    your_id = input("Write your ID: ")
    if not check_the_presence_of_value(your_id):
        raise Exception("Your id does not exist!")
    amount = input("Enter the amount you want to add to your balance: ")
    if not amount.isdigit():
        raise Exception("You must Enter a numerical value!")
    for user in DB:
        if user["id"] == your_id:
            user["balance"] += int(amount)
            user["balance_history"].append({"type": "addition", "amount": int(amount)})
            print("Balance added successfully.")
            return
    raise Exception("User not found in DB")
def transaction():
    from_who = input("Write Your ID: ")
    to_who = input("Write ID of addressee: ")
    if from_who == to_who:
        raise Exception("They must be different!")
    if not check_the_presence_of_value(from_who) or not check_the_presence_of_value(to_who):
        raise Exception("Not appropriate IDs!")
    amount_to_send = input("Enter the amount: ")
    if not amount_to_send.isdigit():
        raise Exception("You must enter a numerical value!")
    amount = int(amount_to_send)
    sender = None
    receiver = None
    for user in DB:
        if user["id"] == from_who:
            sender = user
        elif user["id"] == to_who:
            receiver = user
    if not sender or not receiver:
        raise Exception("Sender or receiver not found in DB!")
    if sender["balance"] < amount:
        raise Exception("You cannot send more than you have!")
    sender["balance"] -= amount
    receiver["balance"] += amount
    sender_transaction = {"from": from_who, "to": to_who, "amount": amount}
    sender.setdefault("transaction_history", []).append(sender_transaction)
    receiver_transaction = {"from": from_who, "to": to_who, "amount": amount}
    receiver.setdefault("transaction_history", []).append(receiver_transaction)
    print("Transaction successful!")
    print(DB)
def check_the_presence_of_value(some):
    a = False
    for i in DB:
        if some in i.values():
            a = True
    return a
