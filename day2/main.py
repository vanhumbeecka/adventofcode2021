from typing import List, Tuple
from pathlib import Path

def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    my_list: List[Tuple[str, int]] = []
    with open(file_path) as f:
        for line in f:
            split = line.split(" ")
            my_list.append((split[0], int(split[1])))
    return my_list

def algo_1(input):
    horizontal = 0
    depth = 0
    for i in input:
        if i[0] == 'forward':
            horizontal += i[1]
        if i[0] == 'down':
            depth += i[1]
        if i[0] == 'up':
            depth -= i[1]
    return horizontal * depth

def algo_2(input):
    horizontal = 0
    depth = 0
    aim = 0
    for i in input:
        if i[0] == 'forward':
            horizontal += i[1]
            depth += aim * i[1]
        if i[0] == 'down':
            aim += i[1]
        if i[0] == 'up':
            aim -= i[1]
    return horizontal * depth


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = read_file('example.txt')
    print(algo_1(input))
    print(algo_2(input))