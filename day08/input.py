from typing import List


class Input:
    def __init__(self, unique: List[str], digit_output: List[str]):
        self.unique = unique
        self.digit_output = digit_output

    @property
    def all(self):
        return self.unique + self.digit_output

    def find_by_length(self, length: int):
        return [i for i in self.all if len(i) == length]

    def __repr__(self):
        return f"<Input unique={self.unique} output={self.digit_output}>"
