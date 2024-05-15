import json

test = open("stuff.json", encoding="utf8")

data = json.load(test)



def shop1():
    access = input('Would you like to use the shop?(Y/N): ')
    if access == 'y' or 'Y':
        x = '1'
        for stuff in data:
            if x == stuff["level"]:
                print(stuff["level"])

shop1()