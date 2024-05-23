from db import db
import random

def check_account(iban):
    if len(db)> 0:
        for account in db:
            if account['iban'] == iban:
                account_number_gen()
            else:
                return iban     
    else:
        return iban

def account_number_gen():
    GEN_NUMBER = 'TB'
    for i in range(4):
        GEN_NUMBER += str(random.randint(0,9))
    return check_account(GEN_NUMBER)

def check_iban_format(iban):
    if not iban.upper().startswith("TB"):
        return False,"Wrong prefix for account!" 
    elif len(iban) != 6:
        return False,"Wrong IBAN length!"
    else:
        if not iban[2:7].isdigit():
            return False,"After prefix IBAN must contain numbers!"
        else:
            return True,None  
