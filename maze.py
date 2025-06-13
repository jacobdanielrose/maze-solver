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
            win: Window,
        ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self) -> None:
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))
                self.__draw_cell(i,j)

    def __draw_cell(self, col: int, row: int) -> None:
        cell = self.__cells[col][row]
        x1 = self.cell_size_x * col + self.x1
        x2 = x1 + self.cell_size_x
        y1 = self.cell_size_y * row + self.y1
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self) -> None:
        self.win.redraw()
        sleep(0.0005)
