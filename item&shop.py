class Allitems:

    def Level_2_key(name, Class, ability, description, level):
        name = 'Level 2 Key'
        Class = 'item'
        ability = 'open'
        description = 'A mysterious key shrouded in power. Can be used to access LEVEL 2'
        level = 1

    def Level_3_key(name, Class, ability, description, level):
        name = 'Level 3 Key'
        Class = 'item'
        ability = 'open'
        description = 'A key overflowing with power. Can be used to access LEVEL 3'
        level = 2

    def Hot_Coals(name, damage, type, level, ability, cost):
        name = 'Hot Coals'
        damage = 20
        type = 'fire'
        level = 1
        ability = 'burn'
        cost = 800

    def Hydrophilic(name, damage, type, level, ability, cost):
        name = 'Hydrophilic'
        damage = 25
        type = 'water'
        level = 1
        ability = 'weaken'
        cost = 500

    def Gorlocks_Stomp(name, damage, type, level, ability, cost):
        name = 'Gorlocks Stomp'
        damage = 40
        type = 'earth'
        level = 1
        ability = 'stun'
        cost = 1000

    def Eat(name, damage, type, level, ability, cost):
        name = 'Eat'
        damage = 5
        type = 'food'
        level = 2
        ability = 'heal'
        cost = 0

    def Fireball(name, damage, type, level, ability, cost):
        name = 'Fireball'
        damage = 100
        type = 'fire'
        level = 2
        ability = 'burn'
        cost = 3000

    def Hydro_Pressure_Canon(name, damage, type, level, ability, cost):
        name = 'Hydro-Pressure Canon'
        damage = 300
        type = 'water'
        level = 2
        ability = 'weaken'
        cost = 4000

    def Ground_Split(name, damage, type, level, ability, cost):
        name = 'Ground Split'
        damage = 150
        type = 'earth'
        level = 2
        ability = 'stun'
        cost = 4000

    def Shadow_Spear(name, damage, type, level, ability, cost):
        name = 'Shadow Spear'
        damage = 500
        type = 'dark'
        level = 2
        ability = 'none'
        cost = 5500

    def Dark_Domain(name, damage, type, level, ability, cost):
        name = 'Dark Domain'
        damage = 500
        type = 'dark'
        level = 3
        ability = 'blind'
        cost = 0

    def Pyrokinesis(name, damage, type, level, ability, cost):
        name = 'Pyrokinesis'
        damage = 400
        type = 'fire'
        level = 3
        ability = 'burn'
        cost = 10000

    def Bullet_Rain(name, damage, type, level, ability, cost):
        name = 'Bullet Rain'
        damage = 1000
        type = 'fire'
        level = 3
        ability = 'weaken'
        cost = 15000

    def Earth_Shatter(name, damage, type, level, ability, cost):
        name = 'Earth Shatter'
        damage = 700
        type = 'fire'
        level = 3
        ability = 'stun'
        cost = 15000

    def Black_Hole(name, damage, type, level, ability, cost):
        name = 'Black Hole'
        damage = 2000
        type = 'dark'
        level = 3
        ability = 'none'
        cost = 20000

import json

test = open("stuff.json", encoding="utf8")

data = json.load(test)


def shop(shopLevel, playerMoney, playerInventor):
    if shopLevel == 1:
        shopKey = Allitems.Level_2_key
        FireSpell = Allitems.Hot_Coals
        WaterSpell = Allitems.Hydrophilic
        EarthSpell = Allitems.Gorlocks_Stomp
    elif shopLevel == 2:
        shopKey = Allitems.Level_3_key
        FireSpell = Allitems.Fireball
        WaterSpell = Allitems.Hydro_Pressure_Canon
        EarthSpell = Allitems.Ground_Split
        DarkSpell = Allitems.Shadow_Spear
    elif shopLevel == 3:
        FireSpell = Allitems.Pyrokinesis
        WaterSpell = Allitems.Bullet_Rain
        EarthSpell = Allitems.Earth_Shatter
        DarkSpell = Allitems.Black_Hole

    shopFormat = {shopKey : shopKey(),
                  FireSpell : FireSpell(),
                  WaterSpell : WaterSpell(),
                  EarthSpell : EarthSpell(),
                  DarkSpell : DarkSpell()}

    buy = (playerMoney - buyChoice())
    
    choice = input('what would you like to buy?(1/2/3/4/5): ')
    print(shopFormat)
    if choice == '1':
        buyChoice = shopKey()
    elif choice == '2':
        buyChoice = FireSpell()
    elif choice == '3':
        buyChoice = WaterSpell()
    elif choice == '4':
        buyChoice = EarthSpell()
    elif choice == '5':
        buyChoice = DarkSpell()