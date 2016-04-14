#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stderr
from operator import add
from functools import reduce

__author__ = 'xmasek15'


class Polynomial(object):
    x = ['', 'x']

    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.deg = len(coeffs) - 1

    def __str__(self):
        print('__str__')
        # Iterate coefficients into a list of non-zero terms
        terms = ['{0:+d}'.format(self.coeffs[k]) + ('x^' + str(k) if k > 1 else self.x[k])
                 for k in range(0, self.deg + 1) if self.coeffs[k] != 0]

        if len(terms) == 0:
            return "0"

        return reduce(add, terms)


def start():
    pol1 = Polynomial([1, -3, 0, 2])
    # pol2 = Polynomial([-1, 3])

    print(str(Polynomial([1, -3, 0, 2])))

    # print(pol2)
    # print(pol1 + pol2)


if __name__ == "__main__":
    try:
        start()

    except KeyboardInterrupt:
        print('Script will be terminated.', file=stderr)
        exit(1)


