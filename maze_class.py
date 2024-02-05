from cells import Cell
import time


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)    

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell_x = self.x1 + i * self.cell_size_x
        cell_y = self.y1 + j * self.cell_size_y
        cell_x2 = cell_x + self.cell_size_x
        cell_y2 = cell_y + self.cell_size_y
        cell.draw(cell_x, cell_y, cell_x2, cell_y2)
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(.05)