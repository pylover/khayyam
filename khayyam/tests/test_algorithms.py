# -*- coding: utf-8 -*-
import unittest
from khayyam import algorithms_c as alg_c
from khayyam import algorithms_pure as alg_p
__author__ = 'vahid'


# TODO: test with negative values
class TestCAlgorithms(unittest.TestCase):

    def test_get_julian_day_from_gregorian(self):
        self.assertRaises(ValueError, alg_p.get_julian_day_from_gregorian_date, 2016, 2, 30)
        self.assertRaises(ValueError, alg_p.get_julian_day_from_gregorian_date, 2015, 2, 29)

        self.assertRaises(ValueError, alg_c.get_julian_day_from_gregorian_date, 2016, 2, 30)
        self.assertRaises(ValueError, alg_c.get_julian_day_from_gregorian_date, 2015, 2, 29)

        self.assertRaises(ValueError, alg_c.get_julian_day_from_gregorian_date, -4713, 2, 30)
        self.assertRaises(ValueError, alg_c.get_julian_day_from_gregorian_date, -4713, 2, 29)

        self.assertEqual(
            alg_c.get_julian_day_from_gregorian_date(-4713, 11, 25),
            alg_p.get_julian_day_from_gregorian_date(-4713, 11, 25)
        )

        for i in range(3000):
            self.assertEqual(
                alg_c.get_julian_day_from_gregorian_date(i, 1, 1),
                alg_p.get_julian_day_from_gregorian_date(i, 1, 1)
            )

    def test_is_leap_year(self):
        for i in range(3000):
            self.assertEqual(
                alg_c.is_jalali_leap_year(i),
                alg_p.is_jalali_leap_year(i)
            )

    def test_days_in_year(self):
        for i in range(3000):
            self.assertEqual(
                alg_c.get_days_in_jalali_year(i),
                alg_p.get_days_in_jalali_year(i)
            )

    def test_days_in_month(self):
        for i in range(3000):
            for m in range(1, 13):
                c = alg_c.get_days_in_jalali_month(i, m)
                p = alg_p.get_days_in_jalali_month(i, m)
                self.assertEqual(c, p, "year: %s, month: %s, results: {c: %s, py: %s}" % (i, m, c, p))

    def test_julian_day_from_jalali_date(self):
        for y in range(303):
            for m in range(1, 13):
                for d in range(1, alg_c.get_days_in_jalali_month(y, m)+1):
                    self.assertEqual(
                        alg_c.get_julian_day_from_jalali_date(y, m, d),
                        alg_p.get_julian_day_from_jalali_date(y, m, d),
                        "year: %s, month: %s, day: %s" % (y, m, d)
                    )

    def test_jalali_date_from_julian_day(self):
        jd = 0
        while jd < 365 * 1000:
            jd += 1
            c = alg_c.get_jalali_date_from_julian_day(jd)
            p = alg_p.get_jalali_date_from_julian_day(jd)
            self.assertEqual(c, p, "Julian day: %s\t%s <> %s" % (jd, c, p))

    def test_gregorian_date_from_julian_day(self):
        jd = 0
        self.assertRaises(ValueError, alg_c.get_gregorian_date_from_julian_day, jd)
        self.assertRaises(ValueError, alg_p.get_gregorian_date_from_julian_day, jd)
        while jd < 365 * 200:
            jd += 1
            self.assertEqual(
                alg_c.get_gregorian_date_from_julian_day(jd),
                alg_p.get_gregorian_date_from_julian_day(jd)
            )

    def test_jalali_date_from_gregorian_date(self):
        jd = 0
        while jd < 365 * 200:
            jd += 1
            cd = alg_c.get_gregorian_date_from_julian_day(jd)
            pd = alg_p.get_gregorian_date_from_julian_day(jd)

            c = alg_c.get_jalali_date_from_gregorian_date(*cd)
            p = alg_p.get_jalali_date_from_gregorian_date(*pd)

            self.assertEqual(c, p, 'jd: %s c: %s py: %s cdate: %s pydate: %s' % (jd, c, p, cd, pd))

    def test_algorithm_import(self):
        from khayyam import algorithms
        self.assertTrue(hasattr(algorithms, 'is_jalali_leap_year'))
        self.assertTrue(hasattr(algorithms, 'get_days_in_jalali_year'))
        self.assertTrue(hasattr(algorithms, 'get_days_in_jalali_month'))
        self.assertTrue(hasattr(algorithms, 'get_julian_day_from_gregorian_date'))
        self.assertTrue(hasattr(algorithms, 'get_julian_day_from_jalali_date'))
        self.assertTrue(hasattr(algorithms, 'get_jalali_date_from_julian_day'))
        self.assertTrue(hasattr(algorithms, 'get_jalali_date_from_gregorian_date'))
        self.assertTrue(hasattr(algorithms, 'get_gregorian_date_from_julian_day'))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
