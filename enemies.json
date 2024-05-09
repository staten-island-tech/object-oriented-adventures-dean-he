






""" import json
import os
## Create Class for creating new dictionaries here

class enemies():
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





with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

while True:
    add = input('do you want add a enemy? Y/N: ').upper()
    if add == "Y":
        name = input("enemy name: ")
        health = int(input('health: '))
        damage = int(input('damage: '))
        coins = int(input('coins: '))
        exp = int(input('exp: '))
        type = input("type: ")
        level = int(input('level: '))
        boss = input("Y/N boss: ")
        y = enemies(name, health, damage, coins, exp, type, level, boss)
    elif add == "N":
        data.append(y.__dict__)
        break



#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")
 """







    

    

    
    

