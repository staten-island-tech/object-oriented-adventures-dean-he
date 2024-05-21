import json, random, time, os

# Open the JSON file of pokemon data
test = open("enemies.json", "uft8")
# create variable "data" that represents the enitre pokedex list
enemies = json.load(test)

