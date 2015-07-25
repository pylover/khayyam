# -*- coding: utf-8 -*-
from khayyam import JalaliDatetime, Timezone, teh_tz
from datetime import timedelta
import unittest
__author__ = 'vahid'

class JalaliDatetimeFormatterTestCase(unittest.TestCase):

    def setUp(self):
        self.leap_year = 1375

    def assert_parse_and_format(self, jdate ,fmt, print_=False):
        jalali_date_str = jdate.strftime(fmt)
        parsed_dt = JalaliDatetime.strptime(jalali_date_str, fmt)
        if print_:
            print(jalali_date_str)
        if jdate != parsed_dt:
            print(repr(jdate))
            print(jalali_date_str)
            print(repr(parsed_dt))
        self.assertEqual(jdate, parsed_dt)


    def test_hour(self):
        """
        Testing:
            %H            Hour (24-hour clock) as a zero padded decimal number [00, 23].
            %k            Hour (24-hour clock) as a decimal number in persian form [۱, ۲۳].
            %h            Hour (24-hour clock) as a zero padded decimal number in persian form [۰۰, ۲۳].
            %I            Hour (12-hour clock) as a zero padded decimal number [01, 12].
            %i            Hour (12-hour clock) as a zero padded decimal number in persian form [۰۱, ۱۲].
            %l            Hour (12-hour clock) as a decimal number in persian form [۱, ۱۲].
        """
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)

        # Test HOUR 24
        self.assertEqual(JalaliDatetime(1386, 12, 23).strftime('%H'), u'00')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 1).strftime('%H'), u'01')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 12).strftime('%H'), u'12')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 13).strftime('%H'), u'13')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 23).strftime('%H'), u'23')
        self.assertEqual(
            (JalaliDatetime(1386, 12, 23, 23, 59, 59) + timedelta(seconds=1)).strftime('%H'), u'00')
        self.assertEqual(JalaliDatetime.strptime('08', '%H'), JalaliDatetime(hour=8))
        self.assertRaises(ValueError, JalaliDatetime.strptime, u'2', '%H')

        self.assertEqual(JalaliDatetime(1386, 12, 23).strftime('%k'), u'۰')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 1).strftime('%k'), u'۱')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 12).strftime('%k'), u'۱۲')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 13).strftime('%k'), u'۱۳')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 23).strftime('%k'), u'۲۳')
        self.assertEqual(
            (JalaliDatetime(1386, 12, 23, 23, 59, 59) + timedelta(seconds=1)).strftime('%k'), u'۰')
        self.assertEqual(JalaliDatetime.strptime(u'۸', '%k'), JalaliDatetime(hour=8))
        self.assertRaises(ValueError, JalaliDatetime.strptime, u'۰۲', '%k')

        self.assertEqual(JalaliDatetime(1386, 12, 23).strftime('%h'), u'۰۰')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 1).strftime('%h'), u'۰۱')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 12).strftime('%h'), u'۱۲')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 13).strftime('%h'), u'۱۳')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 23).strftime('%h'), u'۲۳')
        self.assertEqual(
            (JalaliDatetime(1386, 12, 23, 23, 59, 59) + timedelta(seconds=1)).strftime('%h'), u'۰۰')
        self.assertEqual(JalaliDatetime.strptime(u'۰۸', '%h'), JalaliDatetime(hour=8))
        self.assertRaises(ValueError, JalaliDatetime.strptime, u'۲', '%h')

        # Test HOUR 12
        self.assertEqual(JalaliDatetime(1386, 12, 23).strftime('%I'), u'12')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 1).strftime('%I'), u'01')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 12).strftime('%I'), u'12')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 13).strftime('%I'), u'01')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 23).strftime('%I'), u'11')
        self.assertEqual(
            (JalaliDatetime(1386, 12, 23, 23, 59, 59) + timedelta(seconds=1)).strftime('%I'), u'12')
        self.assertEqual(d1.strftime('%I'), u'12')
        self.assertRaises(ValueError, JalaliDatetime.strptime, u'2', '%I')

        self.assertEqual(JalaliDatetime(1386, 12, 23).strftime('%l'), u'۱۲')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 1).strftime('%l'), u'۱')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 12).strftime('%l'), u'۱۲')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 13).strftime('%l'), u'۱')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 23).strftime('%l'), u'۱۱')
        self.assertEqual(
            (JalaliDatetime(1386, 12, 23, 23, 59, 59) + timedelta(seconds=1)).strftime('%l'), u'۱۲')
        self.assertEqual(d1.strftime('%l'), u'۱۲')
        self.assertRaises(ValueError, JalaliDatetime.strptime, u'۰۲', '%l')

        self.assertEqual(JalaliDatetime(1386, 12, 23).strftime('%i'), u'۱۲')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 1).strftime('%i'), u'۰۱')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 12).strftime('%i'), u'۱۲')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 13).strftime('%i'), u'۰۱')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 23).strftime('%i'), u'۱۱')
        self.assertEqual(
            (JalaliDatetime(1386, 12, 23, 23, 59, 59) + timedelta(seconds=1)).strftime('%i'), u'۱۲')
        self.assertEqual(d1.strftime('%i'), u'۱۲')
        self.assertRaises(ValueError, JalaliDatetime.strptime, u'۲', '%i')

        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in range(1000):
            d_test = d2 + timedelta(hours=i)
            self.assert_parse_and_format(d_test, '%Y-%m-%d %H:%M:%S')
            self.assert_parse_and_format(d_test, '%N-%R-%D %k:%r:%s')
            self.assert_parse_and_format(d_test, '%N-%R-%D %h:%v:%L')
            self.assert_parse_and_format(d_test, '%Y-%m-%d %p %I:%M:%S')
            self.assert_parse_and_format(d_test, '%N-%R-%D %t %i:%r:%s')
            self.assert_parse_and_format(d_test, '%N-%R-%D %p %l:%v:%L')



    def test_minute(self):
        """
        Testing:
            %M            Minute as a decimal number [00, 59].
            %r            Minute as a zero padded decimal number in persian form [۰۰, ۵۹].
            %v            Minute as a decimal number in persian form [۰, ۵۹].
        """
        self.assertEqual(JalaliDatetime(1386, 12, 23, 4, 6).strftime('%M'), u'06')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 4, 6).strftime('%r'), u'۰۶')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 4, 6).strftime('%v'), u'۶')
        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in range(1000):
            d_test = d2 + timedelta(minutes=i)
            self.assert_parse_and_format(d_test, '%Y-%m-%d %H:%M:%S')
            self.assert_parse_and_format(d_test, '%N-%R-%D %H:%r:%s')
            self.assert_parse_and_format(d_test, '%N-%R-%D %H:%v:%L')


    def test_second(self):
        """
        Testing:
            %S            Second as a decimal number [00, 59].
            %s            Second as a zero padded decimal number in persian form [۰۰, ۵۹].
            %L            Second as a decimal number in persian form [۰, ۵۹].
        """
        self.assertEqual(JalaliDatetime(1386, 12, 23, 4, 6, 5).strftime('%S'), u'05')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 4, 6, 5).strftime('%s'), u'۰۵')
        self.assertEqual(JalaliDatetime(1386, 12, 23, 4, 6, 5).strftime('%L'), u'۵')

        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in range(1000):
            d_test = d2 + timedelta(seconds=i)
            self.assert_parse_and_format(d_test, '%Y-%m-%d %H:%M:%S')
            self.assert_parse_and_format(d_test, '%N-%R-%D %H:%r:%s')
            self.assert_parse_and_format(d_test, '%N-%R-%D %H:%r:%L')


    def test_timezone(self):
        """
        Testing:
            %z            UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).
            %o            UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive) in persian format i.e +۰۳:۳۰.
            %Z            Time zone name (empty string if the object is naive).
        """
        # Test Timezone
        tz_dt = JalaliDatetime(tzinfo=Timezone(timedelta(minutes=10)))
        self.assertEqual(JalaliDatetime.strptime('00:10', '%z'), tz_dt)
        self.assertEqual(tz_dt.strftime('%z'), '+00:10')
        tz_dt = JalaliDatetime(tzinfo=Timezone(timedelta(minutes=-30)))
        self.assertEqual(tz_dt.strftime('%z'), '-00:30')
        self.assertEqual(tz_dt.strftime('%o'), u'-۰۰:۳۰')
        self.assertEqual(JalaliDatetime.strptime('', '%o'), JalaliDatetime())
        self.assertEqual(JalaliDatetime.strptime('00:00', '%z'), JalaliDatetime())
        self.assertEqual(JalaliDatetime.strptime('00:01', '%z'),
                         JalaliDatetime(tzinfo=Timezone(timedelta(minutes=1))))
        self.assertNotEqual(JalaliDatetime.strptime('04:30', '%z'), JalaliDatetime.strptime('04:31', '%z'))
        self.assertEqual(JalaliDatetime.strptime('04:30', '%z'), JalaliDatetime.strptime('04:30', '%z'))
        self.assertNotEqual(JalaliDatetime.strptime('04:30', '%z'),
                         JalaliDatetime(tzinfo=teh_tz))
        self.assertEqual(JalaliDatetime.strptime('+04:30', '%z').utcoffset(), timedelta(hours=4.50))

        self.assertEqual(JalaliDatetime.strptime(u'۰۰:۰۰', '%o'), JalaliDatetime())
        self.assertEqual(JalaliDatetime.strptime(u'۰۰:۰۱', '%o'),
                         JalaliDatetime(tzinfo=Timezone(timedelta(minutes=1))))
        self.assertNotEqual(JalaliDatetime.strptime(u'۰۴:۳۰', '%o'), JalaliDatetime.strptime('04:31', '%z'))
        self.assertEqual(JalaliDatetime.strptime(u'۰۴:۳۰', '%o'), JalaliDatetime.strptime('04:30', '%z'))
        self.assertNotEqual(JalaliDatetime.strptime(u'۰۴:۳۰', '%o'),
                         JalaliDatetime(tzinfo=teh_tz))
        self.assertEqual(JalaliDatetime.strptime(u'+۰۴:۳۰', '%o').utcoffset(), timedelta(hours=4.50))


        self.assertEqual(tz_dt.strftime('%z'), tz_dt.strftime('%Z'))

        self.assertEqual(
            JalaliDatetime(1394, 4, 28, 18, 14, 35, 962659, Timezone(timedelta(.3))).strftime('%Y-%m-%d %H:%M:%S.%f %z'),
            '1394-04-28 18:14:35.962659 +07:12')

        self.assertEqual(
            JalaliDatetime.strptime('1394-04-28 18:14:35.962659 +07:12', '%Y-%m-%d %H:%M:%S.%f %z'),
            JalaliDatetime(1394, 4, 28, 18, 14, 35, 962659, Timezone(timedelta(.3)))
            )

        self.assertEqual(
            JalaliDatetime.strptime(u'1394-تیر-29 دوشنبه 00:05:14.113389 +04:30', '%Y-%B-%d %A %H:%M:%S.%f %z'),
            JalaliDatetime(1394, 4, 29, 0, 5, 14, 113389, Timezone(timedelta(hours=4, minutes=30)))
        )

    def test_microseconds(self):
        """
        Testing:
            %f            Microsecond as a decimal number [0, 999999], zero-padded on the left
            %F            Microsecond as a decimal number in persian from[۰۰۰۰۰۰, ۹۹۹۹۹۹], zero-padded on the left
        """
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assert_parse_and_format(d1, '%Y-%m-%d %H:%M:%S.%f')
        self.assert_parse_and_format(d1, '%Y-%m-%d %H:%M:%S.%F')
        self.assert_parse_and_format(JalaliDatetime(1375, 12, 23, 12, 0, 0, 0), '%Y-%m-%d %p %I:%M:%S.%f')
        self.assert_parse_and_format(JalaliDatetime(1375, 12, 23, 12, 0, 0, 0), '%Y-%m-%d %p %I:%M:%S.%F')

        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in range(0, 100000000, 100000):
            d_test = d2 + timedelta(microseconds=i)
            self.assert_parse_and_format(d_test, '%Y-%m-%d %H:%M:%S.%f')
            self.assert_parse_and_format(d_test, '%Y-%m-%d %H:%M:%S.%F')


    def test_am_pm(self):
        """
        Testing:
            %p            Locale’s equivalent of either AM or PM in persian format [ق.ظ, ب.ظ].
            %t            Locale’s equivalent of either AM or PM in ASCII format.
        """
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assert_parse_and_format(d1, '%Y-%m-%d %p %I:%M:%S.%f')
        self.assert_parse_and_format(d1, '%Y-%m-%d %t %I:%M:%S.%F')
        self.assert_parse_and_format(JalaliDatetime(1375, 12, 23, 12, 0, 0, 0), '%Y-%m-%d %p %I:%M:%S.%F')
        self.assert_parse_and_format(JalaliDatetime(1375, 12, 23, 12, 0, 0, 0), '%Y-%m-%d %t %I:%M:%S.%F')

        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in range(500):
            d_test = d2 + timedelta(hours=i)
            self.assert_parse_and_format(d_test, '%Y-%m-%d %p %I:%M:%S')
            self.assert_parse_and_format(d_test, '%N-%R-%D %p %i:%r:%s')
            self.assert_parse_and_format(d_test, '%Y-%m-%d %t %I:%M:%S')
            self.assert_parse_and_format(d_test, '%N-%R-%D %t %i:%r:%s')


    def test_locale_date_time(self):
        """
        Testing:
            %c            Locale’s appropriate short date and time representation.
            %C            Locale’s appropriate date and time representation.
            %q            ASCII Locale’s appropriate short date and time representation.
            %Q            ASCII Locale’s appropriate date and time representation.
            %X            Locale’s appropriate time representation.
        """

        self.assertEqual(JalaliDatetime(1361, 6, 15).strftime('%c'), u'د ۱۵ شه ۶۱ ۰:۰')
        self.assertEqual(JalaliDatetime(1361, 6, 15, 19, 34, 2).strftime('%C'), u'دوشنبه ۱۵ شهریور ۱۳۶۱ ۰۷:۳۴:۰۲ ب.ظ')
        self.assertEqual(JalaliDatetime(1361, 6, 15, 19, 34, 2).strftime('%q'), u'D 15 Sh 61 19:34')
        self.assertEqual(JalaliDatetime(1361, 6, 15, 19, 34, 2).strftime('%Q'), u'Doshanbeh 15 Shahrivar 1361 07:34:02 PM')
        self.assertEqual(JalaliDatetime(1361, 6, 15, 19, 34, 2).strftime('%X'), u'۰۷:۳۴:۰۲ ب.ظ')
        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in range(1000):
            d_test = d2 + timedelta(minutes=i)
            self.assert_parse_and_format(d_test, '%c')
            self.assert_parse_and_format(d_test, '%C')
            self.assert_parse_and_format(d_test, '%q')
            self.assert_parse_and_format(d_test, '%Q')
            self.assert_parse_and_format(d_test, '%Y-%m-%d %X')

if __name__ == '__main__':
    unittest.main()

