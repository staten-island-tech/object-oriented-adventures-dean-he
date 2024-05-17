import json

test = open("stuff.json", encoding="utf8")

data = json.load(test)


class shop:

    def shop1():
        access = input('Would you like to use the shop?(Y/N): ')
        if access == 'y' or 'Y':
            x = '1'

            for stuff in data:
                if x in stuff["level"]:
                    print (stuff["name"])

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
    if stuff['level'] == '1' or '2' or '3':
        y = stuff['level']
        if y == '1':
            shop.shop1
        elif y == '2':
            shop.shop2
        elif y == '3':
            shop.shop3
