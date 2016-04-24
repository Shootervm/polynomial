#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from sys import stderr
from operator import add
from functools import reduce

__author__ = 'xmasek15'


class Polynomial(object):
    x = ['', 'x']

    def __init__(self, *args, **kwargs):
        if args and isinstance(args[0], list):  # Polynomial([#list#])
            self.coeffs = args[0]
        elif args:  # Polynomial(#args#)
            self.coeffs = args
        else:  # Polynomial(#named args#)
            self.coeffs = [kwargs.get(x, 0) for x in ['x' + str(i) for i in range(len(kwargs) + 1)]]

        self.deg = len(self.coeffs)  # is used as range limit, if representing degree `self.deg - 1` needs to be used

    def __str__(self):
        # Create list of terms by iterating coefficients and processing non-zero terms to correctly formatted items
        terms = ['{0:+d}'.format(self.coeffs[k]) + ('x^' + str(k) if k > 1 else self.x[k])
                 for k in range(0, self.deg) if self.coeffs[k] != 0]

        if len(terms) == 0:
            return "0"

        return re.sub('[^0-9]1x', ' x', reduce(add, terms[::-1]).replace('+', ' + ').replace('-', ' - ')).lstrip(' + ')

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

    def __mul__(self, other):
        """Multiplies two Polynomials and will overload * operator when called."""

        prod_coeffs = [0] * (self.deg + other.deg + 1)  # Initialize coefficient list of product
        for i in range(0, self.deg):
            for j in range(0, other.deg):
                prod_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(prod_coeffs)

    def __pow__(self, power):
        if power < 0:
            raise ValueError("Power must be a non-negative integer.")
        elif power == 0:
            return Polynomial(1)
        elif power == 1:
            return self
        else:
            result = self
            for i in range(2, power + 1):
                result = result * self

            return result

    def derivative(self):
        return Polynomial([self.coeffs[d] * d for d in range(1, len(self.coeffs))])

    def deriv(self):
        return self.derivative()


def start():
    pass


if __name__ == "__main__":
    try:
        start()

    except KeyboardInterrupt:
        print('Script will be terminated.', file=stderr)
        exit(1)
