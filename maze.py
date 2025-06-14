from cell import Cell
from time import sleep
from typing_extensions import Union
import random

class Maze():
    def __init__(
            self,
            x1: Union[int, float],
            y1: Union[int, float],
            num_rows: int,
            num_cols: int,
            cell_size_x: Union[int, float],
            cell_size_y: Union[int, float],
            win = None,
            seed = None
        ) -> None:
        if num_rows < 1 or num_cols < 1:
            raise ValueError("Number of columns and rows must be non-zero")
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

        if seed is not None:
            random.seed(seed)

    def __create_cells(self) -> None:
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i,j)

    def __draw_cell(self, col: int, row: int) -> None:
        if self.__win is None:
            return
        x1 = self.__cell_size_x * col + self.__x1
        y1 = self.__cell_size_y * row + self.__y1
        y2 = y1 + self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        self.__cells[col][row].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self) -> None:
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(0.0005)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)

        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1,self.__num_rows-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            if i+1 < self.__num_cols and not self.__cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if j+1 < self.__num_rows and not self.__cells[i][j+1].visited:
                to_visit.append((i,j+1))
            if i-1 >= 0 and not self.__cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if j-1 >= 0 and not self.__cells[i][j-1].visited:
                to_visit.append((i,j-1))

            if not to_visit:
                self.__draw_cell(i,j)
                return

            direction = random.choice(to_visit)
            next_i,next_j = direction

            if next_i == i+1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False
            if next_i == i-1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False
            if next_j == j+1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False
            if next_j == j-1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False

            self.__break_walls_r(next_i,next_j)

    def __reset_cells_visited(self) -> None:
        for col in self.__cells:
            for cell in col:
                cell.visited = False
