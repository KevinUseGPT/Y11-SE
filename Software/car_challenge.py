class Car:
    def __init__(self,make,model,year,price="???",status="For sale"):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.status = status #status of the car eg.sale or not default is sale
    def __str__(self):
        sale = 'Brand: '+self.make+'\nModel: '+self.model+'\nYear: '+str(self.year)+'\nPrice: '+str(self.price)+'\nStatus: '+self.status
        return sale
Mazda = Car('Mazda','6',2005,price='$250000') #cars and ishraj's bike
Banana = Car('Banana Car','5',2023,status="Not for sale",price='$100B')
Motorcycle = Car("Ishraj's Motorcycle", 'X', 1900, price='1 Rupee')

cars = [Mazda, Banana, Motorcycle]

for car in cars: # prints the stats
    print(car)
    print('')
