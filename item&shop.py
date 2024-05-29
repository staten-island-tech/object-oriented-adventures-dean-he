""" import json

test = open("stuff.json", encoding="utf8")

data = json.load(test) """

""" class shop:

    def shop1():
        access = input('Would you like to use the shop?(Y/N): ')
        if access == 'y' or 'Y':
            x = '1'

            for stuff in data:
                if x in stuff["level"]:
                    print (stuff["name"])
                    buy = input('What would you like to buy?')
                    if buy in stuff["name"]:
                        confirm = input('Would you like to buy '+stuff["name"]+'?(y/n)')
                        if confirm == 'n' or 'N':
                            shop.shop1
                        elif confirm == 'y' or 'Y':
                            inv.append(stuff["name"])
                            print('You have bought '+stuff["name"])




    def shop2():
        access = input('Would you like to use the shop?(Y/N): ')
        if access == 'y' or 'Y':
            x = '2'

            for stuff in data:
                if x in stuff["level"]:
                    print (stuff["name"])

    def shop3():
        access = input('Would you like to use the shop?(Y/N): ')
        if access == 'y' or 'Y':
            x = '3'

            for stuff in data:
                if x in stuff["level"]:
                    print (stuff["name"])

for stuff in data:
    if stuff["level"] == '1' or '2' or '3':
        y = stuff['level']
        if y == '1':
            shop.shop1
        elif y == '2':
            shop.shop2
        elif y == '3':
            shop.shop3 """

from Allitems import Allitems



def Level_2_key(Class, ability, description, level):
    Class = 'item'
    ability = 'open'
    description = 'A mysterious key shrouded in power. Can be used to access LEVEL 2'
    level = 1

def Level_3_key(Class, ability, description, level):
    Class = 'item'
    ability = 'open'
    description = 'A key overflowing with power. Can be used to access LEVEL 3'
    level = 2

def Hot_Coals(damage, type, level, ability, cost):
    damage = 20
    type = 'fire'
    level = 1
    ability = 'burn'
    cost = 800

def Hydrophilic(damage, type, level, ability, cost):
    damage = 25
    type = 'water'
    level = 1
    ability = 'weaken'
    cost = 500

def Gorlocks_Stomp(damage, type, level, ability, cost):
    damage = 40
    type = 'earth'
    level = 1
    ability = 'stun'
    cost = 1000

def Eat(damage, type, level, ability, cost):
    damage = 5
    type = 'food'
    level = 2
    ability = 'heal'
    cost = 0

def Fireball(damage, type, level, ability, cost):
    damage = 100
    type = 'fire'
    level = 2
    ability = 'burn'
    cost = 3000

def Hydro_Pressure_Canon(damage, type, level, ability, cost):
    damage = 300
    type = 'water'
    level = 2
    ability = 'weaken'
    cost = 4000

def Ground_Split(damage, type, level, ability, cost):
    damage = 150
    type = 'earth'
    level = 2
    ability = 'stun'
    cost = 4000

def Shadow_Spear(damage, type, level, ability, cost):
    damage = 500
    type = 'dark'
    level = 2
    ability = 'none'
    cost = 5500

def Dark_Domain(damage, type, level, ability, cost):
    damage = 500
    type = 'dark'
    level = 3
    ability = 'blind'
    cost = 0

def Pyrokinesis(damage, type, level, ability, cost):
    damage = 400
    type = 'fire'
    level = 3
    ability = 'burn'
    cost = 10000

def Bullet_Rain(damage, type, level, ability, cost):
    damage = 1000
    type = 'fire'
    level = 3
    ability = 'weaken'
    cost = 15000

def Earth_Shatter(damage, type, level, ability, cost):
    damage = 700
    type = 'fire'
    level = 3
    ability = 'stun'
    cost = 15000

def Black_Hole(damage, type, level, ability, cost):
    damage = 2000
    type = 'dark'
    level = 3
    ability = 'none'
    cost = 20000



def shop(shopLevel, playerMoney, playerInventor):
    if shopLevel == 1:
        shopKey = Level_2_key
        FireSpell = Hot_Coals
        WaterSpell = Hydrophilic
        EarthSpell = Gorlocks_Stomp
    elif shopLevel == 2:
        shopKey = Level_3_key
        FireSpell = Fireball
        WaterSpell = Hydro_Pressure_Canon
        EarthSpell = Ground_Split
        DarkSpell = Shadow_Spear
    elif shopLevel == 3:
        FireSpell = Pyrokinesis
        WaterSpell = Bullet_Rain
        EarthSpell = Earth_Shatter
        DarkSpell = Black_Hole

    