import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health #private health 
        self.weapon = weapon
        self.shield = shield

    def is_dead(self): #Checking function
        if self.__health <= 0: #if health is lower or equal to 0 it will be true in the if statement, then it will print the outcome of lose or win and then break
            return True
        else:
            return False
        
    def report(self): 
        print(self.name+''+ '\n Health: '+ str(self.__health))

    def random_attack(self): #random attack power function selecting a random number in a range of ur weapon damage divide or multiplied by 2
        attack_power = random.randint(int(self.weapon/2),int(self.weapon*2))
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power): #attack power minuses the shield power will give the damage
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage #if its bigger than 0 it will print out the outcome damage
            print('Damage:', damage)
        else:
            print('No damage') #if 0 or below it will be no damage


you = Fighter('You',100,60,20) #2 characters
Ishraj = Fighter('Ishraj',200,30,10)

print('Yuck! You smell something ahead!!!\nIshraj approaches!') 
print('')
you.report()

while True: #loop until death
    print('You attack! \n') 
    time.sleep(2)
    Ishraj.defend(you.random_attack()) #you attack
    print('') 
    time.sleep(2)
    Ishraj.report() #reports the stats of ishraj
    if Ishraj.is_dead(): #checks if he died
        print('You win!')
        break
    time.sleep(2)
    print('')
    print('Ishraj stikes! ! !')
    time.sleep(2)
    print('')
    you.defend(Ishraj.random_attack()) #he attacks you
    time.sleep(2)
    print('')
    you.report()#reports your stats
    if you.is_dead():#checks if you died
        print('You lose!')
        break


