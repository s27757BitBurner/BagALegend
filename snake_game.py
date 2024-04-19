import pygame
import sys
import time

# Game settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
        self.direction = pygame.K_RIGHT

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        if self.direction == pygame.K_UP:
            self.positions.insert(0, (cur[0], cur[1]-GRID_SIZE))
        elif self.direction == pygame.K_DOWN:
            self.positions.insert(0, (cur[0], cur[1]+GRID_SIZE))
        elif self.direction == pygame.K_LEFT:
            self.positions.insert(0, (cur[0]-GRID_SIZE, cur[1]))
        elif self.direction == pygame.K_RIGHT:
            self.positions.insert(0, (cur[0]+GRID_SIZE, cur[1]))
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, GREEN, (p[0], p[1], GRID_SIZE, GRID_SIZE))

def draw_grid(surface):
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.rect(surface, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                snake.direction = event.key

        snake.move()

        surface.fill((0, 0, 0))
        snake.draw(surface)
        draw_grid(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(12)

if __name__ == "__main__":
    main()
