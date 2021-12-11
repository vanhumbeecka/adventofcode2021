from typing import List
from pathlib import Path

import numpy as np

from line import Line, Grid

def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    my_list: List[Line] = []
    with open(file_path) as f:
        for line in f:
            coords_raw = line.rstrip('\n').split(" -> ")
            coords = [tuple(map(int, c.split(","))) for c in coords_raw]
            my_list.append(Line(*coords))
    return my_list

def algo_1(coords):
    grid = Grid(coords, allow_diagonal=False)
    return grid.calculate()


def algo_2(coords):
    grid = Grid(coords, allow_diagonal=True)
    return grid.calculate()


if __name__ == '__main__':
    coords = read_file('example.txt')
    print(algo_1(coords))
    print(algo_2(coords))