name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
    print('Welcome to the Pet Data Management System')
    print("Every vet's best friend")

def increase_age():
    global age
    age = age + 1

def verify_credit_card(card_num):
    if len(card_num) == 19 and len(card_num.split()) == 4:
            return True
    else:
        return False

def vacinate(vacine):
    if vaccinated == False:
        return False
    else:
        return True
    
card2 = input('whatcard: ')
if verify_credit_card(card2) == True:
    account_balance = account_balance - 39
    print('Yes',account_balance)
