from typing import List
from pathlib import Path

def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    my_list: List[int] = []
    with open(file_path) as f:
        for line in f:
            my_list.append(int(line))
    return my_list

def algo_1(numbers):
    second = None
    count = 0
    for num in numbers:
        first = num
        if second is not None and first > second:
            count += 1
        second = first
    return count

def algo_2(numbers):
    ln = len(numbers)
    second = None
    count = 0
    for i in range(ln):
        if i+2 >= ln:
            break
        first = numbers[i] + numbers[i+1] + numbers[i+2]
        if second is not None and first > second:
            count += 1
        second = first
    return count


if __name__ == '__main__':
    numbers = read_file('example.txt')
    print(algo_1(numbers))
    print(algo_2(numbers))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
