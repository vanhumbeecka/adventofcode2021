import dataclasses
from typing import List, Tuple
from pathlib import Path

import numpy as np
from collections import deque

class InvalidStateError(Exception):
    pass

def read_file(name) -> List[str]:
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    lines: List[str] = []
    with open(file_path) as f:
        for line in f:
            line = line.rstrip('\n')
            lines.append(line)
    return lines

def is_open(char: str):
    return char == "[" or char == "(" or char == "{" or char == "<"

def is_close(char: str):
    return char == "]" or char == ")" or char == "}" or char == ">"

def matches(open: str, close: str):
    if (open == "[" and close == "]") or \
            (open == "(" and close == ")") or \
            (open == "{" and close == "}") or \
            (open == "<" and close == ">"):
        return True

    return False

def parse_line_algo_1(line: str):
    chars = list(line)
    stack = deque()
    for char in chars:
        if is_open(char):
            stack.append(char)
        elif is_close(char):
            open_char = stack.pop()
            if not matches(open_char, char):
                return char
        else:
            raise InvalidStateError('invalid char')

    return None

def complement(char):
    if char == "(":
        return ")"
    if char == "{":
        return "}"
    if char == "[":
        return "]"
    if char == "<":
        return ">"
    raise InvalidStateError("not implemented")

def parse_line_algo_2(line: str):
    chars = list(line)
    stack = deque()
    for char in chars:
        if is_open(char):
            stack.append(char)
        elif is_close(char):
            open_char = stack.pop()
            if not matches(open_char, char):
                raise InvalidStateError('Invalid closing char')
        else:
            raise InvalidStateError('invalid char')

    stack_list = list(stack)
    stack_list.reverse()
    result = []
    for char in stack_list:
        result.append(complement(char))
    return result


def score(char):
    if char == ")":
        return 3
    if char == "]":
        return 57
    if char == "}":
        return 1197
    if char == ">":
        return 25137
    raise InvalidStateError(f"score failed: {char}")

def score_char(char):
    if char == ")":
        return 1
    if char == "]":
        return 2
    if char == "}":
        return 3
    if char == ">":
        return 4
    raise InvalidStateError(f"score failed: {char}")

def score_2(chars: List[str]):
    total = 0
    for char in chars:
        total = total * 5 + score_char(char)
    return total

def algo_1(lines: List[str]):
    total = 0
    for line in lines:
        corrupt_char = parse_line_algo_1(line)
        if corrupt_char is not None:
            total += score(corrupt_char)

    return total


def algo_2(lines: List[str]):
    incomplete: List[str] = []
    for line in lines:
        corrupt_char = parse_line_algo_1(line)
        if corrupt_char is None:
            incomplete.append(line)

    scores = []
    for line in incomplete:
        result = parse_line_algo_2(line)
        scores.append(score_2(result))

    scores.sort()
    return scores[len(scores) // 2]


if __name__ == '__main__':
    my_list = read_file('input.txt')
    print(algo_1(my_list))
    print(algo_2(my_list))
