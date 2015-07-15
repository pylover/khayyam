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


    def test_strptime(self):
        """
        %Z not working at all
        """

        f = JalaliDateFormatter

        self.assertEqual(f.parse('1361', '%Y'), JalaliDate(1361, 1, 1))
        self.assertEqual(f.parse('1361', '%Y'), JalaliDate(1361, 1, 1))

        #self.assertEqual(f.parse('د', '%a'), JalaliDate(1, 1, 1))

        # def check_format(f):
        #     formatter = JalaliDateFormatter()
        #     d1 = JalaliDate.today()
        #     d1_str = formatter.format(d1)
        #     d2 = formatter.parse(d1_str)
        #     self.assertEqual(d1, d2)
        #
        #
        # check_format("%Y")



if __name__ == '__main__':
    unittest.main()
