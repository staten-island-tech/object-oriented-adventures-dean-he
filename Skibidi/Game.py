import os, time, json, random

with open('JsonFiles\ShopItems.json', mode='r') as infile:
    Data = json.load(infile)

with open('JsonFiles\PlayerData.json', mode='r') as infile:
    Data2 = json.load(infile)

with open('JsonFiles\enemies.json', mode='r') as infile:
    Data3 = json.load(infile)




def clear():
    os.system('cls')

class Game:
    def __init__(self) -> None:
        pass

    def StartMenu(self):
        clear()
        self.name = input(("Hello human, what would you like to be referred to as?: "))
        time.sleep(0.5)
        print(f"Welcome to THE ULTIMATE GAME, {self.name}. You will be playing a RPG Game. I will be gatekeeping the instruction from you.\n")
        time.sleep(4)
        print("JUST KIDDING! Muahahahahah.\n")
        time.sleep(1)
        print("You must fight against different enemies in different districts, Each time you level up, you get closer to unlocking the new district. You gain levels and bank into order to")
        print("get more attacks and stronger stats. You can choose between fighting and shopping.\n")
        time.sleep(6)
        print("You wake up, GLOCK in hand, destined to resist the NOT YET. ")
        time.sleep(3)
        self.Lobby()
    
    def Lobby(self):
        clear()
        ListChoices = ['SHOP', 'FIGHT']

        LChoice = input("Do you want to go to the SHOP or FIGHT? ").upper()

        while LChoice not in ListChoices:
            clear()
            LChoice = input("Do you want to go to the SHOP or FIGHT? ").upper()
        
        if LChoice == "SHOP":
            self.Shop()
        else:
            self.Fight()





    
    def Shop():
        print("Welcome to the Shop!")
        time.sleep(1)
        print("These are for sale: ")
        
        Shoplvl = 1

        PlayerMoney = 5000
        
        if Shoplvl == 1:
            print('Level 2 Key : 4000')
            print('Hot Coals : 500')
            print('Hydrophilic : 700')
            print('Gorlocks Stomp : 1000')
            buy = input('Input: 1/2/3/4: ')
            if buy == '1':
                for ShopItems in Data:
                    if PlayerMoney >= 4000:
                        for PlayerData in Data2:
                            PlayerData["Inventory"].append(ShopItems["Key"])
                    else:
                        print('You do not have enough money')

            if buy == '2':
                for ShopItems in Data:
                    if PlayerMoney >= 500:
                        for PlayerData in Data2:
                            PlayerData["Inventory"].append(ShopItems["Fire"])
                    else:
                        print('You do not have enough money')
                

""" def shop():
    Shoplvl = 1
    for ShopItems in Data:
        if Shoplvl == ShopItems["LevelReq"]:
            print(ShopItems["Items"])

    print('What would you like buy') """

    def Levelupweapon():
        


              








        

    def Fight(self):
        #get a random enemy from either district 1, 2, 3
        #set variables for each value that the enemy has
        # use those variables
        #when defeated, coin and exp values append to the player values
        #clear all variables and choose a new enemy if chosen fight again
        # repeat for all districts
        clear()

        
        
        enemylist = []
        x = random.choice(enemylist)
        name =  x

        for enemy in Data3:
            if enemy["level"] == 1:
                enemylist.append(enemy["name"])
            if enemy["name"] == name:
                health = enemy["health"]
                damage = enemy["damage"]
                coins = enemy["coins"]
                exp =  enemy["exp"]
                type = enemy["type"]
        print(f"A {name} has stopped you in your journey!")
        time.sleep(2)


        choice = input("What would you like to do? FIGHT/HEAL: ").upper()
        lchoice = ["FIGHT", "HEAL"]


        if choice == "FIGHT":
            print(f"Your attack moves: ")











        

        
        
        

    
    
    



        
