from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict, Set
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


def build_graph(input: Tuple) -> Tuple[Dict[str, Tuple[str, List[str]]], Set]:
    inserts: Dict[str, str] = input[1]
    graph: Dict[str, Tuple[str, List[str]]] = {}
    letters = set()
    for key in inserts.keys():
        split = list(key)
        graph[key] = (inserts[key], [split[0] + inserts[key], inserts[key] + split[1]])
        letters.add(inserts[key])
    return graph, letters


def add_pairs(from_pair: str, counter_letters: Dict[str, int], counter_pairs: Dict[str, int], multiplayer: int = 1):
    letter, pairs = graph[from_pair]
    counter_letters[letter] += 1 * multiplayer
    counter_pairs[from_pair] -= 1 * multiplayer
    for p in pairs:
        counter_pairs[p] += 1 * multiplayer

def sum_letters(counter_letters):
    sum = 0
    for k in counter_letters.keys():
        sum += counter_letters[k]
    return sum

def algo_2(input: Tuple):
    global graph
    graph, letters = build_graph(input)
    entries = input[0]
    counter_letters = dict.fromkeys(letters, 0)
    counter_pairs = dict.fromkeys(graph.keys(), 0)
    for e in entries:
        if e.pair is not None:
            counter_pairs[e.pair] += 1
        counter_letters[e.name] += 1

    print(graph)
    print(f"{counter_letters} - {sum_letters(counter_letters)}")
    for i in range(40):
        new_counter_pairs = counter_pairs.copy()
        for p in counter_pairs.keys():
            c = counter_pairs[p]
            if c > 0:
                add_pairs(p, counter_letters, new_counter_pairs, c)
        counter_pairs = new_counter_pairs
        print(f"{counter_letters} - {sum_letters(counter_letters)}")

    values = counter_letters.values()
    return max(values) - min(values)

if __name__ == '__main__':
    file = 'input.txt'
    print("algo 2:")
    print(algo_2(read_file(file)))
