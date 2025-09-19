import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health 
        self.weapon = weapon
        self.shield = shield

    def is_dead(self): 
        if self.__health <= 0: 
            return True
        else:
            return False
        
    def report(self): 
        print(self.name+''+ '\n Health: '+ str(self.__health))

    def random_attack(self): 
        attack_power = random.randint(int(self.weapon/2),int(self.weapon*2))
        print('Attack power:', attack_power)
        return attack_power
    def skill_attack(self): 
        attack_power = random.randint(int(self.weapon/2),int(self.weapon*2))
        target = random.randint(2,6) #random time for the enter to be pressed
        print('Hit enter in',target, 'seconds to perform critical hit!') #
        time.sleep(2)
        for i in range(target): #a count down because the timing will be hard without it
            print(str(int(i+1))+'...')#prints the second 
            time.sleep(1) #with 1 second delay for each
        print('Now') #time window
        tic = time.time() #start timer
        input() #presses a key
        toc = time.time() #ends timer
        taken = toc-tic  #calculates difference
        multiplier = 3-abs(taken) #3-the amount
        if taken >= 1 or taken<0: #if its too late it will be too late
            multiplier = 0
            print('You are too late!!!')
        print('Attack power:', attack_power)
        print('Multiplier: ', multiplier)
        return attack_power*multiplier #calculates damage

    def defend(self,attack_power): 
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage') 


you = Fighter('You',100,60,20) 
Ishraj = Fighter('Ishraj',200,30,10)

print('Yuck! You smell something ahead!!!\nIshraj approaches!') 
print('')
you.report()

while True: 
    print('You attack! \n') 
    time.sleep(2)
    Ishraj.defend(you.skill_attack()) 
    print('') 
    time.sleep(2)
    Ishraj.report() 
    if Ishraj.is_dead(): 
        print('You win!')
        break
    time.sleep(2)
    print('')
    print('Ishraj stikes! ! !')
    time.sleep(2)
    print('')
    you.defend(Ishraj.random_attack()) 
    time.sleep(2)
    print('')
    you.report()
    if you.is_dead():
        print('You lose!')
        break


