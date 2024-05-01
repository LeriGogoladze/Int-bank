# რომ იმუშაოს [{"id": "TB001", "name": "davit", "surname": "darjania", "balance": 20, "loan": 0}]
# ასეთი სახით უნდა იყოს ჩაწერილი მონაცემთა ბაზა variables - ში უნდა იყოს DB
from Variablies import DB
def add_balance():
    your_id = input("Write your ID: ")
    if not check_the_presence_of_value(your_id):
        raise Exception("Your id does not exists!")
    amount = input("Enter the amount you want to add to your balance: ")
    if not amount.isdigit():
        raise Exception("You must Enter numerical value!")
    for i in DB:
        if your_id in i.values():
            i["balance"] += int(amount)
    print(DB)
def transaction():
    from_who = input("Write Your ID: ")
    to_who = input("Write ID of addressee: ")
    if from_who == to_who:
        raise Exception("They must be different!")
    if not check_the_presence_of_value(from_who) or not check_the_presence_of_value(to_who):
        raise Exception("Not appropriate ID's!")  
    amount_to_send = input("Enter the amount: ")
    if not amount_to_send.isdigit():
        raise Exception("You must Enter numerical value!")
    for i in DB:
        if from_who in i.values():
            if i["balance"] < int(amount_to_send):
                raise Exception("You can not send more than you have!")
            i['balance'] -= int(amount_to_send)
        if to_who in i.values():
            i["balance"] += int(amount_to_send)
    print(DB) 
def check_the_presence_of_value(some):
    a = False
    for i in DB:
        if some in i.values():
            a = True
    return a
