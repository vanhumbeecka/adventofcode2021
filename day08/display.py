from typing import Tuple, List, Set
from input import Input

import numpy as np


def _all() -> Set[str]:
    return {'a', 'b', 'c', 'd', 'e', 'f', 'g'}


def _eight():
    return _all()


class InvalidStateError(Exception):
    pass


class Display:
    def __init__(self, inp: Input):
        self.input = inp
        self.a: Set[str] = _all()
        self.b: Set[str] = _all()
        self.c: Set[str] = _all()
        self.d: Set[str] = _all()
        self.e: Set[str] = _all()
        self.f: Set[str] = _all()
        self.g: Set[str] = _all()

    def __repr__(self):
        return f"<Display a={self.a} b={self.b} c={self.c} d={self.d} e={self.e} f={self.f} g={self.g}>"

    def get_full_number(self):
        return self.get_digit(0) * 1000 + self.get_digit(1) * 100 + self.get_digit(2) * 10 + self.get_digit(3)

    def get_digit(self, num):
        d = self.input.digit_output[num]
        digit = np.array([
            1 if next(iter(self.a)) in d else 0,
            1 if next(iter(self.b)) in d else 0,
            1 if next(iter(self.c)) in d else 0,
            1 if next(iter(self.d)) in d else 0,
            1 if next(iter(self.e)) in d else 0,
            1 if next(iter(self.f)) in d else 0,
            1 if next(iter(self.g)) in d else 0,
        ])
        if np.array_equal(digit, [1, 1, 1, 0, 1, 1, 1]):
            return 0
        if np.array_equal(digit, [0, 0, 1, 0, 0, 1, 0]):
            return 1
        if np.array_equal(digit, [1, 0, 1, 1, 1, 0, 1]):
            return 2
        if np.array_equal(digit, [1, 0, 1, 1, 0, 1, 1]):
            return 3
        if np.array_equal(digit, [0, 1, 1, 1, 0, 1, 0]):
            return 4
        if np.array_equal(digit, [1, 1, 0, 1, 0, 1, 1]):
            return 5
        if np.array_equal(digit, [1, 1, 0, 1, 1, 1, 1]):
            return 6
        if np.array_equal(digit, [1, 0, 1, 0, 0, 1, 0]):
            return 7
        if np.array_equal(digit, [1, 1, 1, 1, 1, 1, 1]):
            return 8
        if np.array_equal(digit, [1, 1, 1, 1, 0, 1, 1]):
            return 9

        raise InvalidStateError("no digit found")

    def close_down(self):
        if len(self.a) == 1:
            self.b = self.b.difference(self.a)
            self.c = self.c.difference(self.a)
            self.d = self.d.difference(self.a)
            self.e = self.e.difference(self.a)
            self.f = self.f.difference(self.a)
            self.g = self.g.difference(self.a)
        if len(self.b) == 1:
            self.a = self.a.difference(self.b)
            self.c = self.c.difference(self.b)
            self.d = self.d.difference(self.b)
            self.e = self.e.difference(self.b)
            self.f = self.f.difference(self.b)
            self.g = self.g.difference(self.b)
        if len(self.c) == 1:
            self.a = self.a.difference(self.c)
            self.b = self.b.difference(self.c)
            self.d = self.d.difference(self.c)
            self.e = self.e.difference(self.c)
            self.f = self.f.difference(self.c)
            self.g = self.g.difference(self.c)
        if len(self.d) == 1:
            self.a = self.a.difference(self.d)
            self.b = self.b.difference(self.d)
            self.c = self.c.difference(self.d)
            self.e = self.e.difference(self.d)
            self.f = self.f.difference(self.d)
            self.g = self.g.difference(self.d)
        if len(self.e) == 1:
            self.a = self.a.difference(self.e)
            self.b = self.b.difference(self.e)
            self.c = self.c.difference(self.e)
            self.d = self.d.difference(self.e)
            self.f = self.f.difference(self.e)
            self.g = self.g.difference(self.e)
        if len(self.f) == 1:
            self.a = self.a.difference(self.f)
            self.b = self.b.difference(self.f)
            self.c = self.c.difference(self.f)
            self.d = self.d.difference(self.f)
            self.e = self.e.difference(self.f)
            self.g = self.g.difference(self.f)
        if len(self.g) == 1:
            self.a = self.a.difference(self.g)
            self.b = self.b.difference(self.g)
            self.c = self.c.difference(self.g)
            self.d = self.d.difference(self.g)
            self.e = self.e.difference(self.g)
            self.f = self.f.difference(self.g)

    def calculate(self):
        inp = self.input
        # find #1, #4, #7
        ones = inp.find_by_length(2)
        fours = inp.find_by_length(4)
        sevens = inp.find_by_length(3)
        zeros_sixes_nines = inp.find_by_length(6)
        twos_threes_fives = inp.find_by_length(5)

        if sevens and ones:
            for one in ones:
                for seven in sevens:
                    c_f = set(seven).intersection(one)
                    top = set(seven).difference(one)
                    if len(top) != 1:
                        raise InvalidStateError('top must be of length 1')
                    self.a = self.a.intersection(top)
                    self.c = self.c.intersection(c_f)
                    self.f = self.f.intersection(c_f)

        if fours and ones:
            for one in ones:
                for four in fours:
                    c_f = set(four).intersection(one)
                    b_d = set(four).difference(one)
                    if len(c_f) != 2 or len(b_d) != 2:
                        raise InvalidStateError('b_d/c_f must be of length 2')
                    self.b = self.b.intersection(b_d)
                    self.d = self.d.intersection(b_d)
                    self.c = self.c.intersection(c_f)
                    self.f = self.f.intersection(c_f)

        if sevens and fours:
            for seven in sevens:
                for four in fours:
                    c_f = set(seven).intersection(four)
                    a = set(seven).difference(four)
                    b_d = set(four).difference(seven)
                    if len(c_f) != 2:
                        raise InvalidStateError('c_f must be of length 2')
                    if len(a) != 1:
                        raise InvalidStateError("a length != 1")
                    self.a = self.a.intersection(a)
                    self.c = self.c.intersection(c_f)
                    self.f = self.f.intersection(c_f)
                    self.b = self.b.intersection(b_d)
                    self.d = self.d.intersection(b_d)

        twos: List[str] = []
        threes_fives: List[str] = []
        if fours and twos_threes_fives:
            for four in fours:
                for num in twos_threes_fives:
                    if len(set(four).intersection(num)) == 2:
                        twos.append(num)
                    else:
                        threes_fives.append(num)

        threes: List[str] = []
        fives: List[str] = []
        if ones and threes_fives:
            for one in ones:
                for num in threes_fives:
                    if len(set(one).intersection(num)) == 1:
                        fives.append(num)
                    else:
                        threes.append(num)
        elif sevens and threes_fives:
            for seven in sevens:
                for num in threes_fives:
                    if len(set(seven).intersection(num)) == 2:
                        fives.append(num)
                    else:
                        threes.append(num)

        sixes: List[str] = []
        zeros_nines: List[str] = []
        if ones and zeros_sixes_nines:
            for one in ones:
                for num in zeros_sixes_nines:
                    if len(set(num).intersection(one)) == 1:
                        sixes.append(num)
                    else:
                        zeros_nines.append(num)
        elif sevens and zeros_sixes_nines:
            for seven in sevens:
                for num in zeros_sixes_nines:
                    if len(set(num).intersection(seven)) == 2:
                        sixes.append(num)
                    else:
                        zeros_nines.append(num)

        if ones and twos:
            for one in ones:
                for two in twos:
                    c = set(two).intersection(one)
                    f = set(one).difference(two)
                    if len(c) != 1 or len(f) != 1:
                        raise InvalidStateError('c/f length must be 1')
                    self.c = self.c.intersection(c)
                    self.f = self.f.intersection(f)

        if twos and fours:
            for two in twos:
                for four in fours:
                    c_d = set(four).intersection(two)
                    b_f = set(four).difference(two)
                    a_e_g = set(two).difference(four)
                    if len(b_f) != 2 or len(a_e_g) != 3:
                        raise InvalidStateError(f'b_f/a_e_g {b_f}/{a_e_g}')
                    self.c = self.c.intersection(c_d)
                    self.d = self.d.intersection(c_d)
                    self.b = self.b.intersection(b_f)
                    self.f = self.f.intersection(b_f)
                    self.a = self.a.intersection(a_e_g)
                    self.e = self.e.intersection(a_e_g)
                    self.g = self.g.intersection(a_e_g)

        if sixes:
            for six in sixes:
                c = _eight().difference(six)
                if len(c) != 1:
                    raise InvalidStateError("c not 1")
                self.c = self.c.intersection(c)

        if fours:
            for four in fours:
                a_e_g = _eight().difference(four)
                b_c_d_f = _eight().intersection(four)
                if len(a_e_g) != 3 or len(b_c_d_f) != 4:
                    raise InvalidStateError("len wrong")
                self.a = self.a.intersection(a_e_g)
                self.e = self.e.intersection(a_e_g)
                self.g = self.g.intersection(a_e_g)
                self.b = self.b.intersection(b_c_d_f)
                self.c = self.c.intersection(b_c_d_f)
                self.d = self.d.intersection(b_c_d_f)
                self.f = self.f.intersection(b_c_d_f)

        if fives:
            for five in fives:
                c_e = _eight().difference(five)
                if len(c_e) != 2:
                    raise InvalidStateError("c_e wrong")
                self.c = self.c.intersection(c_e)
                self.e = self.e.intersection(c_e)

        # close down
        self.close_down()
