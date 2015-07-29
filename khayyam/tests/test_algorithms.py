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

    def test_is_leap_year(self):
        for i in range(3000):
            self.assertEqual(
                alg_c.is_leap_year(i),
                alg_p.is_leap_year(i))

    def test_days_in_year(self):
        for i in range(3000):
            self.assertEqual(
                alg_c.days_in_year(i),
                alg_p.days_in_year(i))

    def test_days_in_month(self):
        for i in range(3000):
            for m in range(1, 13):
                self.assertEqual(
                    alg_c.days_in_month(i, m),
                    alg_p.days_in_month(i, m))

    def test_julian_day_from_jalali_date(self):
        for y in range(303):
            for m in range(1, 13):
                for d in range(1, alg_c.days_in_month(y, m)+1):
                    self.assertEqual(
                        alg_c.julian_day_from_jalali_date(y, m,  d),
                        alg_p.julian_day_from_jalali_date(y, m , d))

    def test_jalali_date_from_julian_day(self):
        jd = 0
        while jd < 365 * 1000:
            jd += 1
            self.assertEqual(
                alg_c.jalali_date_from_julian_day(jd),
                alg_p.jalali_date_from_julian_day(jd))

    def test_gregorian_date_from_julian_day(self):
        jd = 0
        while jd < 365 * 200:
            jd += 1
            self.assertEqual(
                alg_c.gregorian_date_from_julian_day(jd),
                alg_p.gregorian_date_from_julian_day(jd))

    def test_jalali_date_from_gregorian_date(self):
        jd = 0
        while jd < 365 * 200:
            jd += 1
            self.assertEqual(
                alg_c.jalali_date_from_gregorian_date(*alg_c.gregorian_date_from_julian_day(jd)),
                alg_p.jalali_date_from_gregorian_date(*alg_p.gregorian_date_from_julian_day(jd)),)

if __name__ == '__main__':
    unittest.main()