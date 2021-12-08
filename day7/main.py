from typing import List
from pathlib import Path

import numpy as np


def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    with open(file_path) as f:
        line = f.readline()
    return list(map(int, line.split(",")))


def algo_1(crabs: List[int]):
    arr = np.array(crabs)
    median = np.median(arr)
    avg = np.average(arr)

    result = median  # median is a first good guess
    value = np.sum(np.abs(arr - result))

    while True:
        if avg > median:  # answer must be somewhere between median and average
            new_result = result + 1
        else:
            new_result = result - 1
        new_value = np.sum(np.abs(arr - new_result))
        if new_value < value:
            result = new_result
            value = new_value
        else:
            return value


def fuel(distance):
    return distance * (distance + 1) / 2


def algo_2(crabs):
    arr = np.array(crabs)
    avg = np.average(arr)

    result = round(avg)  # avg is a first good guess
    value = np.sum(fuel(np.abs(arr - result)))

    new_result_up = result + 1
    new_value_up = np.sum(fuel(np.abs(arr - new_result_up)))

    if new_value_up < value:
        direction = 'up'
        result = new_result_up
        value = new_value_up
    else:
        direction = 'down'

    while True:
        if direction == 'up':
            new_result = result + 1
        else:
            new_result = result - 1

        new_value = np.sum(fuel(np.abs(arr - new_result)))
        if new_value < value:
            result = new_result
            value = new_value
        else:
            return value


if __name__ == '__main__':
    crabs = read_file('input.txt')
    print(algo_1(crabs))
    print(algo_2(crabs))

