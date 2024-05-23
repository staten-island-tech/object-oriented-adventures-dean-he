import json, random, time, os

# Open the JSON file of pokemon data
test = open("enemies.json", "uft8")
# create variable "data" that represents the enitre pokedex list
enemies = json.load(test)





class districts():
    def District1():
        enemys = []
        for enemy in enemies:
            if enemies["level"] == 1:
                enemys.append["name", "health", "damage", "coins", "exp", "type", "level", "boss"]
        select = random.choice[enemys]
        print(select)

    District1()

        
        
        

    def District2():
        enemys = []
        for enemy in enemies:
            if enemies["level"] == 2:
                enemys.append["name"]
                
    def District3():
        enemys = []
        for enemy in enemies:
            if enemies["level"] == 3:
                enemys.append["name"]

