class Car:
    def __init__(self, name, Wheels, sunroof, doors, seats): # the stats of the cars that should be printed
        self.name = name
        self.wheels = Wheels
        self.sunroof = sunroof
        self.doors = doors
        self.seats = seats 
        print('Car: '+self.name+'\nWheels: '+ str(self.wheels)+'\nsunroof: '+f'{self.sunroof}'+'\nDoors: '+f'{self.doors}'+'\nSeats: '+ f'{self.seats}')
        print('') #Printing the car

c1 = Car("Banana car", 8, None, None, 6) #car 1
c2 = Car("Ishraj's Tesla", 4, 1, 4, 4) #car 2


