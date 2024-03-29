import pygame
import sys
from Board import *


class BoardVisualizer:
    colors = {
        0: (0, 0, 0),  # black
        1: (255, 255, 255),  # white
        2: (255, 0, 0),  # red
        3: (0, 255, 0),  # green
        4: (0, 0, 255),  # blue
        5: (255, 255, 0),  # yellow
        6: (255, 0, 255),  # magenta
        7: (0, 255, 255),  # cyan
        8: (125, 0, 0),  # dark red
        9: (0, 125, 0),  # dark green
        10: (0, 0, 125),  # dark blue
        11: (125, 125, 0),  # dark yellow
        12: (125, 0, 125),  # dark purple
        13: (0, 125, 125),  # dark cyan
        14: (139, 69, 19),  # brown
        15: (255, 192, 203),  # pink
        16: (255, 165, 0)  # orange
    }

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
                pygame.draw.rect(self.screen, (125, 125, 125), rect, 0)

                # white grid
                rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)

                # numbers
                font = pygame.font.SysFont('arial', 50)
                text = font.render(f"{self.board.get(j, i).power}", True, (0, 0, 0))
                self.screen.blit(text, (i * self.cell_size, j * self.cell_size))
