#item attributes: damage, cost, defense, durability, usage(description)

""" class items:
    def __init__(self, damage, cost, defense, durability, classification):
        self.damage = damage
        self.cost = cost
        self.defense = defense
        self.durability = durability
        self.classification = classification
    def __str__(self):
        return(f'{self.damage,self.cost,self.defense,self.durability,self.classification}')




while True:
    Open = input('Would you like to add a fighting style?: ')
    if Open == 'Y':
        name = input('Enter name: ')
        damage = input('Enter dmg: ')
        cost = input('Enter cost: ')
        defense = input('Enter def: ')
        durability = input('Enter dura: ')
        classification = input('Enter usage: ')
        x = items(name, damage, cost, defense, durability, classification)
        AddMore = input('Enter another item?(Y/N): ')
        while AddMore == 'Y':
            ItemsList.append(x.__dict__)
            name = input('Enter name: ')
            damage = input('Enter dmg: ')
            cost = input('Enter cost: ')
            defense = input('Enter def: ')
            durability = input('Enter dura: ')
            classification = input('Enter usage: ')
            x = items(name, damage, cost, defense, durability, classification)
            AddMore = input('Enter another item?(Y/N): ')
        if AddMore == 'N':
            data.append(x.__dict__)
            break """


""" class item:
    def __init__(self, damage, cost, defense, durability, classification):
        self.damage = damage
        self.cost = cost
        self.defense = defense
        self.durability = durability
        self.classification = classification
    def __str__(self):
        return(f'{self.damage,self.cost,self.defense,self.durability,self.classification}') """


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
    

