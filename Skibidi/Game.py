import time, os, random, json

# Open the JSON file of pokemon data
test = open("enemies.json",)
test2 = open("LevelUnlocks.json",)
test3 = open("PlayerData.json",)
test4 = open("ShopItems.json",)
# create variable "data" that represents the enitre pokedex list
enemies = json.load(test)
levelunlocks = json.load(test2)
playerdata = json.load(test3)
shopitems = json.load(test4)




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





    
    def Shop(self):
        print("Welcome to the Shop!")
        time.sleep(1)

        print("These are for sale: ")
        level1items = []
        level2items = []
        level3items = []
        for item in shopitems:
            if item["Level"] == 1:
                level1items.append(item["name"], )
            if item["Level"] == 2:
                level2items.append(item["name"], f"cost = {item["cost"]}")
            if item["Level"] == 3:
                level3items.append(item["name"])
            if item["name"] == "Level 2 key":
                print("Level 2 key: unable to buy")

        print

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

        for enemy in enemies:
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











        

        
        
        

    
    
    



        
