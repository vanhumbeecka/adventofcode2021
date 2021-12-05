from typing import Tuple, List

import numpy as np


class Line:
    def __init__(self, coord1: Tuple[int, int], coord2: Tuple[int, int]):
        self.coord1 = coord1
        self.coord2 = coord2

    def __repr__(self):
        return f"<Line {self.coord1}->{self.coord2}>"

    @property
    def x1(self):
        return self.coord1[0]

    @property
    def y1(self):
        return self.coord1[1]

    @property
    def x2(self):
        return self.coord2[0]

    @property
    def y2(self):
        return self.coord2[1]

    @property
    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    def all_coordinates(self) -> List[Tuple[int, int]]:
        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1
        sign_x = 0
        sign_y = 0
        if delta_x > 0:
            sign_x = 1
        elif delta_x < 0:
            sign_x = -1
        if delta_y > 0:
            sign_y = 1
        elif delta_y < 0:
            sign_y = -1

        internal_coords: List[Tuple[int, int]] = []
        delta_max = max(abs(delta_x), abs(delta_y))
        for i in range(abs(delta_max)+1):
            internal_coords.append((self.x1 + i*sign_x, self.y1 + i*sign_y))
        return internal_coords


class Grid:
    def __init__(self, lines: List[Line], allow_diagonal=False):
        if not allow_diagonal:
            self.lines = [line for line in lines if not line.is_diagonal]
        else:
            self.lines = lines

        self.max_x = 0
        self.max_y = 0
        for line in lines:
            self.max_x = line.x1 if line.x1 > self.max_x else self.max_x
            self.max_x = line.x2 if line.x2 > self.max_x else self.max_x
            self.max_y = line.y1 if line.y1 > self.max_y else self.max_y
            self.max_y = line.y2 if line.y2 > self.max_y else self.max_y

        self.max_x += 1
        self.max_y += 1

        self.marker = np.zeros((self.max_x, self.max_y), dtype=int)

    def __repr__(self):
        return f"<Grid ({self.max_x, self.max_y})>"

    def calculate(self):
        for line in self.lines:
            coords = line.all_coordinates()
            for coord in coords:
                self.marker[coord[0]][coord[1]] += 1

        strip = np.where(self.marker >= 2, 1, 0)
        return np.sum(strip, axis=None)


