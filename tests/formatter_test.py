# -*- coding: utf-8 -*-
import unittest
from khayyam import JalaliDate, JalaliDateFormatter
__author__ = 'vahid'

class TestJalaliDateFormatter(unittest.TestCase):
    """
    %%
    %a%A%b%B%d%j%m%w%W%x%y%Y%e%E%g%G"
    """

    def test_strftime(self):
        d1 = JalaliDate(1361, 6, 15)
        f = JalaliDateFormatter
        self.assertEqual(f.format(d1, '%a'), 'د')
        self.assertEqual(f.format(d1, '%A'), 'دوشنبه')
        self.assertEqual(f.format(d1, '%b'), 'شه')
        self.assertEqual(f.format(d1, '%B'), 'شهریور')
        self.assertEqual(f.format(d1, '%d'), '15')
        self.assertEqual(f.format(d1, '%j'), '170')
        self.assertEqual(f.format(d1, '%m'), '06')
        self.assertEqual(f.format(d1, '%w'), '2')
        self.assertEqual(f.format(d1, '%W'), '24')
        self.assertEqual(f.format(d1, '%x'), 'دوشنبه 15 شهریور 1361')
        self.assertEqual(f.format(d1, '%y'), '61')
        self.assertEqual(f.format(d1, '%Y'), '1361')
        self.assertEqual(f.format(d1, '%e'), 'D')
        self.assertEqual(f.format(d1, '%E'), 'Doshanbeh')
        self.assertEqual(f.format(d1, '%g'), 'Sh')
        self.assertEqual(f.format(d1, '%G'), 'Shahrivar')
        self.assertEqual(f.format(d1, '%%'), '%')

        self.assertEqual(
            f.format(d1, '%a%A%b%B%d%j%m%w%W%x%y%Y%e%E%g%G%%'),
            'ددوشنبهشهشهریور1517006224دوشنبه 15 شهریور 1361611361DDoshanbehShShahrivar%')
        self.assertEqual(f.format(d1, '%Y-%m-%d'), '1361-06-15')
        self.assertEqual(f.format(d1, 'اول%Y-%m-%dآخر'), 'اول1361-06-15آخر')


    def test_strptime(self):
        """
        %Z not working at all
        """

        f = JalaliDateFormatter

        # Test Year
        self.assertEqual(f.parse('1361', '%Y'), dict(year=1361))
        self.assertEqual(f.parse('1361%C', '%Y%C'), dict(year=1361))
        self.assertEqual(f.parse('اریا1361گلگشت', 'اریا%Yگلگشت'), dict(year=1361))

        # Test All months
        for i in range(1, 13):
            self.assertEqual(f.parse(str(i), '%m'), dict(month=i))
        self.assertRaises(ValueError, f.parse, '13', '%m')
        self.assertRaises(ValueError, f.parse, '0', '%m')

        # Test All days
        for i in range(1, 32):
            self.assertEqual(f.parse(str(i), '%d'), dict(day=i))
        self.assertRaises(ValueError, f.parse, '32', '%d')
        self.assertRaises(ValueError, f.parse, '0', '%d')

        # Test day of year
        for i in range(1, 366):
            self.assertEqual(f.parse(str(i), '%j'), dict(year=1, month=1, day=i))
        self.assertRaises(ValueError, f.parse, '366', '%j')
        self.assertRaises(ValueError, f.parse, '0', '%j')
        self.assertEqual(f.parse('1345 5', '%Y %j'), dict(year=1345, month=1, day=5))


        def check_format(d ,fmt):
            formatter = JalaliDateFormatter(fmt)
            d_str = formatter.get_string(d)
            d2 = formatter.parse_(d_str, JalaliDate)
            self.assertEqual(d, d2)

        i = 0
        while i < 100: # * 365:
            i += 1
            d = JalaliDate.fromordinal(i)
            check_format(d ,"%Y-%m-%d %a%A%b%B%j") # "%j%m%w%W%x%y%Y%e%E%g%G%%")



if __name__ == '__main__':
    unittest.main()
