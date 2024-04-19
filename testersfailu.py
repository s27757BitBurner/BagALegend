import unittest

class TestSnake(unittest.TestCase):
    def test_move(self):
        snake = Snake()
        initial_position = snake.get_head_position()
        snake.move()
        new_position = snake.get_head_position()
        self.assertNotEqual(initial_position, new_position)

if __name__ == "__main__":
    unittest.main()
