import pygame
import sys

class BoardVisualizer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['' for _ in range(width)] for _ in range(height)]
        self.cell_size = 50
        self.screen = pygame.display.set_mode((width * self.cell_size, height * self.cell_size))
        pygame.init()

    def draw_board(self):
        self.screen.fill((255, 255, 255))  # Fill screen with white color
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.screen, (0, 0, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size), 1)  # Draw grid lines
                if self.board[y][x]:
                    pygame.draw.circle(self.screen, (255, 0, 0), (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2), self.cell_size // 3)  # Draw a red circle for occupied cells
        pygame.display.flip()

    def update_board(self, board):
        self.board = board
        self.draw_board()

if __name__ == "__main__":
    visualizer = BoardVisualizer(10, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()