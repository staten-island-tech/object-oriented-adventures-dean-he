class player:
    def __init__(self, name, health, moves,  level, money, playerhealth):
        self.name = name
        self.health = health
        self.moves = moves
        self.level = level
        self.money = money
        def __str__(self):
            return f"{self.name}{self.moves}"



