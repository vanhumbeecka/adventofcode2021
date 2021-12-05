from typing import List, Tuple
from pathlib import Path

def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    my_list: List[str] = []
    with open(file_path) as f:
        for line in f:
            my_list.append(line.rstrip('\n'))
    return my_list


def algo_1(input):
    length = len(input[0])
    zeros: List[int] = [0 for i in range(length)]
    ones: List[int] = [0 for i in range(length)]
    for i in input:
        for index in range(len(i)):
            if int(i[index]) == 0:
                zeros[index] += 1
            else:
                ones[index] += 1

    gamma: str = ''
    epsilon: str = ''
    for l in range(length):
        if zeros[l] > ones[l]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    g = int(gamma, 2)
    e = int(epsilon, 2)
    return g * e

def find_max_index(arr: List, index: int, search: str) -> List:
    zeros = []
    ones = []
    for line in arr:
        if line[index] == '0':
            zeros.append(line)
        else:
            ones.append(line)
    if search == 'oxygen':
        if len(ones) >= len(zeros):
            return ones
        return zeros
    else:
        if len(zeros) <= len(ones):
            return zeros
        return ones

def oxygen(input) -> int:
    length = len(input[0])

    for i in range(length):
        input = find_max_index(input, i, 'oxygen')
        if len(input) == 1:
            break

    return int(input[0], 2)

def scrubber(input) -> int:
    length = len(input[0])

    for i in range(length):
        input = find_max_index(input, i, 'scrubber')
        if len(input) == 1:
            break

    return int(input[0], 2)

def algo_2(input):
    length = len(input[0])

    input_copy = input[:]
    ox = oxygen(input_copy)
    input_copy = input[:]
    sc = scrubber(input_copy)

    return ox * sc



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = read_file('example.txt')
    print(algo_1(input))
    print(algo_2(input))