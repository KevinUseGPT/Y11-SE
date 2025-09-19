class Pet:
    def __init__(self, name, category, age = 0, credit = "Unknown", Vaccination = "False"): # this read the stat
        self.name = name
        self.category = category
        self.age = age
        self.credit = credit
        self.vaccination = Vaccination
    def __str__(self):
        if len(list(self.credit)) == 16 and len(self.credit.split) == 4: #test valid card
            payment_method = 'Registered payment method'
        else:
            payment_method = 'Not registered' # if the card is not valid it will change it to not registered
        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\ncCard: ' + self.credit + '\nCard status: ' + payment_method + '\nVaccination status: ' + self.vaccination #this is the thing to return
        return my_status #returns the text

p1 = Pet("Bonnie", "Cat") #Bonnie's stats

print(p1) # prints out p1
