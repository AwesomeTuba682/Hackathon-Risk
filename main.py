from Board import *
from Tile import *

board = Board(5, 6)
board.set(2, 3, Tile("sharmiland", 5, 1))
print(board)

print(board.capture(1, board.get(2, 3), board.get(1, 3), 3))
print(board.move(1, board.get(2, 3), board.get(1, 3), 1))
print(board)