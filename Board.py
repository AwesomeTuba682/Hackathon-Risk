from Tile import *
from Player import *

class Board:

    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9,
             9, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 0, 3, 0, 0, 0, 0, 8, 8, 8, 0, 8, 9, 9, 9, 9, 9, 9, 9, 9,
             10, 10, 10, 10, 10, 10, 10, 10, 0],
            [5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 3, 3, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [0, 5, 0, 0, 5, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 1, 1,
             10, 10, 10, 10, 0, 10, 10, 0, 0],
            [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 16, 16, 9, 9, 9, 9, 1, 1, 1,
             1, 1, 1, 10, 0, 0, 10, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 16, 16, 16, 16, 16, 9, 9, 1, 1,
             1, 1, 1, 1, 1, 10, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 8, 16, 0, 16, 0, 16, 16, 16, 9, 1, 1,
             1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 11, 0, 0, 0, 16, 16, 16, 16, 16, 16, 1, 1,
             1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 11, 11, 11, 11, 11, 11, 11, 16, 16, 0, 16, 16, 16,
             13, 13, 13, 13, 13, 13, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 11, 11, 11, 11, 11, 0, 0, 16, 0, 0, 13, 13,
             13, 13, 13, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 11, 11, 11, 11, 12, 12, 12, 12, 12, 0, 0, 0, 13, 0,
             0, 13, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 0, 0, 0, 0,
             13, 13, 0, 0, 13, 13, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 12, 12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 13,
             0, 0, 0, 0, 13, 13, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 12, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0,
             13, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 6, 6, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 0, 15, 0, 0, 0, 0, 0, 0,
             0, 0, 14, 14, 14, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             14, 14, 14, 14, 14, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             14, 14, 14, 14, 14, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 14, 14, 0, 0, 14, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 14, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.n = len(self.board)
        self.m = len(self.board[0])

        # americas
        greenland = Tile("greenland", 2, -1)
        canada = Tile("canada", 3, -1)
        alaska = Tile("alaska", 1, -1)
        united_states = Tile("united states", 4, -1)
        argentina = Tile("argentina", 2, -1)
        northern_south_america = Tile("northern south america", 3, -1)

        # europe and asia
        europe = Tile("europe", 4, -1)
        middle_east = Tile("middle east", 3, -1)
        western_russia = Tile("western_russia", 3, -1)
        china = Tile("china", 3, -1)
        eastern_russia = Tile("eastern_russia", 3, -1)

        # africa
        north_africa = Tile("north africa", 2, -1)
        central_africa = Tile("central africa", 3, -1)
        south_africa = Tile("south africa", 1, -1)

        # misc
        indonesia = Tile("indonesia", 2, -1)
        australia = Tile("australia", 3, -1)
        empty_tile = Tile("empty", 0, -2)

        greenland.neighbors = [united_states, canada, europe]
        canada.neighbors = [alaska, united_states, greenland]
        alaska.neighbors = [eastern_russia, united_states, canada]
        united_states = [canada, alaska, greenland, northern_south_america]
        northern_south_america.neighbors = [north_africa, united_states, argentina]
        argentina.neighbors = [northern_south_america]

        europe.neighbors = [greenland, north_africa, middle_east, western_russia]
        middle_east.neighbors = [central_africa, north_africa, europe, western_russia, china, indonesia]
        western_russia.neighbors = [europe, middle_east, china, eastern_russia]
        china.neighbors = [western_russia, eastern_russia, middle_east, indonesia]
        eastern_russia.neighbors = [western_russia, china, alaska]

        north_africa.neighbors = [europe, middle_east, central_africa]
        central_africa.neighbors = [north_africa, middle_east, south_africa]
        south_africa.neighbors = [central_africa]

        indonesia.neighbors = [china, middle_east, australia]
        australia.neighbors = [indonesia]

        num_to_region = {
            0: empty_tile,
            1: china,
            2: canada,
            3: greenland,
            4: united_states,
            5: alaska,
            6: northern_south_america,
            7: argentina,
            8: europe,
            9: western_russia,
            10: eastern_russia,
            11: north_africa,
            12: central_africa,
            13: indonesia,
            14: australia,
            15: south_africa,
            16: middle_east
        }

        self.board = [[num_to_region[self.get(i, j)] for j in range(self.m)]for i in range(self.n)]

    def get(self, i, j):
        return self.board[i][j]

    def set(self, i, j, tile: Tile):
        self.board[i][j] = tile

    # def calc_neighbors(self):
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             self.board[i][j].neighbors.append(self.board[(i + 1) % self.n][j])
    #             self.board[i][j].neighbors.append(self.board[(i - 1) % self.n][j])
    #             self.board[i][j].neighbors.append(self.board[i][(j + 1) % self.m])
    #             self.board[i][j].neighbors.append(self.board[i][(j - 1) % self.m])

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
