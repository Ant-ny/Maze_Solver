from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
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
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            left_l = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_l)
        else:
            left_l = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_l, "white")
        if self.has_bottom_wall:
            top_l = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(top_l)
        else:
            top_l = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(top_l, "white")
        if self.has_right_wall:
            right_l = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(right_l)
        else:
            right_l = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(right_l, "white")
        if self.has_top_wall:
            bottom_l = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
            self._win.draw_line(bottom_l)
        else:
            bottom_l = Line(Point(self._x2, self._y1), Point(self._x1, self._y1))
            self._win.draw_line(bottom_l, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        center_x1 = (self._x1 + self._x2) / 2
        center_y1 = (self._y1 + self._y2) / 2
        center_x2 = (to_cell._x1 + to_cell._x2) / 2
        center_y2 = (to_cell._y1 + to_cell._y2) / 2
        if undo is False:
            point1 = Point(center_x1, center_y1)
            point2 = Point(center_x2, center_y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "red")
        elif undo:
            point1 = Point(center_x1, center_y1)
            point2 = Point(center_x2, center_y2)
            line = Line(point1, point2)
            self._win.draw_line(line, "gray")