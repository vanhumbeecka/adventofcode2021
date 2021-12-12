from typing import List
from pathlib import Path

from day12.graph import Cave, CaveType


class InvalidStateError(Exception):
    pass


def read_file(name) -> List[Cave]:
    base_path = Path(__file__).parent
    file_path = (base_path / name).resolve()
    caves: List[Cave] = []
    with open(file_path) as f:
        for line in f:
            line = line.rstrip('\n').split("-")
            if not [c for c in caves if c.name == line[0]]:
                cave_0 = Cave(line[0])
                caves.append(cave_0)
            else:
                cave_0 = [c for c in caves if c.name == line[0]][0]
            if not [c for c in caves if c.name == line[1]]:
                cave_1 = Cave(line[1])
                caves.append(cave_1)
            else:
                cave_1 = [c for c in caves if c.name == line[1]][0]

            cave_0.add_neighbour(cave_1)
            cave_1.add_neighbour(cave_0)

    return caves


def search(_caves: List[Cave], cave: Cave, path: List[str], all_paths: List[List[str]]):
    for n in cave.neighbours:
        if not (n.name in path and n.type is CaveType.SMALL):
            path_copy = list(path)
            path_copy.append(n.name)
            if n.name == "end":
                all_paths.append(path)
            else:
                search(_caves, n, path_copy, all_paths)


def can_visit(path: List[str], cave: Cave):
    if cave.name == "start":
        return False
    if cave.type is CaveType.BIG:
        return True
    if cave.name not in path:
        return True

    lower = [i for i in path if i.islower()]
    return len(lower) == len(set(lower)) and "end" not in lower


def search_2(_caves: List[Cave], cave: Cave, path: List[str], all_paths: List[List[str]]):
    for n in cave.neighbours:
        ok = can_visit(path, n)
        if ok:
            path_copy = list(path)
            path_copy.append(n.name)
            if n.name == "end":
                all_paths.append(path)
            else:
                search_2(_caves, n, path_copy, all_paths)


def algo_1(_caves: List[Cave]):
    start = [s for s in caves if s.name == "start"][0]

    all_paths = []
    search(_caves, start, ["start"], all_paths)
    return len(all_paths)


def algo_2(_caves: List[Cave]):
    start = [s for s in caves if s.name == "start"][0]

    all_paths = []
    search_2(_caves, start, ["start"], all_paths)
    return len(all_paths)


if __name__ == '__main__':
    file = 'input.txt'
    caves = read_file(file)
    print("algo 1:")
    print(algo_1(caves))
    print()
    print("algo 2:")
    print(algo_2(caves))
