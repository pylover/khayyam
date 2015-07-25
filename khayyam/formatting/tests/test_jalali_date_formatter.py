# -*- coding: utf-8 -*-
import unittest
from datetime import timedelta
from khayyam import JalaliDate
from khayyam.formatting import constants as c
from rtl import rtl
__author__ = 'vahid'


class JalaliDateFormatterTestCase(unittest.TestCase):

    def assert_parse_and_format(self, jdate ,fmt, print_=False):
        jdate_str = jdate.strftime(fmt)
        if print_:
            print(jdate_str)
        d2 = JalaliDate.strptime(jdate_str, fmt)
        self.assertEqual(jdate, d2)


    def test_week(self):
        """
        Testing:
            %a           Locale’s abbreviated weekday name.
            %A           Locale’s full weekday name.
            %e           ASCII Locale’s abbreviated weekday name.
            %E           ASCII Locale’s full weekday name.
            %w           Weekday as a decimal number [0(Saturday), 6(Friday)].
            %W           Week number of the year (SATURDAY as the first day of the week) as a decimal number [00, 53]. All days in a new year preceding the first Monday are considered to be in week 0.
            %U           Week number of the year (Sunday as the first day of the week) as a decimal number [00, 53]. All days in a new year preceding the first Sunday are considered to be in week 0.

        """

        d1 = JalaliDate(1361, 6, 15)
        self.assertEqual(d1.strftime('%a'), u'د')
        self.assertEqual(d1.strftime('%A'), u'دوشنبه')
        self.assertEqual(d1.strftime('%e'), u'D')
        self.assertEqual(d1.strftime('%E'), u'Doshanbeh')
        self.assertEqual(d1.strftime('%w'), u'2')
        self.assertEqual(d1.strftime('%W'), u'24')


        for i in range(7):
            self.assert_parse_and_format(JalaliDate.min + timedelta(i), '%d %w %W %U')
            self.assertEqual(
                JalaliDate.strptime('1345 10 10 %s' % c.PERSIAN_WEEKDAY_ABBRS[i], '%Y %m %d %a'),
                JalaliDate(year=1345, month=10, day=10))
            self.assertEqual(
                JalaliDate.strptime('1345 10 10 %s' % c.PERSIAN_WEEKDAY_ABBRS_ASCII[i], '%Y %m %d %e'),
                JalaliDate(year=1345, month=10, day=10))
            self.assertEqual(
                JalaliDate.strptime('1345 10 10 %s' % c.PERSIAN_WEEKDAY_NAMES[i], '%Y %m %d %A'),
                JalaliDate(year=1345, month=10, day=10))
            self.assertEqual(
                JalaliDate.strptime('1345 10 10 %s' % c.PERSIAN_WEEKDAY_NAMES_ASCII[i], '%Y %m %d %E'),
                JalaliDate(year=1345, month=10, day=10))

    def test_year(self):
        """
        Testing:
            %y           Year without century as a zero padded decimal number [00, 99].
            %n           Year without century as a decimal number in persian form [۱, ۹۹].
            %u           Year without century as a zero padded decimal number in persian form [۰۱, ۹۹].
            %Y           Year with century as a decimal number [1-3178].
            %N           Year with century as a decimal number in persian form [۱-۳۱۷۸].
            %O           Year with century as a zero padded decimal number in persian form [۰۰۰۱-۳۱۷۸].
        """

        self.assertEqual(JalaliDate(1361, 6, 15).strftime('%y'), u'61')
        self.assertEqual(JalaliDate(1361, 6, 15).strftime('%Y'), u'1361')
        self.assertEqual(JalaliDate(61, 11, 5).strftime('%N'), u'۶۱')
        self.assertEqual(JalaliDate(61, 11, 5).strftime('%O'), u'۰۰۶۱')

        self.assertEqual(JalaliDate.strptime('94', '%y'), JalaliDate(1394))
        self.assertEqual(JalaliDate.strptime('01', '%y'), JalaliDate(1301))
        self.assertEqual(JalaliDate.strptime('00', '%y'), JalaliDate(1300))
        self.assertEqual(JalaliDate.strptime(u'۹۴', '%n'), JalaliDate(1394))
        self.assertEqual(JalaliDate.strptime(u'۱', '%n'), JalaliDate(1301))
        self.assertEqual(JalaliDate.strptime(u'۰', '%n'), JalaliDate(1300))
        self.assertEqual(JalaliDate.strptime(u'۹۴', '%u'), JalaliDate(1394))
        self.assertEqual(JalaliDate.strptime(u'۰۱', '%u'), JalaliDate(1301))
        self.assertEqual(JalaliDate.strptime(u'۰۰', '%u'), JalaliDate(1300))

        self.assertEqual(JalaliDate.strptime(u'۰۰۴', '%N'), JalaliDate(4, 1, 1))
        self.assertEqual(JalaliDate.strptime(u'۰۴', '%N'), JalaliDate(4, 1, 1))
        self.assertEqual(JalaliDate.strptime(u'۴', '%N'), JalaliDate(4, 1, 1))

        self.assertEqual(JalaliDate.strptime(u'۰۰۴', '%O'), JalaliDate(4, 1, 1))
        self.assertEqual(JalaliDate.strptime(u'۰۴', '%O'), JalaliDate(4, 1, 1))
        self.assertEqual(JalaliDate.strptime(u'۴', '%O'), JalaliDate(4, 1, 1))


        this_century = JalaliDate(int(JalaliDate.today().year/100) * 100)
        for i in range(99):
            self.assert_parse_and_format(this_century.replace(year=this_century.year+i), '%y')
            self.assert_parse_and_format(this_century.replace(year=this_century.year+i), '%n')
            self.assert_parse_and_format(this_century.replace(year=this_century.year+i), '%u')

        for i in range(1, 1001):
            self.assert_parse_and_format(JalaliDate(i), '%Y')
            self.assert_parse_and_format(JalaliDate(i), '%N')
            self.assert_parse_and_format(JalaliDate(i), '%O')


    def test_month(self):
        """
        Testing:
            %m           Month as a decimal number [01, 12].
            %R           Month as a decimal number in persian form [۱, ۱۲].
            %P           Month as a zero padded decimal number in persian form [۰۱, ۱۲].
            %b           Locale’s abbreviated month name.
            %B           Locale’s full month name.
            %g           ASCII Locale’s abbreviated month name.
            %G           ASCII Locale’s full month name.

        """

        d1 = JalaliDate(1361, 6, 15)
        self.assertEqual(d1.strftime('%b'), u'شه')
        self.assertEqual(d1.strftime('%B'), u'شهریور')
        self.assertEqual(d1.strftime('%m'), u'06')
        self.assertEqual(d1.strftime('%g'), u'Sh')
        self.assertEqual(d1.strftime('%G'), u'Shahrivar')

        self.assertEqual(JalaliDate(1361, 1, 5).strftime('%R'), u'۱')
        self.assertEqual(JalaliDate(1361, 11, 5).strftime('%P'), u'۱۱')
        self.assertEqual(JalaliDate(1361, 1, 5).strftime('%P'), u'۰۱')

        self.assertEqual(JalaliDate.strptime(u'۷', '%R'), JalaliDate(1, 7, 1))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۰۷', '%R')
        self.assertEqual(JalaliDate.strptime(u'۰۷', '%P'), JalaliDate(1, 7, 1))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۷', '%P')


        # Test months
        for i in range(1, 13):
            self.assertEqual(JalaliDate.strptime(str(i), '%m'), JalaliDate(month=i))
            self.assertEqual(JalaliDate.strptime('1345 %s' % c.PERSIAN_MONTH_ABBRS[i], '%Y %b'),
                             JalaliDate(year=1345, month=i, day=1))
            self.assertEqual(JalaliDate.strptime('1345 %s' % c.PERSIAN_MONTH_NAMES[i], '%Y %B'),
                             JalaliDate(year=1345, month=i, day=1))
            self.assertEqual(JalaliDate.strptime('1345 %s' % c.PERSIAN_MONTH_ABBRS_ASCII[i], '%Y %g'),
                             JalaliDate(year=1345, month=i, day=1))
            self.assertEqual(JalaliDate.strptime('1345 %s' % c.PERSIAN_MONTH_NAMES_ASCII[i], '%Y %G'),
                             JalaliDate(year=1345, month=i, day=1))
            self.assertEqual(JalaliDate.strptime('1345 %s' % rtl(str(i), digits=True), '%Y %R'),
                             JalaliDate(year=1345, month=i, day=1))
            self.assertEqual(JalaliDate.strptime('1345 %s' % rtl('%.2d' % i, digits=True), '%Y %P'),
                             JalaliDate(year=1345, month=i, day=1))



        self.assertRaises(ValueError, JalaliDate.strptime, '13', '%m')
        self.assertRaises(ValueError, JalaliDate.strptime, '0', '%m')
        self.assertRaises(ValueError, JalaliDate.strptime, u'1345 مت', '%Y %b')
        self.assertRaises(ValueError, JalaliDate.strptime, u'1345 شتران', '%Y %B')
        self.assertRaises(ValueError, JalaliDate.strptime, u'1345 مت', '%Y %g')
        self.assertRaises(ValueError, JalaliDate.strptime, u'1345 شتران', '%Y %G')


        start_date = JalaliDate()
        for i in range(1, 501):
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %m %d')
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %b %d')
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %B %d')
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %g %d')
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %G %d')
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %R %d')
            self.assert_parse_and_format(start_date + timedelta(days=i) , '%Y %P %d')


    def test_day(self):
        """
        Testing:
            %d           Day of the month as a decimal number [01, 31].
            %D           Day of the month as a decimal number in persian form [۱, ۳۱].
            %K           Day of the month as a zero padded decimal number in persian form [۰۱, ۳۱].
            %j           Day of the year as a zero padded decimal number [001, 366].
            %J           Day of the year as a decimal number in persian form [۱, ۳۶۶].
            %V           Day of the year as a zero padded decimal number in persian form [..۱, ۳۶۶].

        """

        d1 = JalaliDate(1361, 6, 15)
        self.assertEqual(d1.strftime('%d'), u'15')
        self.assertEqual(d1.strftime('%j'), u'170')
        self.assertEqual(d1.strftime('%D'), u'۱۵')

        self.assertEqual(JalaliDate(1361, 6, 2).strftime('%D'), u'۲')
        self.assertEqual(JalaliDate(1361, 6, 2).strftime('%K'), u'۰۲')
        self.assertEqual(JalaliDate(1361, 6, 2).strftime('%J'), u'۱۵۷')
        self.assertEqual(JalaliDate(1361, 1, 5).strftime('%J'), u'۵')
        self.assertEqual(JalaliDate(1361, 1, 25).strftime('%V'), u'۰۲۵')
        self.assertEqual(JalaliDate(1361, 1, 5).strftime('%V'), u'۰۰۵')

        # Test days
        for i in range(1, 32):
            self.assertEqual(JalaliDate.strptime(str(i), '%d'), JalaliDate(day=i))

        self.assertRaises(ValueError, JalaliDate.strptime, '32', '%d')
        self.assertRaises(ValueError, JalaliDate.strptime, '0', '%d')

        # Test day of year
        for i in range(1, 366):
            self.assertEqual(JalaliDate.strptime(str(i), '%j'), JalaliDate.fromordinal(i))
        self.assertRaises(ValueError, JalaliDate.strptime, '366', '%j')
        self.assertRaises(ValueError, JalaliDate.strptime, '0', '%j')
        self.assertEqual(JalaliDate.strptime('1345 5', '%Y %j'),
                         JalaliDate(year=1345, month=1, day=5))

        self.assertEqual(JalaliDate.strptime('1302 123 3 4', '%Y %j %m %d'),
                         JalaliDate(year=1302, month=4, day=30))

        self.assertEqual(JalaliDate.strptime('1302 3 4', '%Y %m %d'),
                         JalaliDate(year=1302, month=3, day=4))

        self.assertEqual(JalaliDate.strptime(u'۲', '%D'), JalaliDate(2))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۰۲', '%D')

        self.assertEqual(JalaliDate.strptime(u'۰۲', '%K'), JalaliDate(1, 1, 2))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۲', '%K')

        self.assertEqual(JalaliDate.strptime(u'۰۲', '%K'), JalaliDate(1, 1, 2))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۲', '%K')

        self.assertEqual(JalaliDate.strptime(u'۱۵۷', '%J'), JalaliDate(1, 6, 2))
        self.assertEqual(JalaliDate.strptime(u'۷', '%J'), JalaliDate(1, 1, 7))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۰۷', '%J')
        self.assertRaises(ValueError, JalaliDate.strptime, u'۰۴۷', '%J')

        self.assertEqual(JalaliDate.strptime(u'۰۴۷', '%V'), JalaliDate(1, 2, 16))
        self.assertEqual(JalaliDate.strptime(u'۰۰۷', '%V'), JalaliDate(1, 1, 7))
        self.assertRaises(ValueError, JalaliDate.strptime, u'۷', '%V')
        self.assertRaises(ValueError, JalaliDate.strptime, u'۴۷', '%V')


        for i in range(1, 400):
            self.assert_parse_and_format(JalaliDate.fromordinal(i), "%Y-%m-%d")
            self.assert_parse_and_format(JalaliDate.fromordinal(i), "%Y-%m-%D")
            self.assert_parse_and_format(JalaliDate.fromordinal(i), "%Y-%m-%K")
            self.assert_parse_and_format(JalaliDate.fromordinal(i), "%Y-%j")
            self.assert_parse_and_format(JalaliDate.fromordinal(i), "%Y-%J")
            self.assert_parse_and_format(JalaliDate.fromordinal(i), "%Y-%V")


    def test_locale_date(self):
        """
        Testing:
            %x           Locale’s appropriate date representation.
        """
        self.assertEqual(JalaliDate(1361, 6, 15).strftime('%x'), u'دوشنبه ۱۵ شهریور ۱۳۶۱')
        self.assertEqual(JalaliDate().strftime('%x'), u'جمعه ۱ فروردین ۱')
        self.assertEqual(JalaliDate.strptime(u'جمعه ۱ فروردین ۱', '%x'), JalaliDate.min)

        self.assertEqual(JalaliDate(1375, 1, 31).strftime('%x'), u'جمعه ۳۱ فروردین ۱۳۷۵')
        self.assertEqual(JalaliDate.strptime(u'جمعه ۳۱ فروردین ۱۳۷۵%', '%x%%'),
                         JalaliDate(1375, 1, 31))


    def test_percent(self):
        """
        Testing:
            %%      A literal '%' character.
        """
        self.assert_parse_and_format(JalaliDate(1375, 1, 31), "%Y-%m-%d %%")
        self.assert_parse_and_format(JalaliDate(1375, 1, 31), "%Y-%m-%d %% %% %%")


if __name__ == '__main__':
    unittest.main()
