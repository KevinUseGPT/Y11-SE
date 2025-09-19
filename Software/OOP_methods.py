class Pet:
    def __init__(self, name, category, age = 0, ccard="Unregisted", vaccinated=False, account_balance=0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccinated
        self.account_balance = account_balance
    def vaccinating(self): #Vaccination function, it will make vaccinated status == true
        self.vaccinated = True
        print("Vaccinating animal...")
    def have_birthday(self): #Adds one birthday to the age
        self.age += 1
    def rob_money(self): #Clears out all the money inside the account balance
        self.account_balance = 0
    def dog_age(self): #Multiplies the age by 7 to make it in dog years
        dog_years = self.age*7
        print(self.name+" is "+str(dog_years)+" in dog years!")
    def __str__(self): #Scaffold of the sentence that will be printed
        stats = "Name: "+self.name+"\nCategory: "+self.category+"\nAge: "+str(self.age)+"\ncCard: "+self.ccard+"\nVaccination: "+f'{self.vaccinated}'+"\nAccount balance: "+"$"+str(self.account_balance)
        return stats
p1 = Pet("Ishraj", "Dog", 3, "Registered", False, 654)
p1.have_birthday() #Birthday function
p1.vaccinating() #Vaccinate the animal
p1.rob_money() #Running clearing balance function
print(p1) #Printing stats
p1.dog_age() #Run the dog year function