import unittest
import pygame

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_initial_head_position(self):
        self.assertEqual(self.snake.get_head_position(), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    def test_move_right(self):
        self.snake.direction = pygame.K_RIGHT
        self.snake.move()
        self.assertEqual(self.snake.get_head_position(), ((WINDOW_WIDTH // 2) + GRID_SIZE, WINDOW_HEIGHT // 2))

    def test_move_left(self):
        self.snake.direction = pygame.K_LEFT
        self.snake.move()
        self.assertEqual(self.snake.get_head_position(), ((WINDOW_WIDTH // 2) - GRID_SIZE, WINDOW_HEIGHT // 2))

    def test_move_up(self):
        self.snake.direction = pygame.K_UP
        self.snake.move()
        self.assertEqual(self.snake.get_head_position(), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - GRID_SIZE))

    def test_move_down(self):
        self.snake.direction = pygame.K_DOWN
        self.snake.move()
        self.assertEqual(self.snake.get_head_position(), (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + GRID_SIZE))

if __name__ == '__main__':
    unittest.main()
