import os, time, json

with open('JsonFiles\ShopItems.json', mode='r') as infile:
    Data = json.load(infile)

with open('JsonFiles\PlayerData.json', mode='r') as infile:
    Data2 = json.load(infile)

def clear():
    os.system('cls')

def Shop():
    print("Welcome to the Shop!")
    time.sleep(1)
    print("These are for sale: ")
    
    Shoplvl = 1

    PlayerMoney = 5000
    
    if Shoplvl == 1:
        print('Level 2 Key : 4000')
        print('Hot Coals : 500')
        print('Hydrophilic : 700')
        print('Gorlocks Stomp : 1000')
        buy = input('Input: 1/2/3/4: ')
        if buy == '1':
            for ShopItems in Data:
                if PlayerMoney >= 4000:
                    for PlayerData in Data2:
                        PlayerData["Inventory"].append(ShopItems["Key"])
                else:
                    print('You do not have enough money')

        if buy == '2':
            for ShopItems in Data:
                if PlayerMoney >= 500:
                    for PlayerData in Data2:
                        PlayerData["Inventory"].append(ShopItems["Fire"])
                else:
                    print('You do not have enough money')

Shop()

""" lvl = 1
for ShopItems in Data:
    if lvl == ShopItems["LevelReq"]:
        print(ShopItems["Fire"])
        print("Fire"["cost"]) """