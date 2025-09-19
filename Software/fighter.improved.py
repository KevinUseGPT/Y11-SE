import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield): #values for character
        self.name = name 
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self): #your stats printed
        print(self.name+ ':\nHealth: '+str(self.health))
    def atk(self): #random attack damage in a range
        dmg = random.randint(int(self.weapon/2),int(self.weapon*2))
        print('Attack power: '+str(dmg))
        return dmg
    def defend(self,dmg):
        damage = dmg-self.shield #total damage will be how much shield - the attack power(real damage)
        if damage > 0: #if its smaller than 0 then it will print miss if bigger it will deal on the health
            self.health -= damage
            print('Damage: ',damage)
        else:
            print('Misses!!!')

you = Fighter('You',150,60,30)  #stats of characters
ishraj = Fighter('Ishraj',300,40,15)

print('You smell something funny')
time.sleep(3)
print('INCOMING!!!!')
time.sleep(3)
print('You encounter Ishraj')
time.sleep(2)
while you.health > 0 and ishraj.health > 0: #When my health and the enemies health is above zero it will run until it has a winner
    you.report() #reports my stats
    time.sleep(3) #wait time for each message
    print('You attack Ishraj!') #print the actions
    print('')
    time.sleep(2)
    ishraj.defend(you.atk())
    print('')     
    time.sleep(3)
    if ishraj.health <=0:  #checks if the goblin is alive
        print('Ishraj has fallen')
        print('You win')
        break
    ishraj.report() 
    print('')
    print('Ishraj strikes!!!')
    time.sleep(2)
    you.defend(ishraj.atk())
    print('')
    time.sleep(3) 
    if you.health <= 0: #checks if I am alive after his hit
        print("You've fallen")
        print('You lose!')
        break
