class Pet:
    def __init__(self, name, category, age, ccard, vaccinated, billingaddress):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccinated
        self.billingaddress = billingaddress
        self.ownername = 'unknown'
        self.balance = 0
        
p1 = Pet('Bonnie', 'cat', 3, '4212 1234 3212 6543', 'false', '156 lakeside parade')
p2 = Pet('Foxy', 'dog', 4, '1234 5678 9012 3456', 'true', '3 Baanyas place')

print(f'{p1.name}','s vaccination status is', p1.vaccinated) 