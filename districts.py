import json, random, time, os

# Open the JSON file of pokemon data
test = open("enemies.json", "uft8")
# create variable "data" that represents the enitre pokedex list
enemies = json.load(test)

def District1():
    enemys = []
    for enemy in enemies:
        if enemies["level"] == 1:
            enemys.append["name"]
    print(enemys)

District1()

