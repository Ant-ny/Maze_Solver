from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            left_l = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_l)
        if self.has_bottom_wall:
            top_l = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(top_l)
        if self.has_right_wall:
            right_l = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(right_l)
        if self.has_top_wall:
            bottom_l = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
            self._win.draw_line(bottom_l)