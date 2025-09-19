class Pet:
    def __init__(self, name, category, age = 0, ccard = "unknown"):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
    def __str__(self):
        payment = 'Unregistered'
        if len(self.ccard) == 19:
            payment = 'Registered' # payment will always be unregistered unless the ccard is valid
        mystatus =  'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\npayment: ' + self.ccard + '\nVaccination status: ' + f'{self.vaccinated}' #the text that will be returned for printing
        return mystatus
    

    
pet1 = Pet("Bonnie", "Cat", 3) #pets stat
pet2 = Pet("Ishraj", "Rat", 59)
pet3 = Pet(category="Dog", name="Kevin",age=4)

pets = [pet1, pet2, pet3] # list of pet which was supposed to be printed in forloop

    
for i in pets: #vaccinating pet
    i.vaccinated = True
    print(i)
    print('')