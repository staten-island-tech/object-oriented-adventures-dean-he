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





    
    def Shop(self):
        print("Welcome to the Shop!")
        time.sleep(1)
        print("These are for sale: ")

        Shoplvl = Data2["District"]

        PlayerMoney = Data2['Money']
        
        if Shoplvl == 1:
            print('Level 2 Key : 4000')
            print('Hot Coals : 500')
            print('Hydrophilic : 700')
            print('Gorlocks Stomp : 1000')
            buy = input('Input: 1/2/3/4: ')
            
            if buy == '1':
                if PlayerMoney > 4000:
                    print('You have bought Level 2 Key!')
                    time.sleep(3)
                    Data2['Inventory'].append('Level 2 Key')
                    PlayerMoney = (PlayerMoney - 4000)
                elif PlayerMoney < 4000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '2':
                if PlayerMoney > 500:
                    print('You have bought Hot Coals!')
                    time.sleep(3)
                    Data2['Inventory'].append('Hot Coals')
                    PlayerMoney = (PlayerMoney - 500)
                elif PlayerMoney < 500:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '3':
                if PlayerMoney > 700:
                    print('You have bought Hydrophilic!')
                    time.sleep(3)
                    Data2['Inventory'].append('Hydrophilic')
                    PlayerMoney = (PlayerMoney - 700)
                elif PlayerMoney < 700:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '4':
                if PlayerMoney > 1000:
                    print('You have bought Gorlocks Stomp!')
                    time.sleep(3)
                    Data2['Inventory'].append('Gorlocks Stomp')
                    PlayerMoney = (PlayerMoney - 1000)
                elif PlayerMoney < 1000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()


        if Shoplvl == 2:
            print('Level 3 Key : 20000')
            print('Fireball : 3000')
            print('Ground Split : 3000')
            print('Hydro-pressure Cannon : 5000')
            print('Shadow Spear : 6000')
            buy = input('Input: 1/2/3/4/5: ')
            
            if buy == '1':
                if PlayerMoney > 20000:
                    print('You have bought Level 3 Key!')
                    time.sleep(3)
                    Data2['Inventory'].append('Level 3 Key')
                    PlayerMoney = (PlayerMoney - 20000)
                elif PlayerMoney < 20000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '2':
                if PlayerMoney > 3000:
                    print('You have bought Fireball!')
                    time.sleep(3)
                    Data2['Inventory'].append('Fireball')
                    PlayerMoney = (PlayerMoney - 3000)
                elif PlayerMoney < 3000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '3':
                if PlayerMoney > 3000:
                    print('You have bought Ground Split!')
                    time.sleep(3)
                    Data2['Inventory'].append('Ground Shatter')
                    PlayerMoney = (PlayerMoney - 3000)
                elif PlayerMoney < 3000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '4':
                if PlayerMoney > 5000:
                    print('You have bought Hydro-pressure Cannon!')
                    time.sleep(3)
                    Data2['Inventory'].append('Hydro-pressure Cannon')
                    PlayerMoney = (PlayerMoney - 5000)
                elif PlayerMoney < 5000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '5':
                if PlayerMoney > 6000:
                    print('You have bought Shadow Spear!')
                    time.sleep(3)
                    Data2['Inventory'].append('Shadow Spear')
                    PlayerMoney = (PlayerMoney - 6000)
                elif PlayerMoney < 6000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

        
        if Shoplvl == 3:
            print('Pyrokinesis : 10000')
            print('Earth Shatter : 15000')
            print('Bullet Rain : 15000')
            print('Black Hole : 20000')
            buy = input('Input: 1/2/3/4: ')
            
            if buy == '1':
                if PlayerMoney > 10000:
                    print('You have bought Pyrokinesis!')
                    time.sleep(3)
                    Data2['Inventory'].append('Pyrokinesis')
                    PlayerMoney = (PlayerMoney - 10000)
                elif PlayerMoney < 10000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '2':
                if PlayerMoney > 15000:
                    print('You have bought Ground Shatter!')
                    time.sleep(3)
                    Data2['Inventory'].append('Ground Shatter')
                    PlayerMoney = (PlayerMoney - 15000)
                elif PlayerMoney < 15000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '3':
                if PlayerMoney > 15000:
                    print('You have bought Bullet Rain!')
                    time.sleep(3)
                    Data2['Inventory'].append('Bullet Rain')
                    PlayerMoney = (PlayerMoney - 15000)
                elif PlayerMoney < 15000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()

            if buy == '4':
                if PlayerMoney > 20000:
                    print('You have bought Black Hole!')
                    time.sleep(3)
                    Data2['Inventory'].append('Black Hole')
                    PlayerMoney = (PlayerMoney - 20000)
                elif PlayerMoney < 20000:
                    print('You do not have enough money')
                    time.sleep(3)
                    self.Lobby()



    def bosses1(self):
        for enemy in Data3:
            if enemy["level"] == 1 and enemy["boss"] == "Y":
                name =  enemy["name"]
                health = enemy["health"]
                damage = enemy["damage"]
                coins = enemy["coins"]
                exp =  enemy["exp"]
                type = enemy["type"]
        
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

            choice = input("What would you like to do? FIGHT/HEAL: \n").upper()
            lchoice = ["FIGHT", "HEAL"]

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
                    if " " in Data2["Inventory"]:
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
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    Data2["District"] += 1
                    self.Fight2()
                    break
                if defeated == True:
                    break
            if choice == "HEAL":
                player_health += 20

    def bosses2(self):
        for enemy in Data3:
            if enemy["level"] == 2 and enemy["boss"] == "Y":
                name =  enemy["name"]
                health = enemy["health"]
                damage = enemy["damage"]
                coins = enemy["coins"]
                exp =  enemy["exp"]
                type = enemy["type"]
        
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

            choice = input("What would you like to do? FIGHT/HEAL: \n").upper()
            lchoice = ["FIGHT", "HEAL"]

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
                    if " " in Data2["Inventory"]:
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
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    Data2["District"] += 1
                    self.Fight3()
                    break
                if defeated == True:
                    break
            if choice == "HEAL":
                player_health += 30
        
    def shadow(self):
        for enemy in Data3:
            if enemy["level"] == 3 and enemy["boss"] == "Y" and enemy["name"] == "someones_shadow?":
                name =  enemy["name"]
                health = enemy["health"]
                damage = enemy["damage"]
                coins = enemy["coins"]
                exp =  enemy["exp"]
                type = enemy["type"]
        
        player_health = Data2["Health"]

        if health > 0:
            defeated = False

        def idkattackmove(health):
            health -= 1000000
            return health
        
        def idkdamagehealth(player_health):
            player_health -= damage
            return player_health

        print(f"A {name} has stopped you in your journey!\n")
        while defeated == False:
            
            time.sleep(2)

            choice = input("What would you like to do? FIGHT/HEAL: \n").upper()
            lchoice = ["FIGHT", "HEAL"]

            if choice == "FIGHT":
                print(f"Your attack moves: {Data4[0]['name']}, and your inventory is {Data2['Inventory']}\n")
                fightingchoices = ["MOVE", "INVENTORY"]
                fightingchoice = input("Would you want to use your attack move, or something from your inventory? MOVE/INVENTORY: \n").upper()
            
                if fightingchoice == "MOVE":
                    print(f"You used {Data4[0]['name']}, you dealt {Data4[0]['damage']}!")
                    health = idkattackmove(health)
                    print(f"The enemy's health is {health}")

                else:
                    print("NO INVENTORY")
                
                print(f"Ouch, looks like he did {damage} to your health!")
                player_health = idkdamagehealth(player_health)
                print(f"Your health is {player_health}")
                if health < 0:
                    defeated = True
                    print("Yippee you killed them!!!")
                    time.sleep(5)
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    self.Whalen()
                    break
                if defeated == True:
                    break
            if choice == "HEAL":
                player_health += 50
   
        
    def Whalen(self):
        for enemy in Data3:
            if enemy["name"] == "Whalen":
                name =  enemy["name"]
                health = enemy["health"]
                damage = enemy["damage"]
                coins = enemy["coins"]
                exp =  enemy["exp"]
                type = enemy["type"]
        
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

            choice = input("What would you like to do? FIGHT/HEAL: \n").upper()
            lchoice = ["FIGHT", "HEAL"]

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
                    if " " in Data2["Inventory"]:
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
                    print("Yippee you hit him lightly!!!")
                    time.sleep(5)
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    break
                if defeated == True:
                    break
            if choice == "HEAL":
                player_health += 30






    

        









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
                Data2["Health"] += 30
                

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
                    if "" in Data2["Inventory"]:
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
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    if 'Level 2 Key' in Data2["Inventory"]:
                        self.bosses1()
                    break

                if defeated == True:
                    break
            
            if choice == "HEAL":
                player_health += 15








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
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    if 'Level 3 Key' in Data2["Inventory"]:
                        self.bosses2()
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
                    coins += Data2["Money"]
                    exp += Data2["Exp"]
                    choice = input("Are you ready? Y/N ").upper()
                    if choice == 'Y':
                        self.shadow()
                    else:

                        break

                if defeated == True:
                    break

    


    def LevelUp():
        requiredxp = 20
        if Data2["Exp"] >= requiredxp:
            Data2["Level"] += 1 
            requiredxp += 20
            Data4["damage"] += 20
            Data2["Health"] += 100
            print(f"You have leveled up to {Data2['Level']}")


