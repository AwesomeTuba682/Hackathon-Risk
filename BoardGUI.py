import pygame
import sys
from Board import *

class BoardVisualizer:
    def __init__(self, board: Board):
        self.board = board
        self.cell_size = 100
        self.screen = pygame.display.set_mode((self.board.m * self.cell_size, self.board.n * self.cell_size))
        self.colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255))
        pygame.init()

    def draw_board(self):
        self.screen.fill((255, 255, 255))  # Fill screen with white color
        for j in range(self.board.n):
            for i in range(self.board.m):
                # colored rectangles
                rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.colors[self.board.get(j, i).owner], rect, 0)

                # white grid
                rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)

                # numbers
                font = pygame.font.SysFont('arial', 50)
                text = font.render(f"{self.board.get(j, i).power}", True, (0, 0, 0))
                self.screen.blit(text, (i * self.cell_size, j * self.cell_size))


if __name__ == "__main__":
    board = Board(6, 10)
    board.set(5, 9, Tile("lol", 10, 2))
    visualizer = BoardVisualizer(board)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        visualizer.draw_board()
        pygame.display.update()