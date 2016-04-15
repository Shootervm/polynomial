#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stderr
from operator import add
from functools import reduce

__author__ = 'xmasek15'


class Polynomial(object):
    x = ['', 'x']

    def __init__(self, *args, **kwargs):
        if args and isinstance(args[0], list):  # Polynomial([1,-3,0,2])
            self.coeffs = args[0]
        elif args:  # Polynomial(1,-3,0,2)
            self.coeffs = args
        else:  # Polynomial(x0=1,x3=2­,x1=-3)
            self.coeffs = [kwargs.get(x, 0) for x in ['x' + str(i) for i in range(len(kwargs) + 1)]]

        self.deg = len(self.coeffs)  # is used as range limit, if representing degree `self.deg - 1` needs to be used

    def __str__(self):
        # Create list of terms by iterating coefficients and processing non-zero terms to correctly formatted items
        terms = [('{0:+d}'.format(self.coeffs[k]) if self.coeffs[k] > 1 or k == 0 else '') +
                 ('x^' + str(k) if k > 1 else self.x[k])
                 for k in range(0, self.deg) if self.coeffs[k] != 0]

        if len(terms) == 0:
            return "0"

        return reduce(add, terms[::-1]).replace('+', ' + ').replace('-', ' - ').lstrip(' + ')

    def __call__(self, x):
        """Evaluates the Polynomial at value of x"""
        return reduce(add, [self.coeffs[i] * (x ** i) for i in range(self.deg)])

    def at_value(self, x, y=None):

        return self.__call__(x) if y is None else self.__call__(y) - self.__call__(x)

    def __add__(self, other):
        """Adds two Polynomials and will overload + operator when called."""

        terms = [0] * max(self.deg, other.deg)
        for i in range(self.deg):
            terms[i] = self.coeffs[i]
        for i in range(other.deg):
            terms[i] = terms[i] + other.coeffs[i]

        return Polynomial(terms)


def start():
    pol1 = Polynomial([1, -3, 0, 2])
    pol3 = Polynomial(1, -3, 0, 2)
    pol2 = Polynomial([1, -3])
    print(Polynomial(x0=1, x1=1))

    # print(pol1)
    # print(pol1.at_value(2))
    # print(pol1.at_value(3))
    # print(pol1.at_value(2, 3))

    # print(Polynomial(1, -3, 0, 2))
    # print(Polynomial(x0=1, x3=2, x1=-3))
    # print(Polynomial(x0=5, x3=2, x4=4, x5=4, x1=-3))
    # "2x^3 - 3x + 1"

    # print(pol2)
    # print(pol1 + pol2)


if __name__ == "__main__":
    try:
        start()

    except KeyboardInterrupt:
        print('Script will be terminated.', file=stderr)
        exit(1)


