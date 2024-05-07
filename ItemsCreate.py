import json
import os
#item attributes: damage, cost, defense, durability, usage(description)



class Weapons():
    def __init__(self, name, damage, ability):
        self.name = name
        self.damage = damage
        self.ability = ability
    def __str__(self):
        return(f'{self.name,self.damage,self.ability}')

class Shield:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
    def __str__(self):
        return(f'{self.name,self.defense}')

class Items:
    def __init__(self, name, ability, description):
        self.name = name
        self.ability = ability
        self.description = description
    def __str__(self):
        return(f'{self.name,self.ability,self.description}')
    

with open("data.json", "r") as f:

    data = json.load(f)
 
""" Open = input('open?: ')
if Open == 'Y':
    name = input('name: ')
    damage = input('damage: ')
    level = input('level: ')
    x = Weapons(name, damage, level)
    AddMore = input('open more?: ')
    while AddMore == 'Y':
        data.append(x.__dict__)
        name = input('name: ')
        damage = input('damage: ')
        level = input('level: ')
        x = Weapons(name, damage, level)
    AddMore = input('open?: ')
    if AddMore == 'N':
        data.append(x.__dict__) """

Open = input('open?: ')
if Open == 'Y':
    name = input('name: ')
    ability = input('ability: ')
    description = input('description: ')
    x = Items(name, ability, description)
    AddMore = input('open more?: ')
    while AddMore == 'Y':
        data.append(x.__dict__)
        name = input('name: ')
        ability = input('ability: ')
        description = input('description: ')
        x = Items(name, ability, description)
    AddMore = input('open?: ')
    if AddMore == 'N':
        data.append(x.__dict__)



#----------------------------------------------------------------------
new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(data)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")