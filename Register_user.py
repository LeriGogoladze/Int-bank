from Variablies import DB, EX_INPUT_BALANCE, MAX_BALANCE_AMOUNT, EX_INPUT_NUMBER
from Validation import user_number_gen, user_check_base
import csv

def Register_user():
    
    user = [input('Enter user name: '), input('Enter last name: ')]
    balance = int(input('Enter amount: '))
    if balance > MAX_BALANCE_AMOUNT:
        raise Exception(EX_INPUT_BALANCE)
    if  user_check_base(user_number_gen()):    
        DB.append({"id": user_number_gen(),"name": user[0], "surname": user[1], "balance": balance, "loan": 8.2})
        with open('USERS.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = DB[0].keys(), quoting=csv.QUOTE_NONNUMERIC, delimiter=' ',)
            writer.writeheader()
            writer.writerow(DB[len(DB)-1])
            file.close
        return DB[len(DB)-1]

#except None:
#    print(EX_INPUT_BALANCE)
#except ValueError:
#    print(EX_INPUT_NUMBER)    
