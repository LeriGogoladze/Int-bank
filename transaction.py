from db import db
import csv 
import time

class Transactions:
    def __init__(self,from_who,to_who):
        
        if from_who == to_who:
            raise Exception("They must be different!")
        if not check_the_presence_of_value(from_who) or not check_the_presence_of_value(to_who):
            raise Exception("Not appropriate ID's!")  
        amount_to_send = input("Enter the amount: ")
        if not amount_to_send.isdigit():
            raise Exception("You must Enter numerical value!")
        for i in db:
            if from_who in i.values():
                if i["balance"] < int(amount_to_send):
                    raise Exception("You can not send more than you have!")
                i['balance'] -= int(amount_to_send)
            if to_who in i.values():
                i["balance"] += int(amount_to_send)
        make_csv_transaction(from_who,to_who, amount_to_send)

def make_csv_transaction(f, t, a): #გადაეცემა პირადი ნომრები transaction - ფუნქციიდან, იქედანვე იღებს სახელებს, გვარებს და ადგენს მონაცემებს 
    for i in db:
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
    for i in db:
        if some in i.values():
            a = True
    return a