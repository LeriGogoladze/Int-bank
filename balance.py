# რომ იმუშაოს DB = [{"id": "TB001", "name": "davit", "surname": "darjania", "balance": 20, "loan": 0}]
# ასეთი სახით უნდა იყოს ჩაწერილი მონაცემთა ბაზა. (variables - ში უნდა იყოს DB)
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
import csv 
import time
def make_csv_transaction(f, t, a): #გადაეცემა პირადი ნომრები transaction - ფუნქციიდან, იქედანვე იღებს სახელებს, გვარებს და ადგენს მონაცემებს 
    for i in DB:
        if f in i.values():
            name_from = i["name"]
            surname_from = i["surname"]
        if t in i.values():
            name_to = i["name"]
            surname_to = i["surname"]
    current_time = current_time_returner()    
    with open("transactions.csv", "a") as csv_file:
        fieldnames = (["From", "To", "Amount", "Time"])
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({"From": f"{name_from} {surname_from}", "To": f"{name_to} {surname_to}", "Amount": a, "Time": current_time})
def current_time_returner(): # აბრუნებს ზუსტ ახლანდელ დროს 
    local_time = time.localtime()
    current_time = time.strftime("%B %d %Y %H:%M:%S%p GMT%Z", local_time)
    return current_time
def check_the_presence_of_value(some):
    a = False
    for i in DB:
        if some in i.values():
            a = True
    return a
