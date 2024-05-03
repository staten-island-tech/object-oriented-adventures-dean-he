#dustin
#all enemies:goomba, kevin, whalen, henriques, dean, 
#caseoh, spongebob, The Jrim Reeper, Ted Bundy
#hurricane sandy, lebron james
#health, coins, exp,type, name, what level (training district)
import random


class Level1():
    def Goomba():
        health = random.choice[40, 60]
        damage = random.choice[5, 15]
        coins = 100
        exp = random.choice[5, 10]
        type = "Earth"
        level = 1
        boss = False

    def Kevin():
        health = random.choice[65, 90]
        damage = random.choice[10, 15]
        coins = 150
        exp = random.choice[11, 20]
        type = "Earth"
        level = 1
        boss = False

    def Spongebob():
        health = random.choice[95, 115]
        damage = random.choice[16, 25]
        coins = 200
        exp = random.choice[21, 35]
        type = "Water"
        level = 1
        boss = False

    def Dean():
        health = 500
        damage = random.choice[25, 40]
        coins = 400
        exp = random.choice[100, 150]
        type = "Food"
        level = 1
        boss = True



class Level2():
    def Lebron_james():
        health = random.choice[150, 165]
        damage = random.choice[20, 30]
        coins = 300
        exp = random.choice[30, 45]
        type = "Earth"
        level = 2
        boss = False

    def Caseoh():
        health = 700
        damage = random.choice[40, 50]
        coins = 350
        exp = random.choice[50, 60]
        type = "Food"
        level = 2
        boss = False

    def OmniMan():
        health = random.choice[180, 210]
        damage = random.choice[40, 50]
        coins = 400
        exp = random.choice[65, 75]
        type = "Dark"
        level = 2
        boss = False

    def Henriques():
        health = 1000
        damage = random.choice[80, 100]
        coins = 700
        exp = random.choice[100, 120]
        type = "Dark", "Earth"
        level = 2
        boss = True


 Level3():
    def EnderDragon():
        health = random.choice[600, 700]
        damage = random.choice[150, 170]
        coins = 900
        exp = random.choice[121, 140]
        type = "Dark"
        level = 3
        boss = False

    def Britain():
        health = random.choice[700, 800]
        damage = random.choice[160, 190]
        coins = 1000
        exp = random.choice[135, 160]
        type = "Earth", "Water"
        level = 3
        boss = False

    def Disney():
        health = random.choice[420, 900]
        damage = random.choice[200, 210]
        coins = 1200
        exp = random.choice[150, 180]
        type = "Fire", "Earth"
        level = 3
        boss = False

    def Drake():
        health = random.choice[1000, 1200]
        damage = random.choice[220, 250]
        coins = 1500
        exp = random.choice[200, 210]
        type = "Dark", "Food"
        level = 3
        boss = False



    #preboss
    def Shadow():
        health = 10000 
        #should be one tap by mc (surprising)
        damage = random.choice[80, 100]
        exp = 1000
        type = "Dark", "Earth"
        level = 3
        boss = True
        #buildup to whalen (transition into final boss)




    #finalboss
    def Whalen():
        health = 10000
        damage = random.choice[400, 500]
        coins = 2000
        exp = 1000
        type = "???"
        level = 3
        boss = True














class ememies(health, damage):
    def __init__(self, name, health, damage, coins, exp, type, level, boss):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins
        self.exp = exp
        self.type = type
        self.level = level
        self.boss = boss

    def __str__(self):
        return(f'{self.name,self.type,self.boss}')








    

    

    
    

