import numpy as np
from typing import List


class Board:
    def __init__(self, board_lines: List[List[int]]):
        self.numbers = np.array(board_lines, np.int32)
        self.markers = np.zeros((5, 5), dtype=int)

    def __repr__(self):
        return f"<Board {self.numbers}>"

    def mark(self, num):
        index = np.where(self.numbers == num)
        if len(index[0]):
            self.markers[index] = 1

    @property
    def is_winner(self):
        for i in range(5):
            if np.all(self.markers[:,i]):
                return True
            if np.all(self.markers[i,:]):
                return True

        return False

    def score(self, num):
        if not self.is_winner:
            return 0

        ones = np.ones((5, 5), dtype=int)
        mask = ones - self.markers
        others = np.multiply(mask, self.numbers)
        sum = np.sum(others, axis=None)
        # print(sum)

        return num * sum


