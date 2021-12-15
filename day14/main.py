from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
from pathlib import Path
from entry import Entry
import numpy as np


class InvalidStateError(Exception):
    pass


def read_file(name) -> Tuple:
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    template = ""
    entries: List[Entry] = []
    inserts: Dict[str, str] = {}
    with open(file_path) as f:
        for line in f:
            if not template:
                template = line.rstrip("\n")
                last_entry: Optional[Entry] = None
                for t in list(template):
                    new_entry = Entry(t)
                    entries.append(new_entry)
                    if last_entry:
                        last_entry.set_next(new_entry)
                    last_entry = new_entry
            elif line != '\n':
                raw = line.rstrip('\n').split(" -> ")
                inserts[raw[0]] = raw[1]

    return entries, inserts


def algo_1(input: Tuple):
    entries: List[Entry] = input[0]
    start = entries[0]
    inserts: Dict[str, str] = input[1]
    for i in range(10):
        e = start
        while e.has_next():
            target = inserts.get(e.pair, False)
            if target:
                e = e.insert_and_return_last(Entry(target))
    counts = {}
    e = start
    counts[e.name] = 1
    while e.has_next():
        e = e.get_next()
        counts[e.name] = 1 if not counts.get(e.name, False) else counts[e.name] + 1

    min = None
    max = None
    for key in counts.keys():
        if min is None or counts[key] < min:
            min = counts[key]
        if max is None or counts[key] > max:
            max = counts[key]

    return max - min


if __name__ == '__main__':
    file = 'example.txt'
    print("algo 1:")
    print(algo_1(read_file(file)))
