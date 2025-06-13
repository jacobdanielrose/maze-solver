import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_empy(self):
        num_cols = 0
        num_rows = 0
        with self.assertRaisesRegex(ValueError, 'Number of columns and rows must be non-zero'):
            Maze(0, 0, num_rows, num_cols, 10, 10)

        num_cols = 0
        num_rows = 1
        with self.assertRaisesRegex(ValueError, 'Number of columns and rows must be non-zero'):
            Maze(0, 0, num_rows, num_cols, 10, 10)

        num_cols = 1
        num_rows = 0
        with self.assertRaisesRegex(ValueError, 'Number of columns and rows must be non-zero'):
            Maze(0, 0, num_rows, num_cols, 10, 10)


if __name__ == "__main__":
    unittest.main()
