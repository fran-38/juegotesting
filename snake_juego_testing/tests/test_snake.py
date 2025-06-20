import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def test_start_position(self):
        s = Snake()
        self.assertEqual(s.head(), [100, 50])

    def test_move(self):
        s = Snake()
        s.move()
        self.assertEqual(s.head(), [120, 50])

    def test_grow(self):
        s = Snake()
        old_len = len(s.body)
        s.grow()
        self.assertEqual(len(s.body), old_len + 1)

if __name__ == '__main__':
    unittest.main()
