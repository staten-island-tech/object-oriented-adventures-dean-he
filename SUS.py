import json, random, time, os


# Open the JSON file of pokemon data
test = open("enemies.json",)
# create variable "data" that represents the enitre pokedex list
enemies = json.load(test)




name = input(("Hello human, what would you like to be referred to as?: "))
time.sleep(0.5)
print(f"Welcome to THE ULTIMATE GAME, {name}. You will be playing a RPG Game. I will be gatekeeping the instruction from you.\n")
time.sleep(4)
print("JUST KIDDING! Muahahahahah.\n")
time.sleep(1)
print("You must fight against different enemies in different districts, Each time you level up, you get closer to unlocking the new district. You gain levels and bank into order to")
print("get more attacks and stronger stats. You can choose between fighting, shopping, and healing.\n")
time.sleep(10)
print("You wake up, GLOCK in hand, destined to resist the NOT YET. ")
time.sleep(2)

choose = input(("\nWould you rather fight, shop, or heal? F/S/H: ")).upper

health = 100
level = 0
money = 0
turn = 0 
required_xp = 50

from levelup import levelup
from districts import districts

class player:
    def __init__(self, name, health, moves,  level, money, playerhealth):
        self.name = name
        self.health = health
        self.moves = moves
        self.level = level
        self.money = money
    def __str__(self):
        return f"{self.name}{self.moves}"


def District1():
        enemys = []
        for enemy in enemies:
            if enemies["level"] == 1:
                enemys.append["name"]
        select = random.choice[enemys]
        return select 








enemy_data = []






if choose == "F": 
    """ enemys = []
    enemy_data = []
    select = random.choice[enemys]
    if select == enemies["name"]:
        enemy_data.append["name", "health", "damage", "coins", "exp", "type", "level", "boss"]
    if enemy_data["boss"] == "Y":
        enemy_data.clear()
    print(f"A {"name"} has appeared!")"""
    name =
    damage = 
    coins = 
    exp = 
    


    for enemy in enemies:
        if enemies["level"] == 1:
            print(f"A {"name"} has appeared!")
                

    
    
            
    
# when player finishes game, print whalen
# easter egg: if player types "Whalen" in choice, print evil whalen
       







""" while battle_sequence == True:
    while enemy_health > 0:
        #Select random enemy from enemy list in current district
        turn + 1 
        while turn == odd:
            print (#available moves)
            player_attack = input("what move would you like to use?: ")
            #if move is in list of moves:
            #    preform the move on the enemy
            #    turn + 1
            #else:
            #    print("Sorry that isn't a valid move... You can use these moves here: ")
            #    print (#available moves)
            #   player_attack = input("what move would you like to use?: ")
        
        while turn == even:
            Allow the enemy to attack
            turn + 
      else:
        print(enemy name' Has been defeeated! ) """  