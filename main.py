from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    line = Line(Point(100, 100), Point(700, 500))
    win.draw_line(line, "black")
    win.wait_for_close()

main()