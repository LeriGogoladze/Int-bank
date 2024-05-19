from Variablies import DB
# DB = [{"id": "TB0001", "name": "davit", "surname": "darjania", "balance": 20, "loan": 10}]
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

def get_user_info(iban):
    current_user = None
    ok,error = check_iban_format(iban)
    if ok:
        for user in DB:
            if iban in user.values():
                current_user = user
                break   
        if not current_user:
            print(f"user with IBAN- '{iban}' not found!!")
        else:
            print(f"user name is '{current_user["name"]}',surname - '{current_user["surname"]}'")  
    else:
        print(error)


