from graphics import Line, Point
from typing_extensions import Union

class Cell():
    def __init__(self, win=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def draw(self, x1: Union[float, int], y1: Union[float, int], x2: Union[float, int], y2: Union[float, int]) -> None:
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")


    def draw_move(self, to_cell, undo=False) -> None:
        self_center_x = (self.__x2 + self.__x1) / 2
        self_center_y = (self.__y2 + self.__y1) / 2
        to_center_x = (to_cell.__x2 + to_cell.__x1) / 2
        to_center_y = (to_cell.__y2 + to_cell.__y1) / 2
        line = Line(Point(self_center_x, self_center_y), Point(to_center_x, to_center_y))
        if self.__win is None:
            return
        if not undo:
            self.__win.draw_line(line,fill_color="red")
        else:
            self.__win.draw_line(line, fill_color="gray")
