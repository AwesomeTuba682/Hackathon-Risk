from Tile import *
from Player import *

class Board:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = [[Tile("", 0, -1) for j in range(m)] for i in range(n)]
        self.calc_neighbors()


    def get(self, i, j):
        return self.board[i][j]

    def set(self, i, j, tile: Tile):
        self.board[i][j] = tile
        self.calc_neighbors()

    def calc_neighbors(self):
        for i in range(self.n):
            for j in range(self.m):
                self.board[i][j].neighbors.append(self.board[(i + 1) % self.n][j])
                self.board[i][j].neighbors.append(self.board[(i - 1) % self.n][j])
                self.board[i][j].neighbors.append(self.board[i][(j + 1) % self.m])
                self.board[i][j].neighbors.append(self.board[i][(j - 1) % self.m])

    def place(self, player, tile, troops_to_place):
        if tile.owner != player.id and tile.owner != -1:
            return "this is not your tile or an empty tile"

        if troops_to_place > player.available_troops:
            return "you don't have enough units"

        tile.power += troops_to_place
        player.available_troops -= troops_to_place
        tile.owner = player.id
        return True

    def move(self, mover: Player, from_tile, to_tile, troops_to_transfer):
        if mover.id != from_tile.owner:
            # moving units from a tile that
            # doesn't belong to the player
            return "this is not your tile"

        if from_tile.owner != to_tile.owner:
            # moving units to a non-friendly tile
            return "this tile doesn't belong to you   "

        # if to_tile not in from_tile.neighbors:
        #     # moving units to a tile that
        #     # isn't a neighbor
        #     return "this tile isn't close enough"

        if troops_to_transfer > from_tile.power - 1:
            # attempting to move too many units
            return "you don't have enough power"

        from_tile.power -= troops_to_transfer
        to_tile.power += troops_to_transfer
        return True

    def capture(self, attacker: Player, attacking_tile, defending_tile, troops_to_transfer):
        if attacker.id != attacking_tile.owner:
            # attacking with a tile that
            # doesn't belong to the attacker
            return "this is not your tile"

        if attacking_tile.owner == defending_tile.owner:
            # attempting to attack a friendly tile
            return "this tile belongs to you"

        if defending_tile not in attacking_tile.neighbors:
            # attacking a tile that isn't
            # a neighbor
            return "this tile isn't close enough"

        if troops_to_transfer > attacking_tile.power - 1:
            # attempting to attack with more units than possible
            return "you don't have enough power"

        if troops_to_transfer == defending_tile.power:
            attacking_tile.power -= troops_to_transfer
            defending_tile.power = 1
            return True

        if troops_to_transfer > defending_tile.power:
            attacking_tile.power -= troops_to_transfer
            defending_tile.power = troops_to_transfer - defending_tile.power
            defending_tile.owner = attacking_tile.owner
            return True

        attacking_tile.power -= troops_to_transfer
        defending_tile.power -= troops_to_transfer
        return True

    def __str__(self):
        str = ""

        for line in self.board:
            for tile in line:
                str += tile.__str__()
            str += '\n'

        return str
