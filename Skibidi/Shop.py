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

        Shoplvl = Data2["District"]

        PlayerMoney = Data2['Money']
        
        if Shoplvl == 1:
            print('Level 2 Key : 4000')
            print('Hot Coals : 500')
            print('Hydrophilic : 700')
            print('Gorlocks Stomp : 1000')
            buy = input('Input: 1/2/3/4: ')
            
            if buy == '1':
                if PlayerMoney > 4000:
                    print('You have bought Level 2 Key!')
                    Data2['Inventory'].append('Level 2 Key')
                    PlayerMoney = (PlayerMoney - 4000)
                elif PlayerMoney < 4000:
                    print('You do not have enough money')

            if buy == '2':
                if PlayerMoney > 500:
                    print('You have bought Hot Coals!')
                    Data2['Inventory'].append('Hot Coals')
                    PlayerMoney = (PlayerMoney - 500)
                elif PlayerMoney < 500:
                    print('You do not have enough money')

            if buy == '3':
                if PlayerMoney > 700:
                    print('You have bought Hydrophilic!')
                    Data2['Inventory'].append('Hydrophilic')
                    PlayerMoney = (PlayerMoney - 700)
                elif PlayerMoney < 700:
                    print('You do not have enough money')

            if buy == '4':
                if PlayerMoney > 1000:
                    print('You have bought Gorlocks Stomp!')
                    Data2['Inventory'].append('Gorlocks Stomp')
                    PlayerMoney = (PlayerMoney - 1000)
                elif PlayerMoney < 1000:
                    print('You do not have enough money')


        if Shoplvl == 2:
            print('Level 3 Key : 20000')
            print('Fireball : 3000')
            print('Ground Split : 3000')
            print('Hydro-pressure Cannon : 5000')
            print('Shadow Spear : 6000')
            buy = input('Input: 1/2/3/4/5: ')
            
            if buy == '1':
                if PlayerMoney > 20000:
                    print('You have bought Level 3 Key!')
                    Data2['Inventory'].append('Level 3 Key')
                    PlayerMoney = (PlayerMoney - 20000)
                elif PlayerMoney < 20000:
                    print('You do not have enough money')

            if buy == '2':
                if PlayerMoney > 3000:
                    print('You have bought Fireball!')
                    Data2['Inventory'].append('Fireball')
                    PlayerMoney = (PlayerMoney - 3000)
                elif PlayerMoney < 3000:
                    print('You do not have enough money')

            if buy == '3':
                if PlayerMoney > 3000:
                    print('You have bought Ground Split!')
                    Data2['Inventory'].append('Ground Shatter')
                    PlayerMoney = (PlayerMoney - 3000)
                elif PlayerMoney < 3000:
                    print('You do not have enough money')

            if buy == '4':
                if PlayerMoney > 5000:
                    print('You have bought Hydro-pressure Cannon!')
                    Data2['Inventory'].append('Hydro-pressure Cannon')
                    PlayerMoney = (PlayerMoney - 5000)
                elif PlayerMoney < 5000:
                    print('You do not have enough money')

            if buy == '5':
                if PlayerMoney > 6000:
                    print('You have bought Shadow Spear!')
                    Data2['Inventory'].append('Shadow Spear')
                    PlayerMoney = (PlayerMoney - 6000)
                elif PlayerMoney < 6000:
                    print('You do not have enough money')

        
        if Shoplvl == 3:
            print('Pyrokinesis : 10000')
            print('Earth Shatter : 15000')
            print('Bullet Rain : 15000')
            print('Black Hole : 20000')
            buy = input('Input: 1/2/3/4: ')
            
            if buy == '1':
                if PlayerMoney > 10000:
                    print('You have bought Pyrokinesis!')
                    Data2['Inventory'].append('Pyrokinesis')
                    PlayerMoney = (PlayerMoney - 10000)
                elif PlayerMoney < 10000:
                    print('You do not have enough money')

            if buy == '2':
                if PlayerMoney > 15000:
                    print('You have bought Ground Shatter!')
                    Data2['Inventory'].append('Ground Shatter')
                    PlayerMoney = (PlayerMoney - 15000)
                elif PlayerMoney < 15000:
                    print('You do not have enough money')

            if buy == '3':
                if PlayerMoney > 15000:
                    print('You have bought Bullet Rain!')
                    Data2['Inventory'].append('Bullet Rain')
                    PlayerMoney = (PlayerMoney - 15000)
                elif PlayerMoney < 15000:
                    print('You do not have enough money')

            if buy == '4':
                if PlayerMoney > 20000:
                    print('You have bought Black Hole!')
                    Data2['Inventory'].append('Black Hole')
                    PlayerMoney = (PlayerMoney - 20000)
                elif PlayerMoney < 20000:
                    print('You do not have enough money')

Shop()