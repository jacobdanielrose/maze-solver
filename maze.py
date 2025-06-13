from cell import Cell
from time import sleep
from graphics import Window
from typing_extensions import Union

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
        
    