import os, time, json

with open('JsonFiles\ShopItems.json', mode='r') as infile:
    Data = json.load(infile)

with open('JsonFiles\PlayerData.json', mode='r') as infile:
    Data2 = json.load(infile)


def clear():
    os.system('cls')

def shop():
    Shoplvl = 1
    for ShopItems in Data:
        if Shoplvl == ShopItems["LevelReq"]:
            print(ShopItems["Items"])

    print('What would you like buy')

shop()