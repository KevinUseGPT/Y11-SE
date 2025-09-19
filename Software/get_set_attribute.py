class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def get_weight(self): #Get the value inside the brackets in the function
        return self.weight
    def set_weight(self, new_weight): #Changes the weight from 0 to the set weight
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print("Please enter a positive number") #If the number is lower than 0 it will print this
        else:
            print('Please print a number') #It has to be a number, not a string or boolean


p1 = Pet("Bonnie", "Cat", age=3)
p1.set_weight(23) #sets the value
print("Bonnie's weight is: ",p1.weight,'Kg') #prints out the weight