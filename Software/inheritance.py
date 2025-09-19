import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2),(self.weapon*2))
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

class Wizard(Fighter):
    def __init__(self,name, starting_health, weapon, shield,magic): #wizard class's attribute
        super().__init__(name, starting_health, weapon, shield) 
        self.magic = magic #magic stat
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        print('Attack power:', attack_power)
        return attack_power + self.magic #calculates the damage and then adds the magical damage with it
    


you = Fighter('You',100,60,20) 
Ishraj = Wizard('Ishraj',200,30,10, 50) #magical ishraj

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
