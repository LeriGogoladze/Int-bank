from Variablies import DB, EX_CHECK_ERROR
import random

def user_check_base(user):
    for i in DB:
        if i['id'] == user:
            raise Exception(EX_CHECK_ERROR)
    return user     

def user_number_gen():
    GEN_NUMBER = 'TB'
    for i in range(4):
        GEN_NUMBER += str(random.randint(0,9))
    return GEN_NUMBER          