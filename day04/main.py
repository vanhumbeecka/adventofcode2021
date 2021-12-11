from typing import List
from pathlib import Path
from board import Board

import numpy as np

def read_file(name):
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    boards: List[np]
    with open(file_path) as f:
        first_line = f.readline()
        numbers = list(map(int, first_line.split(",")))
        boards: List[Board] = []
        board_lines = []

        next_line = 1
        while next_line:
            next_line = f.readline() # empty
            clean_line = next_line.rstrip("\n")
            if not clean_line:
                if len(board_lines) != 5:
                    pass
                else:
                    boards.append(Board(board_lines))
                    board_lines = []


            else:
                nums = [s for s in clean_line.split(" ") if s != '']
                board_line = list(map(int, nums))
                board_lines.append(board_line)

    return (numbers, boards)


def algo_1(numbers, boards):
    for num in numbers:
        for board in boards:
            board.mark(num)
            if board.is_winner:
                return board.score(num)

    raise Exception('No winner found!')


def algo_2(numbers, boards):
    for num in numbers:
        for board in boards:
            board.mark(num)
            if board.is_winner and len(boards) == 1:
                return board.score(num)
            if board.is_winner and len(boards) > 1:
                boards = [b for b in boards if b != board]


if __name__ == '__main__':
    numbers, boards = read_file('input.txt')
    print(numbers)
    print(algo_1(numbers, boards))
    print(algo_2(numbers, boards))