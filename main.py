from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(16, 18), Point(200, 300))
    win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == '__main__':
   main()
