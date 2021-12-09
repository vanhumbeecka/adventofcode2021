from typing import List, Tuple
from pathlib import Path
from display import Display
from input import Input

import numpy as np


def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    my_list: List[Input] = []
    with open(file_path) as f:
        for line in f:
            split = line.rstrip('\n').split(" | ")
            uniques: List[str] = split[0].split(" ")
            digits: List[str] = split[1].split(" ")

            my_list.append(Input(uniques, digits))
    return my_list


def algo_1(input: List[Input]):
    count = 0
    for line in input:
        digits = line.digit_output
        for d in digits:
            if len(d) in [2, 3, 4, 7]:
                count += 1

    return count


def algo_2(inputs: List[Input]):
    count = 0
    for p in inputs:
        d = Display(p)
        d.calculate()
        num = d.get_full_number()
        count += num

    return count


if __name__ == '__main__':
    my_list = read_file('input.txt')
    print(algo_1(my_list))
    print(algo_2(my_list))
