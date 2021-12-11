import dataclasses
from typing import List


@dataclasses.dataclass
class Coord:
    row: int
    col: int

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def get_neighbours(self, max_row: int, max_col: int):
        neighbours = [
            Coord(self.row - 1, self.col) if self.row > 0 else None,
            Coord(self.row - 1, self.col + 1) if self.row > 0 and self.col < max_col else None,
            Coord(self.row, self.col + 1) if self.col < max_col else None,
            Coord(self.row + 1, self.col + 1) if self.row < max_row and self.col < max_col else None,
            Coord(self.row + 1, self.col) if self.row < max_row else None,
            Coord(self.row + 1, self.col - 1) if self.row < max_row and self.col > 0 else None,
            Coord(self.row, self.col - 1) if self.col > 0 else None,
            Coord(self.row - 1, self.col - 1) if self.col > 0 and self.row > 0 else None
        ]

        return [i for i in neighbours if i is not None]



class Octopus:
    def __init__(self, energy: int, coord: Coord):
        self.coord = coord
        self.neighbours = []
        self.energy = energy
        self.flashed = False
        self.flash_count = 0

    def __repr__(self):
        return f"<Octopus energy={self.energy} {self.coord} neighbours={len(self.neighbours)} flash_count={self.flash_count}>"

    def set_neighbours(self, neighbours: List["Octopus"]):
        self.neighbours = neighbours

    def reset_step(self):
        self.flashed = False

    def _flash(self):
        self.energy = 0
        self.flashed = True
        self.flash_count += 1
        for neighbour in self.neighbours:
            neighbour.increase_energy()

    def increase_energy(self):
        if self.flashed:
            return

        if self.energy < 9:
            self.energy += 1
        else:
            self._flash()
