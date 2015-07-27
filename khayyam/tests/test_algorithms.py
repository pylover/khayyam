# -*- coding: utf-8 -*-
import unittest
from khayyam import algorithms_c as alg_c
from khayyam import algorithms_pure as alg_p
__author__ = 'vahid'

class TestCAlgorithms(unittest.TestCase):

    def test_get_julian_day_from_gregorian(self):
        for i in range(3000):
            self.assertEqual(
                alg_c.get_julian_day_from_gregorian(i, 1, 1),
                alg_p.get_julian_day_from_gregorian(i, 1, 1))


if __name__ == '__main__':
    unittest.main()