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
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        print('Attack power:', attack_power)
        return attack_power
    def block(self,attack_power):
        damage = attack_power - self.shield-50
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')
    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
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
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        print('The Wizard casts a spell!')
        attack_power = random.randint(int(self.weapon/2),int(self.weapon*2))
        print('Attack power:', attack_power)
        return attack_power + self.magic

class Archer(Fighter):
    def __init__(self, name, starting_health, weapon, shield, bow):
        super().__init__(name, starting_health, weapon, shield)
        self.bow = bow
    def random_attack(self):
        print('The archer aims his bow!')
        aiming = random.randint(1,5)
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        if aiming >3:
            print('The archer missed!')
        else:
            print('Attack power: ',attack_power)
            return attack_power*int(self.bow)
            
        return attack_power
you = Fighter('You',100,60, 50) 
wiz = Wizard('The Grey Wizard',100,30,10,50)
ish = Fighter('The Giant', 300, 40, 10)
Thief = Fighter('Thief', 150, 40,20)
Archer = Archer('Archer', 150, 30,20,1.5)
items = []
Curry = 50

enemy = [Archer]


e = random.choice(enemy)

print('You encountered',f'{e.name}','\nWhat would you do?')
time.sleep(3)
print('')

while True:
    you.report()
    time.sleep(2)
    print('')
    print('1.Attack!\n2.Critical hit!\n3.Items\n4.Run away!')
    print('')
    try:
        action = int(input())
    except ValueError:
        continue
    if action == 1:
        e.defend(you.random_attack())
    elif action == 2:
        e.defend(you.skill_attack())
    elif action == 3:
        print('ye')
    elif action == 4:
        print('nah')
    if e.is_dead():
        print('You win!')
        break
    e.report()
    time.sleep(3)
    print('')
    print(f'{e.name} attacks!')
    time.sleep(2)
    you.defend(e.random_attack())
    if you.is_dead():
        print('You Died!')
        break
    print('')
