# -*- coding: utf-8 -*-
import unittest
from khayyam import JalaliDatetime, teh_tz
from datetime import datetime, timedelta
from khayyam.timezones import TehranTimezone, Timezone
from khayyam.jalali_date import JalaliDate
from khayyam.compat import xrange
__author__ = 'vahid'


class TestJalaliDateTime(unittest.TestCase):
    
    def setUp(self):
        self.leap_year = 1375
        self.naive_jdt = JalaliDatetime(self.leap_year, 12, 30, 10, 2, 1, 3)
        self.aware_jdt = JalaliDatetime(self.leap_year, 12, 30, 10, 2, 1, 3, TehranTimezone())
        
    def test_to_from_datetime(self):
        # Naive
        jdate1 = JalaliDatetime.from_datetime(self.naive_jdt.to_datetime())
        self.assertEqual(self.naive_jdt, jdate1)
        
        # Aware
        jdate2 = JalaliDatetime.from_datetime(self.aware_jdt.to_datetime())
        self.assertEqual(self.aware_jdt, jdate2)
        
    def test_today(self):
        dt = datetime.now().date()
        jdt = JalaliDatetime.today().date()
        self.assertEqual(jdt, JalaliDate.from_date(dt))
        
    def test_now(self):
        self.assertIsNotNone(JalaliDatetime.now())
        
    def test_utcnow(self):
        jutcnow = JalaliDatetime.utcnow()
        utcnow = jutcnow.to_datetime()
        self.assertEqual(jutcnow.time(), utcnow.time())
    
    def test_strftime_strptime(self):
        """
%H            Hour (24-hour clock) as a decimal number [00,23].
%I            Hour (12-hour clock) as a decimal number [01,12].
%M            Minute as a decimal number [00,59].
%S            Second as a decimal number [00,61].    (3)
%f            Microsecond as a decimal number [0,999999], zero-padded on the left    (1)
%p            Locale’s equivalent of either AM or PM.    (2)
%c            Locale’s appropriate short date and time representation.
%C            Locale’s appropriate date and time representation.
%q            ASCII Locale’s appropriate short date and time representation.
%Q            ASCII Locale’s appropriate date and time representation.
%U            Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (4)
%X            Locale’s appropriate time representation.
%z            UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).    (5)
%Z            Time zone name (empty string if the object is naive).
        """

        def check_format(jdate ,fmt):
            jdate_str = jdate.strftime(fmt)
            d2 = JalaliDatetime.strptime(jdate_str, fmt)
            if jdate != d2:
                print(repr(jdate))
                print(repr(d2))
            self.assertEqual(jdate, d2)

        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)


        # Test HOUR
        self.assertEqual(d1.strftime('%H'), u'12')
        self.assertEqual(JalaliDatetime.strptime('8', '%H'), JalaliDatetime(hour=8))

        # Test Timezone
        tz_dt = JalaliDatetime(tzinfo=Timezone(timedelta(minutes=10)))
        self.assertEqual(JalaliDatetime.strptime('00:10', '%z'), tz_dt)
        self.assertEqual(tz_dt.strftime('%z'), '+00:10')
        tz_dt = JalaliDatetime(tzinfo=Timezone(timedelta(minutes=-30)))
        self.assertEqual(tz_dt.strftime('%z'), '-00:30')
        self.assertEqual(JalaliDatetime.strptime('', '%z'), JalaliDatetime())
        self.assertEqual(JalaliDatetime.strptime('00:00', '%z'), JalaliDatetime())
        self.assertEqual(JalaliDatetime.strptime('00:01', '%z'),
                         JalaliDatetime(tzinfo=Timezone(timedelta(minutes=1))))
        self.assertNotEqual(JalaliDatetime.strptime('04:30', '%z'), JalaliDatetime.strptime('04:31', '%z'))
        self.assertEqual(JalaliDatetime.strptime('04:30', '%z'), JalaliDatetime.strptime('04:30', '%z'))
        self.assertNotEqual(JalaliDatetime.strptime('04:30', '%z'),
                         JalaliDatetime(tzinfo=teh_tz))
        self.assertEqual(JalaliDatetime.strptime('+04:30', '%z').utcoffset(), timedelta(hours=4.50))
        self.assertEqual(tz_dt.strftime('%z'), tz_dt.strftime('%Z'))

        self.assertEqual(
            JalaliDatetime(1394, 4, 28, 18, 14, 35, 962659, Timezone(timedelta(.3))).strftime('%Y-%m-%d %H:%M:%S.%f %z'),
            '1394-04-28 18:14:35.962659 +07:12')

        self.assertEqual(
            JalaliDatetime.strptime('1394-04-28 18:14:35.962659 +07:12', '%Y-%m-%d %H:%M:%S.%f %z'),
            JalaliDatetime(1394, 4, 28, 18, 14, 35, 962659, Timezone(timedelta(.3)))
            )

        check_format(d1, '%Y-%m-%d %H:%M:%S.%f')
        check_format(JalaliDatetime(1375, 12, 23, 12, 0, 0, 0), '%Y-%m-%d %p %I:%M:%S.%f')

        self.assertEqual(
            JalaliDatetime.strptime('1394-تیر-29 دوشنبه 00:05:14.113389 +04:30', '%Y-%B-%d %A %H:%M:%S.%f %z'),
            JalaliDatetime(1394, 4, 29, 0, 5, 14, 113389, Timezone(timedelta(hours=4, minutes=30)))
        )

        d2 = JalaliDatetime(self.leap_year, 12, 23)
        for i in xrange(100):
            d_test = d2 + timedelta(hours=i)
            check_format(d_test, '%Y%m%d%H%a%A%b%B%c%C%f%I%j%M%p%S%w%x%X%y%g%G%e%E%W%%')
            check_format(d_test, '%Y-%m-%d %p %I:%M:%S.%f')
            check_format(d_test, '%Y-%m-%d %X')
            check_format(d_test, '%x %H')
            check_format(d_test, '%c')
            check_format(d_test, '%C')
            check_format(d_test, '%q')
            check_format(d_test, '%Q')

        self.assertEqual(d1.isoformat(), '%s-12-23T12:03:45.034567' % self.leap_year)


        tz_datetime = d1.astimezone(teh_tz)
        self.assertEqual(tz_datetime.strftime('%Z'), 'Iran/Tehran')


    def test_iso_format(self):
        jdate = JalaliDatetime(self.leap_year, 12, 23)
        self.assertEqual(jdate.isoformat(), '%s-12-23T00:00:00.000000' % self.leap_year)

    def test_algorithm(self):
        min = datetime(1900, 1, 1, 1, 1, 1)
        max_days = 5000 # 3000 years !
        days = 0
        while True:
            dt = min + timedelta(days=days)
            jd = JalaliDatetime.from_datetime(dt)
            # print('Processing day: %s' % jd.year)
            dt2 = jd.to_datetime()
            self.assertEqual(dt, dt2)
            days += 1
            if days > max_days:
                break;

    def test_add(self):
        jdate = JalaliDatetime(self.leap_year, 12, 23)
        jdate2 = jdate + timedelta(10)
        
        self.assertEqual(jdate2, JalaliDatetime(self.leap_year + 1, 1, 3))
        
    def test_sub(self):
        jdate = JalaliDatetime(self.leap_year, 12, 23)
        jdate2 = jdate - timedelta(10)
        
        self.assertEqual(jdate2, JalaliDatetime(self.leap_year, 12, 13))
        
        jtimedelta = jdate - JalaliDatetime(self.leap_year - 1, 12, 1)
        
        self.assertEqual(jtimedelta, timedelta(387))
        
    def test_lt_gt_le_ge_ne_eg(self):
        jdate = JalaliDatetime(self.leap_year, 12, 23)
        jdate2 = JalaliDatetime(self.leap_year, 12, 24)
        jdate3 = JalaliDatetime(self.leap_year, 12, 24)
        
        self.assertTrue(jdate <= jdate2)
        self.assertTrue(jdate != jdate2)
        self.assertFalse(jdate > jdate2)
        self.assertTrue(jdate2 == jdate3)

    def test_replace(self):
        d1 = JalaliDatetime(1391, 12, 30)
        self.assertEqual(d1.replace(year=1395), JalaliDatetime(1395, 12, 30))
        self.assertEqual(d1.replace(month=1),   JalaliDatetime(1391, 1, 30))
        self.assertEqual(d1.replace(day=1),     JalaliDatetime(1391, 12, 1))
        self.assertRaises(ValueError, d1.replace, year=1392)
    
if __name__ == '__main__':
    unittest.main()
