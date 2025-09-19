class Pet:
    def __init__(self, name, category, breed = None, age = 0): #Default values for attributes
        self._name = name
        self.__category = category
        self.__breed = breed #privated value for breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self):
        self.age += 1 # adds one in birthday/age

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated) #Print function
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
print(p1)

