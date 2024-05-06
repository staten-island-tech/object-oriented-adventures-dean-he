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
    

with open("data.json", "r", "UTF-8") as f:

    data = json.load(f)
 
while True:
    Open = input('Would you like to add a fighting style?: ')
    if Open == 'Y':
        name = input('name: ')
        damage = input('damage: ')
        ability = input('abiity: ')
        x = Weapons(name, damage, ability)
        AddMore = input('Do you want to add another fighting style?(Y/N): ')
        while AddMore == 'Y':
            data.append(x.__dict__)
            name = input('name: ')
            damage = input('damage: ')
            ability = input('abiity: ')
            x = Weapons(name, damage, ability)
        AddMore = input('Do you want to add another fighting style?(Y/N): ')
        if AddMore == 'N':
            data.append(x.__dict__)
            break




#----------------------------------------------------------------------
new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(data)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")