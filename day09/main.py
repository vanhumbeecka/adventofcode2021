import dataclasses
from typing import List, Tuple
from pathlib import Path

import numpy as np


def read_file(name) -> np.array:
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    lines: List[List[int]] = []
    with open(file_path) as f:
        for line in f:
            line = list(map(int, list(line.rstrip('\n'))))
            lines.append(line)
    return np.array(lines)


def algo_1(input: np.array):
    count = 0

    row_mins = []
    for row in range(len(input)):
        for i in range(len(input[row])):
            if (i == 0 and input[row][i + 1] > input[row][i]) or \
                    (i == len(input[row]) - 1 and input[row][i - 1] > input[row][i]) or \
                    (input[row][i - 1] > input[row][i] and input[row][i + 1] > input[row][i]):
                if (row == 0 and input[row + 1][i] > input[row][i]) or \
                        (row == len(input) - 1 and input[row - 1][i] > input[row][i]) or \
                        (input[row - 1][i] > input[row][i] and input[row + 1][i] > input[row][i]):
                    row_mins.append(input[row][i])

    # print(row_mins)

    return (np.array(row_mins) + 1).sum()


@dataclasses.dataclass
class Coord:
    row: int
    col: int

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return f"({self.row}, {self.col})"


def find_min_coords(input) -> List[Coord]:
    coords = []
    for row in range(len(input)):
        for i in range(len(input[row])):
            if (i == 0 and input[row][i + 1] > input[row][i]) or \
                    (i == len(input[row]) - 1 and input[row][i - 1] > input[row][i]) or \
                    (input[row][i - 1] > input[row][i] and input[row][i + 1] > input[row][i]):
                if (row == 0 and input[row + 1][i] > input[row][i]) or \
                        (row == len(input) - 1 and input[row - 1][i] > input[row][i]) or \
                        (input[row - 1][i] > input[row][i] and input[row + 1][i] > input[row][i]):
                    coords.append(Coord(row, i))

    return coords


def basin(coords: List[Coord], input, search: List[Coord]):
    new_coords: List[Coord] = []
    for coord in search:
        # left
        if coord.col != 0 and input[coord.row][coord.col - 1] > input[coord.row][coord.col]:
            nw = Coord(coord.row, coord.col - 1)
            if nw not in new_coords and nw not in coords and input[nw.row][nw.col] != 9:
                new_coords.append(nw)

        # up
        if coord.row != 0 and input[coord.row - 1][coord.col] > input[coord.row][coord.col]:
            nw = Coord(coord.row - 1, coord.col)
            if nw not in new_coords and nw not in coords and input[nw.row][nw.col] != 9:
                new_coords.append(nw)

        # right
        if coord.col != len(input[0]) - 1 and input[coord.row][coord.col + 1] > input[coord.row][coord.col]:
            nw = Coord(coord.row, coord.col + 1)
            if nw not in new_coords and nw not in coords and input[nw.row][nw.col] != 9:
                new_coords.append(nw)

        # down
        if coord.row != len(input) - 1 and input[coord.row + 1][coord.col] > input[coord.row][coord.col]:
            nw = Coord(coord.row + 1, coord.col)
            if nw not in new_coords and nw not in coords and input[nw.row][nw.col] != 9:
                new_coords.append(nw)

    if new_coords:
        coords = coords + new_coords
        return basin(coords, input, new_coords)

    return coords


def algo_2(input):
    coords = find_min_coords(input)

    basins = []
    for coord in coords:
        basins_coords = basin([coord], input, [coord])
        # print(basins_coords)
        basins.append(len(basins_coords))

    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':
    my_list = read_file('input.txt')
    print(algo_1(my_list))
    print(algo_2(my_list))
