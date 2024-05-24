""" import json

test = open("stuff.json", encoding="utf8")

data = json.load(test) """

import Allitems

inv = []

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


def shop(shopLevel, playerMoney, playerInventor):
    if shopLevel == 1:
        shopKey = 
