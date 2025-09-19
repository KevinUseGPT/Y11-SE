import random
class Fighter:
    def __init__(self, name, health, attack, defend): #All values for the fighter
        self.name = name 
        self.__health = health #privated value
        self.attack = attack
        self.defend = defend
    def gethealth(self): #get the health from private
        return self.__health
    def report(self):
        print(self.name+':'+'\nHealth: '+str(self.__health)) #reporting the stats of the character
    def atk(self): #calculating the attack damage range and printing delt damage
        dmg=random.randint(int(self.attack/2),int(self.attack*2)) 
        print('Damage delt: '+str(dmg))
        return dmg

you = Fighter('You',100,8,10) #my stats
ishraj = Fighter('Ishraj',100,8,5) #The goblin's stats

myhealth = you.gethealth() # getting health 
enemyhealth = ishraj.gethealth()


while myhealth > 0 and enemyhealth > 0: #When my health and the enemies health is above zero it will run until it has a winner
    you.report() #reports my stats
    print('You attack Ishraj!') 
    print('')
    enemyhealth -= you.atk() #attacks
    if enemyhealth <=0: #if their health < 0 then print win and break
        print('You win')
        break
    ishraj.report() #if not they attack me
    print('')
    print('Ishraj strikes!!!')
    myhealth -= ishraj.atk()
    you.report() 
    if myhealth <= 0: #if my health is below 0 i lose and print lose
        print('You lose!')
        break
