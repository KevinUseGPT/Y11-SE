class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0
    
    def set_name(self,new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Please use a string as a name attribute')
    
    def get_name(self):
        return self._name

    def get_weight(self):
        return self.weight

    def get_category(self):
        return self.__category
    
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')
        else:
            print('Please enter a number for weight')

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'
        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name='Bonnie', category='Dog')
p2 = Pet('Clyde','Cat','Persian',12)
p3 = Pet('Cindy', 'Dog',age = 3)
p4 = Pet('Ishraj', 'Rat','Street rat',age=59) #New pet 1
p5 = Pet('Morshed','Dog',age=30) #New pet 2

pets = [p1,p2,p3,p4,p5]


for pet in pets: #For loop to go through all the pets in pet list
    pet.age += 1 #Adds one age to the pet
    category = pet.get_category() #get the category of the pet through the get category function
    if category == 'Dog': #If its a dog it will print the stats of the pet
        print(pet)
        print('')
