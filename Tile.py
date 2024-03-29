class Tile:
    def __init__(self, name, power, owner):
        self.name = name
        self.power = power
        self.owner = owner
        self.neighbors = []

    def __str__(self):
        # return f"{self.name}, belongs to: {self.owner}"
        return f"{self.power} "