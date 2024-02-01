from graphics import Window
from cells import Cell


def main():
    win = Window(800, 600)
    c = Cell(win)
    c.draw(100, 200, 300, 400)
    win.wait_for_close()

main()