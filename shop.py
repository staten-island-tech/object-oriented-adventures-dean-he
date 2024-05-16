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


y = PlayerDistrict
if PlayerDistrict == '1':
    shop.shop1
elif PlayerDistrict == '2':
    shop.shop2
elif PlayerDistrict == '3':
    shop.shop3
