import dataclasses
from typing import List, Tuple
from pathlib import Path
from octopus import Octopus, Coord

import numpy as np
from collections import deque


class InvalidStateError(Exception):
    pass


def read_file(name) -> List[Octopus]:
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    lines: List[str] = []
    with open(file_path) as f:
        for line in f:
            line = line.rstrip('\n')
            lines.append(line)

    max_row = len(lines)
    max_col = len(lines[0])

    octopus_list: List[Octopus] = []
    for row in range(max_row):
        line = list(lines[row])
        for i in range(len(line)):
            octopus = Octopus(int(line[i]), Coord(row, i))
            octopus_list.append(octopus)

    for octopus in octopus_list:
        neighbour_coords = octopus.coord.get_neighbours(max_row, max_col)
        neighbours = [n for n in octopus_list if n.coord in neighbour_coords]
        octopus.set_neighbours(neighbours)

    return octopus_list

def algo_1(octopus_list: List[Octopus]):
    for i in range(100):
        for o in octopus_list:
            o.increase_energy()
        for o in octopus_list:
            o.reset_step()

    flash_count = 0
    for o in octopus_list:
        flash_count += o.flash_count

    return flash_count

def algo_2(octopus_list: List[Octopus]):
    step = 0
    while True:
        step += 1
        for o in octopus_list:
            o.increase_energy()

        flashed = [o.flashed for o in octopus_list]
        if all(flashed):
            return step

        for o in octopus_list:
            o.reset_step()



if __name__ == '__main__':
    file = 'example.txt'
    my_list = read_file(file)
    print(algo_1(my_list))
    my_list_2 = read_file(file)
    print(algo_2(my_list_2))
