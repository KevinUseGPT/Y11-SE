class Pet:
    def __init__(self, name, species, age, status): #All the stats the pet contains
        self.name = name    
        self.species = species
        self.age = age
        self.status = True

    def __str__(self): #scaffolding out each stat with new line
        text = "Pet name: "+ self.name+"\nSpecies: "+ self.species+"\nAge: "+str(self.age)+"\nVaccination status: "+ f'{self.status}'
        return text #returning the text

p1= Pet('Foxy', 'Dog', 8, False) #Pet foxy's stats
p2= Pet("Ishraj", "Rat", 59, False) #Rat's stat
p3= Pet("Hootie", "Blowfish", 34, False)
pets = [p1, p2, p3]#The list that will run in the class function

for i in pets: #prints out the outcome with new line using for loop
    print(i)
    print('')