import time, os

def clear():
    os.system('cls')

class Player:
    def __init__(self, name) -> None:
        self.name = name
    
    def NewPlayer(self):
        PlayerData = {
            "Name": self.name,
            "Level": 0,
            "UnlockLevel": 0,
            "Inventory": [],
            "Exp": 0,
            "Money": 0
        }