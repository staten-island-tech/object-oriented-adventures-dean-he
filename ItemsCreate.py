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
    def __init__(self, name, ability, description, level, cost):
        self.name = name
        self.ability = ability
        self.description = description
        self.level = level
        self.cost = cost
    def __str__(self):
        return(f'{self.name,self.ability,self.description,self.level,self.cost}')
    
class Spells:
    def __init__(self, name, damage, type, level, ability, cost):
        self.name = name
        self.damage = damage
        self.type = type
        self.level = level
        self.ability = ability
        self.cost = cost
    def __str__(self):
        return(f'{self.name,self.damage,self.type,self.level,self.ability, self.cost}')
    

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

""" Open = input('open?: ')
if Open == 'Y':
    name = input('name: ')
    ability = input('ability: ')
    description = input('description: ')
    level = input('level: ')
    x = Items(name, ability, description, level)
    AddMore = input('open more?: ')
    while AddMore == 'Y':
        data.append(x.__dict__)
        name = input('name: ')
        ability = input('ability: ')
        description = input('description: ')
        level = input('level: ')
        x = Items(name, ability, description, level)
    AddMore = input('open?: ')
    if AddMore == 'N':
        data.append(x.__dict__) """

Open = input('open?: ')
if Open == 'Y':
    name = input('name: ')
    damage = input('dmg: ')
    type = input('type: ')
    level = input('level: ')
    ability = input('ability: ')
    cost = input('cost: ')
    x = Spells(name, damage, type, level, ability, cost)
    AddMore = input('open more?: ')
    while AddMore == 'Y':
        data.append(x.__dict__)
        name = input('name: ')
        type = input('type: ')
        level = input('level: ')
        ability = input('ability: ')
        cost = input('cost: ')
        x = Spells(name, damage, type, level, ability, cost)
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