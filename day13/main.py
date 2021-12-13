from dataclasses import dataclass
from typing import List, Tuple
from pathlib import Path
import numpy as np


class InvalidStateError(Exception):
    pass


@dataclass
class Coord:
    x: int
    y: int


def read_file(name) -> Tuple:
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    coords: List[Coord] = []
    folds: List[Tuple[str, int]] = []
    is_coords = True
    max_x = 0
    max_y = 0
    with open(file_path) as f:
        for line in f:
            if line == '\n':
                is_coords = False
            elif is_coords:
                raw = line.rstrip('\n').split(",")
                c = Coord(int(raw[0]), int(raw[1]))
                coords.append(c)
                if max_x < c.x:
                    max_x = c.x
                if max_y < c.y:
                    max_y = c.y
            else:
                raw = line.split(" ")[2].split("=")
                folds.append((raw[0], int(raw[1])))

    paper = np.zeros((max_y+1, max_x+1), int)
    for c in coords:
        paper[c.y][c.x] = 1
    return paper, folds


def algo_1(input: Tuple):
    paper = input[0]
    folds = input[1]

    fold = folds[0]

    if fold[0] == 'y':
        y = fold[1]
        part_1 = paper[:y, :]
        part_2 = np.flip(paper[y+1:, :], axis=0)
        new_paper = part_1 + part_2
    elif fold[0] == 'x':
        x = fold[1]
        part_1 = paper[:, :x]
        part_2 = np.flip(paper[:, x+1:], axis=1)
        new_paper = part_1 + part_2
    else:
        raise InvalidStateError('invalid fold')

    return np.count_nonzero(new_paper >= 1)

def algo_2(input: Tuple):
    paper = input[0]
    folds = input[1]

    for fold in folds:
        if fold[0] == 'y':
            y = fold[1]
            part_1 = paper[:y, :]
            part_2 = np.flip(paper[y + 1:, :], axis=0)
            paper = part_1 + part_2
        elif fold[0] == 'x':
            x = fold[1]
            part_1 = paper[:, :x]
            part_2 = np.flip(paper[:, x + 1:], axis=1)
            paper = part_1 + part_2
        else:
            raise InvalidStateError('invalid fold')

    for row in paper:
        line = ''
        for i in row:
            if i >= 1:
                line += '#'
            else:
                line += '.'
        print(line)


if __name__ == '__main__':
    file = 'input.txt'
    file_input = read_file(file)
    print("algo 1:")
    print(algo_1(file_input))
    print()
    print("algo 2:")
    algo_2(file_input)
