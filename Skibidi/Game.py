import os, time, json, random

with open('JsonFiles\ShopItems.json', mode='r') as infile:
    Data = json.load(infile)

with open('JsonFiles\PlayerData.json', mode='r') as infile:
    Data2 = json.load(infile)

with open('JsonFiles\enemies.json', mode='r') as infile:
    Data3 = json.load(infile)

with open('JsonFiles\LevelUnlocks.json', mode='r') as infile:
    Data4 = json.load(infile)



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
        time.sleep(1)
        print("You wake up, Nerf Glock in hand, destined to resist the NOT YET. ")
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
            self.Fight1()





    
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
        
            if buy == '3':
                for ShopItems in Data:
                    if PlayerMoney >= 700:
                        for PlayerData in Data2:
                            PlayerData["Inventory"].append(ShopItems["Fire"])
                    else:
                        print('You do not have enough money')

            if buy == '4':
                for ShopItems in Data:
                    if PlayerMoney >= 1000:
                        for PlayerData in Data2:
                            PlayerData["Inventory"].append(ShopItems["Fire"])
                    else:
                        print('You do not have enough money')
                



    def Levelupweapon():
        while Data2["Level"] == 1:
            #make damage equal to 10 for glock
            Data4["damage"] = 10
        
        if Data2["Level"] == +1:
            Data4["damage"] + 20


              






    

        

    def Fight1(self):

        clear()

        
        



        enemylist = []
        for enemy in Data3:
            if enemy["level"] == 1 and enemy["boss"] == "N":
                enemylist.append(enemy)
            
        x = random.choice(enemylist)
        name =  x["name"]
        health = x["health"]
        damage = x["damage"]
        coins = x["coins"]
        exp =  x["exp"]
        type = x["type"]


        player_health = Data2["Health"]

        

        if health > 0:
            defeated = False

        

        def idkattackmove(health):
            health -= int(Data4[0]["damage"])
            return health
        
        def idkdamagehealth(player_health):
            player_health -= damage
            return player_health

        

        print(f"A {name} has stopped you in your journey!\n")
        while defeated == False:
            
            time.sleep(2)




            choice = input("What would you like to do? FIGHT/HEAL/RETURN: \n").upper()
            lchoice = ["FIGHT", "HEAL", "RETURN"]

        

            if choice == "RETURN":
                self.Lobby()

            if choice == "HEAL":
                Data2["Health"] += 15
                

            if choice == "FIGHT":
                print(f"Your attack moves: {Data4[0]['name']}, and your inventory is {Data2['Inventory']}\n")
                fightingchoices = ["MOVE", "INVENTORY"]
                fightingchoice = input("Would you want to use your attack move, or something from your inventory? MOVE/INVENTORY: \n").upper()
            
                if fightingchoice == "MOVE":
                    print(f"You used {Data4[0]['name']}, you dealt {Data4[0]['damage']}!")
                    health = idkattackmove(health)
                    print(f"The enemy's health is {health}")

                else:
                    if not Data2["Inventory"]:
                        print("List is empty, moving to next turn")
                    if x in Data2["Inventory"]:
                        moves = print(Data2['Inventory'])
                        
                        pick = input("Pick an inventory item to use: ")

                        if pick == moves:
                            print(f"You used {pick}! You dealt {Data['damage']}!")
                            health - Data["damage"]
                
                print(f"Ouch, looks like he did {damage} to your health!")
                player_health = idkdamagehealth(player_health)
                print(f"Your health is {player_health}")

                
                if health < 0:
                    defeated = True
                    print("Yippee you killed them!!!")
                    time.sleep(5)
                    coins + Data2["Money"]
                    exp + Data2["Exp"]
                    break

                if defeated == True:
                    break








    def Fight2(self):
        clear()

        
        



        enemylist = []
        for enemy in Data3:
            if enemy["level"] == 2 and enemy["boss"] == "N":
                enemylist.append(enemy)
            
        x = random.choice(enemylist)
        name =  x["name"]
        health = x["health"]
        damage = x["damage"]
        coins = x["coins"]
        exp =  x["exp"]
        type = x["type"]


        player_health = Data2["Health"]

        

        if health > 0:
            defeated = False

        

        def idkattackmove(health):
            health -= int(Data4[0]["damage"])
            return health
        
        def idkdamagehealth(player_health):
            player_health -= damage
            return player_health

        

        print(f"A {name} has stopped you in your journey!\n")
        while defeated == False:
            
            time.sleep(2)




            choice = input("What would you like to do? FIGHT/HEAL/RETURN: \n").upper()
            lchoice = ["FIGHT", "HEAL", "RETURN"]

        

            if choice == "RETURN":
                self.Lobby()

            if choice == "HEAL":
                Data2["Health"] += 15
                

            if choice == "FIGHT":
                print(f"Your attack moves: {Data4[0]['name']}, and your inventory is {Data2['Inventory']}\n")
                fightingchoices = ["MOVE", "INVENTORY"]
                fightingchoice = input("Would you want to use your attack move, or something from your inventory? MOVE/INVENTORY: \n").upper()
            
                if fightingchoice == "MOVE":
                    print(f"You used {Data4[0]['name']}, you dealt {Data4[0]['damage']}!")
                    health = idkattackmove(health)
                    print(f"The enemy's health is {health}")

                else:
                    if not Data2["Inventory"]:
                        print("List is empty, moving to next turn")
                    if x in Data2["Inventory"]:
                        moves = print(Data2['Inventory'])
                        
                        pick = input("Pick an inventory item to use: ")

                        if pick == moves:
                            print(f"You used {pick}! You dealt {Data['damage']}!")
                            health - Data["damage"]
                
                print(f"Ouch, looks like he did {damage} to your health!")
                player_health = idkdamagehealth(player_health)
                print(f"Your health is {player_health}")

                
                if health < 0:
                    defeated = True
                    print("Yippee you killed them!!!")
                    time.sleep(5)
                    coins + Data2["Money"]
                    exp + Data2["Exp"]
                    break

                if defeated == True:
                    break








    def Fight3(self):
        clear()

        
        



        enemylist = []
        for enemy in Data3:
            if enemy["level"] == 3 and enemy["boss"] == "N":
                enemylist.append(enemy)
            
        x = random.choice(enemylist)
        name =  x["name"]
        health = x["health"]
        damage = x["damage"]
        coins = x["coins"]
        exp =  x["exp"]
        type = x["type"]


        player_health = Data2["Health"]

        

        if health > 0:
            defeated = False

        

        def idkattackmove(health):
            health -= int(Data4[0]["damage"])
            return health
        
        def idkdamagehealth(player_health):
            player_health -= damage
            return player_health

        

        print(f"A {name} has stopped you in your journey!\n")
        while defeated == False:
            
            time.sleep(2)




            choice = input("What would you like to do? FIGHT/HEAL/RETURN: \n").upper()
            lchoice = ["FIGHT", "HEAL", "RETURN"]

        

            if choice == "RETURN":
                self.Lobby()

            if choice == "HEAL":
                Data2["Health"] += 15
                

            if choice == "FIGHT":
                print(f"Your attack moves: {Data4[0]['name']}, and your inventory is {Data2['Inventory']}\n")
                fightingchoices = ["MOVE", "INVENTORY"]
                fightingchoice = input("Would you want to use your attack move, or something from your inventory? MOVE/INVENTORY: \n").upper()
            
                if fightingchoice == "MOVE":
                    print(f"You used {Data4[0]['name']}, you dealt {Data4[0]['damage']}!")
                    health = idkattackmove(health)
                    print(f"The enemy's health is {health}")

                else:
                    if not Data2["Inventory"]:
                        print("List is empty, moving to next turn")
                    if x in Data2["Inventory"]:
                        moves = print(Data2['Inventory'])
                        
                        pick = input("Pick an inventory item to use: ")

                        if pick == moves:
                            print(f"You used {pick}! You dealt {Data['damage']}!")
                            health - Data["damage"]
                
                print(f"Ouch, looks like he did {damage} to your health!")
                player_health = idkdamagehealth(player_health)
                print(f"Your health is {player_health}")

                
                if health < 0:
                    defeated = True
                    print("Yippee you killed them!!!")
                    time.sleep(5)
                    coins + Data2["Money"]
                    exp + Data2["Exp"]
                    break

                if defeated == True:
                    break






""" def shop():
    Shoplvl = 1
    for ShopItems in Data:
        if Shoplvl == ShopItems["LevelReq"]:
            print(ShopItems["Items"])

    print('What would you like buy') """




                

        











        

        
        
        

    
    
    



        
