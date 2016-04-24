#!/usr/bin/python3

# Tests were adjusted, original author is David Balvín

from Polynomial import *
import unittest


class TestPrintFormat(unittest.TestCase):
    def test_params_basic(self):
        self.assertEqual(str(Polynomial([1, -3, 0, 2])), "2x^3 - 3x + 1",
                         "Test 1 - Spatny vystupni format Polynomial(list cisel)")
        self.assertEqual(str(Polynomial([1, -3, 0, -2])), "- 2x^3 - 3x + 1",
                         "Test 1 - Spatny vystupni format Polynomial(list cisel)")

    def test_params_args(self):
        self.assertEqual(str(Polynomial(1, -3, 0, 2)), "2x^3 - 3x + 1",
                         "Test 2 - Spatny vystupni format Polynomial(cisla)")
        self.assertEqual(str(Polynomial(x0=1, x3=2, x1=-3)), "2x^3 - 3x + 1",
                         "Test 3 - Spatny vystupni format Polynomial(named)")

        pol2 = Polynomial(1, -3, 0, 2)
        self.assertEqual(str(pol2), "2x^3 - 3x + 1", "Test 4 - Spatny vystupni format pol2 = Polynomial(cisla)")

    def test_add_op(self):
        self.assertEqual(str(Polynomial(1, -3, 0, 2) + Polynomial([1, -3, 0, 2])), "4x^3 - 6x + 2",
                         "Test 5 - Spatny soucet dvou polynomu")
        self.assertEqual(str(Polynomial(-1, 1) + Polynomial(x1=-2, x0=2)), "- x + 1",
                         "Test 6 - Spatny soucet dvou polynomu")

    def test_pow_op(self):
        self.assertEqual(str(Polynomial(-1, 1) ** 2), "x^2 - 2x + 1", "Test 7 - Spatny vypocet mocniny")
        self.assertEqual(str(Polynomial(-1, 1) ** 0), "1", "Test 8 - Spatny vypocet polynomu na nultou")
        self.assertEqual(str(Polynomial(0) ** 0), "1", "Test 24 - polynom na nultou")  # (0*x^0)^0 = 1

    def test_derivative(self):
        obj1 = Polynomial(1, -3, 0, 2)
        obj2 = obj1.derivative()
        obj3 = obj2.derivative()
        obj4 = obj3.derivative()

        self.assertEqual(str(obj1.derivative()), "6x^2 - 3", "Test 10 - Spatny vypocet derivace")
        self.assertEqual(str(obj2.derivative()), "12x", "Test 11 - Spatny vypocet derivace z Testu 10")
        self.assertEqual(str(obj3.derivative()), "12", "Test 12 - Spatny vypocet derivace z Testu 11")
        self.assertEqual(str(obj4.derivative()), "0", "Test 13 - Spatny vypocet derivace z Testu 12")

        test1 = Polynomial(x0=1, x1=1)
        test2 = test1.derivative()

        self.assertIsNot(test1, test2,
                         "Test 14 - Spatne provedeni metody derivative(). Nemela by menit originalni polynom")
        self.assertEqual(str(test1), "x + 1",
                         "Test 15 - Spatne provedeni metody derivative(). Nemela by menit originalni polynom")
        self.assertEqual(str(test2), "1", "Test 16 - Spatny vypocet derivace #2")

    def test_at_value_basic(self):
        self.assertEqual(Polynomial([1, -3, 0, 2]).at_value(2), 11, "Test 22 - Spatny vypocet at_value(x)")
        self.assertEqual(Polynomial([1, -3, 0, 2]).at_value(2, 3), 35, "Test 23 - Spatny vypocet at_value(x, y)")

    def test_at_value(self):
        self.assertEqual(Polynomial(1, -3, 0, 2).at_value(2), 11, "Test 17 - Spatny vypocet at_value(x)")
        self.assertEqual(Polynomial(1, -3, 0, 2).at_value(2, 3), 35, "Test 18 - Spatny vypocet at_value(x, y)")
        self.assertEqual(Polynomial(1, -3, 0, 2).at_value(1, 1), 0, "Test 19 - Spatny vypocet at_value(1, 1)")
        self.assertEqual(Polynomial(1, -3, 0, 2).at_value(1, 0), 1, "Test 19 - Spatny vypocet at_value(1, 0)")

        test1 = Polynomial(x0=1, x1=1)
        test2 = test1.at_value(2)

        self.assertIsNot(test1, test2,
                         "Test 20 - Spatne provedeni metody derivative(). Nemela by menit originalni polynom")
        self.assertEqual(str(test1), "x + 1",
                         "Test 21 - Spatne provedeni metody derivative(). Nemela by menit originalni polynom")
        self.assertEqual(test2, 3, "Test 22 - Spatny vypocet at_value #2")


if __name__ == '__main__':
    unittest.main()
