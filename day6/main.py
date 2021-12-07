from typing import List
from pathlib import Path

import numpy as np


def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    with open(file_path) as f:
        line = f.readline()
    return list(map(int, line.split(",")))

def algo_1(fish: List[int], days_left):
    if days_left == 0:
        return len(fish)

    delta = min(fish) + 1
    if delta >= days_left:
        delta = days_left

    fish_next = list(map(lambda x: x-delta, fish))
    indices = [x for x, v in enumerate(fish_next) if v < 0]
    total = len(indices)

    for i in indices:
        fish_next[i] = 6
    fish_next += [8 for i in range(total)]

    return algo_1(fish_next, days_left-delta)

def fish_to_fishlist(fish: List[int]) -> np.ndarray:
    fish_list = np.zeros(9, int)
    for i in range(9):
        fish_list[i] = fish.count(i)
    return fish_list


def algo_2(fish: List[int], days_left):
    fishlist = fish_to_fishlist(fish)
    if days_left == 0:
        return fishlist.sum(axis=None)

    for i in range(days_left):
        # print(f"{i}: {fishlist}")
        c_0 = fishlist[1]
        c_1 = fishlist[2]
        c_2 = fishlist[3]
        c_3 = fishlist[4]
        c_4 = fishlist[5]
        c_5 = fishlist[6]
        c_6 = fishlist[7] + fishlist[0]
        c_7 = fishlist[8]
        c_8 = fishlist[0]
        fishlist = np.array([c_0, c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8])

    return fishlist.sum(axis=None)


if __name__ == '__main__':
    fish = read_file('input.txt')
    print("part 1:")
    print(algo_1(fish, 80))
    print("part 1b:")
    print(algo_2(fish, 80))

    print("part 2:")
    print(algo_2(fish, 256))