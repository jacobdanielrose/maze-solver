from tkinter import Tk, BOTH, Canvas
from typing_extensions import Union

class Point():
    def __init__(self, x: Union[float, int], y: Union[float, int]) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas : Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_color,
            width=2
        )

class Window():
    def __init__(self, width: Union[str, float], height: Union[str, float]) -> None:
       self.__root = Tk()
       self.__root.title("Maze Solver")
       self.__root.protocol("WM_DELETE_WINDOW", self.close)
       self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
       self.__canvas.pack(fill=BOTH, expand=1)
       self.__running = False


    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)

    def close(self) -> None:
        self.__running = False
