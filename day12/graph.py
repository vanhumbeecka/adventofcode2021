from enum import Enum
from typing import List


class CaveType(Enum):
    BIG = 1
    SMALL = 2


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.neighbours: List["Cave"] = []
        if name.isupper():
            self.type: CaveType = CaveType.BIG
        else:
            self.type: CaveType = CaveType.SMALL

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"<Cave {self.name} neighbours={len(self.neighbours)}>"

    def add_neighbour(self, neigbour: "Cave"):
        self.neighbours.append(neigbour)

    @property
    def is_start(self):
        return self.name == "start"

    @property
    def is_end(self):
        return self.name == "end"
