# -*- coding: utf-8 -*-
import unittest

from khayyam import JalaliDatetime, teh_tz, Timezone
from datetime import datetime, timedelta, time, tzinfo
from khayyam.timezones import TehranTimezone
from khayyam.jalali_date import JalaliDate
__author__ = 'vahid'


class TestJalaliDateTime(unittest.TestCase):
    
    def setUp(self):
        self.leap_year = 1375
        self.naive_jdt = JalaliDatetime(self.leap_year, 12, 30, 10, 2, 1, 3)
        self.aware_jdt = JalaliDatetime(self.leap_year, 12, 30, 10, 2, 1, 3, TehranTimezone())

    def test_instantiate(self):

        jalali_time = JalaliDatetime(1376, 10, 9, 8, 7, 6, 5)
        self.assertFalse(jalali_time is None)

        self.assertEqual(JalaliDatetime(jalali_time.todatetime()), jalali_time)
        self.assertEqual(JalaliDatetime(jalali_time), jalali_time)
        self.assertEqual(JalaliDatetime(jalali_time.date()).date(), jalali_time.date())
        self.assertEqual(JalaliDatetime(julian_day=2450674), JalaliDatetime(1376, 5, 23))
        self.assertEqual(
            JalaliDatetime(1361, 6, 15, tzinfo=TehranTimezone),
            JalaliDatetime(1361, 6, 15, tzinfo=TehranTimezone())
        )

    def test_to_from_datetime(self):
        # Naive
        jalali_time1 = JalaliDatetime(self.naive_jdt.todatetime())
        self.assertEqual(self.naive_jdt, jalali_time1)
        
        # Aware
        jalali_time2 = JalaliDatetime(self.aware_jdt.todatetime())
        self.assertEqual(self.aware_jdt, jalali_time2)
        
    def test_today(self):
        dt = datetime.now().date()
        jdt = JalaliDatetime.today().date()
        self.assertEqual(jdt, JalaliDate(dt))
        
    def test_now(self):
        self.assertIsNotNone(JalaliDatetime.now())
        self.assertIsNone(JalaliDatetime.now().tzinfo)
        self.assertIsNotNone(JalaliDatetime.now(TehranTimezone()).tzinfo)
        
    def test_utcnow(self):
        jalali_utcnow = JalaliDatetime.utcnow()
        datetime_utcnow = jalali_utcnow.todatetime()
        self.assertEqual(jalali_utcnow.time(), datetime_utcnow.time())
        self.assertEqual(jalali_utcnow.timetz(), datetime_utcnow.timetz())
    
    def test_strftime_strptime(self):
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assertEqual(d1.strftime('%Q'), 'Panjshanbeh 23 Esfand 1375 12:03:45 PM')
        self.assertEqual(
            d1.strptime('Panjshanbeh 23 Esfand 1375 12:03:45 PM', '%Q'),
            d1 - timedelta(microseconds=34567))

        self.assertEqual(d1.isoformat(), '%s-12-23T12:03:45.034567' % self.leap_year)
        tz_datetime = d1.astimezone(teh_tz)
        self.assertEqual(tz_datetime.strftime('%Z'), 'Iran/Tehran')

    def test_iso_format(self):
        jalali_time = JalaliDatetime(self.leap_year, 12, 23)
        self.assertEqual(jalali_time.isoformat(), '%s-12-23T00:00:00.000000' % self.leap_year)
        jalali_time = JalaliDatetime(self.leap_year, 12, 23, tzinfo=teh_tz)
        self.assertEqual(jalali_time.isoformat(), '%s-12-23T00:00:00.000000+03:30' % self.leap_year)

    def test_algorithm(self):
        min_date = datetime(1900, 1, 1, 1, 1, 1)
        max_days = 5000  # 3000 years !
        days = 0
        while True:
            dt = min_date + timedelta(days=days)
            jd = JalaliDatetime(dt)
            # print('Processing day: %s' % jd.year)
            dt2 = jd.todatetime()
            self.assertEqual(dt, dt2)
            days += 1
            if days > max_days:
                break

    def test_add(self):
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23)
        jalali_tme2 = jalali_time1 + timedelta(10)
        self.assertEqual(jalali_tme2, JalaliDatetime(self.leap_year + 1, 1, 3))
        
    def test_sub(self):
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23)
        jalali_time2 = jalali_time1 - timedelta(10)
        self.assertEqual(jalali_time2, JalaliDatetime(self.leap_year, 12, 13))
        difference = jalali_time1 - JalaliDatetime(self.leap_year - 1, 12, 1)
        self.assertEqual(difference, timedelta(387))
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23, 4, 2, 10, 7)
        self.assertEqual(jalali_time1 - jalali_time1.date(), timedelta(hours=4, minutes=2, seconds=10, microseconds=7))

    def test_lt_gt_le_ge_ne_eg(self):
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23)
        jalali_time2 = JalaliDatetime(self.leap_year, 12, 24)
        jalali_time3 = JalaliDatetime(self.leap_year, 12, 24)
        
        self.assertTrue(jalali_time1 <= jalali_time2)
        self.assertTrue(jalali_time1 != jalali_time2)
        self.assertFalse(jalali_time1 > jalali_time2)
        self.assertTrue(jalali_time2 == jalali_time3)

    def test_replace(self):
        d1 = JalaliDatetime(1391, 12, 30)
        self.assertEqual(d1.replace(year=1395), JalaliDatetime(1395, 12, 30))
        self.assertEqual(d1.replace(month=1),   JalaliDatetime(1391, 1, 30))
        self.assertEqual(d1.replace(day=1),     JalaliDatetime(1391, 12, 1))
        self.assertRaises(ValueError, d1.replace, year=1392)

    def test_repr(self):
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assertEqual(repr(d1), 'khayyam.JalaliDatetime(1375, 12, 23, 12, 3, 45, 34567, Panjshanbeh)')

    def test_properties(self):
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assertEqual(d1.year, self.leap_year)
        self.assertEqual(d1.month, 12)
        self.assertEqual(d1.day, 23)
        self.assertEqual(d1.hour, 12)
        self.assertEqual(d1.minute, 3)
        self.assertEqual(d1.second, 45)
        self.assertEqual(d1.microsecond, 34567)
        self.assertEqual(d1.ampm(), u'ب.ظ')

        d1.year = 1361
        d1.month = 6
        d1.day = 15
        self.assertRaises(AttributeError, setattr, d1, 'hour', 16)
        self.assertRaises(AttributeError, setattr, d1, 'minute', 16)
        self.assertRaises(AttributeError, setattr, d1, 'second', 16)
        self.assertRaises(AttributeError, setattr, d1, 'microsecond', 16)
        self.assertRaises(AttributeError, setattr, d1, 'tzinfo', teh_tz)

    def test_fromtimestamp(self):
        ts = 1471628912.749938

        self.assertEqual(
            JalaliDatetime.fromtimestamp(ts),
            JalaliDatetime.combine(JalaliDatetime(1395, 5, 29), datetime.fromtimestamp(ts).time())
        )

        self.assertEqual(
            JalaliDatetime.utcfromtimestamp(ts),
            JalaliDatetime.combine(JalaliDatetime(1395, 5, 29), datetime.utcfromtimestamp(ts).time())
        )

    def test_ordinal(self):
        self.assertEqual(JalaliDatetime.min.toordinal(), 1)
        self.assertEqual(JalaliDatetime.max.toordinal(), 1160739)

        min_ = JalaliDatetime.fromordinal(JalaliDatetime.min.toordinal())
        max_ = JalaliDatetime.fromordinal(JalaliDatetime.max.toordinal())
        self.assertEqual(min_.year, 1)
        self.assertEqual(min_.month, 1)
        self.assertEqual(min_.day, 1)
        self.assertEqual(min_, JalaliDatetime.min)
        self.assertEqual(max_, JalaliDatetime.max.replace(hour=0, minute=0, second=0, microsecond=0))

    def test_combine(self):
        dt = JalaliDate(1361, 11, 6)
        t = time(10, 11, 12)
        self.assertEqual(JalaliDatetime.combine(dt, t), JalaliDatetime(1361, 11, 6, 10, 11, 12))

    def test_astimezone(self):
        d1 = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938, tzinfo=teh_tz)
        tz_fake = Timezone(timedelta(hours=2))
        self.assertEqual(d1.astimezone(teh_tz), d1)
        self.assertEqual(d1.astimezone(tz_fake), JalaliDatetime(1395, 5, 29, 19, 48, 32, 749938, tzinfo=tz_fake))

    def test_utcoffset(self):
        d1 = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938, tzinfo=teh_tz)
        naive = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938)
        self.assertEqual(d1.utcoffset(), timedelta(minutes=270))
        self.assertIsNone(naive.utcoffset())

    def test_tzname(self):
        d1 = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938, tzinfo=teh_tz)
        naive = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938)
        self.assertEqual(d1.tzname(), u'Iran/Tehran')
        self.assertIsNone(naive.tzname())

    def test_formats(self):
        d1 = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938, tzinfo=teh_tz)
        naive = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938)
        self.assertEqual(d1.localshortformat(), u'ج 29 مر 95 22:18')
        self.assertEqual(d1.localshortformatascii(), u'J 29 Mo 95 22:18')
        self.assertEqual(d1.localdatetimeformat(), u'جمعه 29 مرداد 1395 10:18:32 ب.ظ')
        self.assertEqual(d1.localdatetimeformatascii(), u'Jomeh 29 Mordad 1395 10:18:32 PM')
        self.assertEqual(d1.localtimeformat(), u'10:18:32 \u0628.\u0638')
        self.assertEqual(d1.utcoffsetformat(), u'04:30')
        self.assertEqual(naive.utcoffsetformat(), u'')
        self.assertEqual(d1.tznameformat(), u'Iran/Tehran')
        self.assertEqual(naive.tznameformat(), u'')

    def test_day_of_year(self):
        d1 = JalaliDatetime(1395, 5, 29, 22, 18, 32, 749938, tzinfo=teh_tz)
        self.assertEqual(d1.dayofyear(), 153)

    def test_str(self):
        d1 = JalaliDatetime(1361, 6, 15)
        self.assertEqual(
            d1.__str__(),
            d1.isoformat(sep=' ')
        )

    def test_operators(self):
        invalid_object = dict(a=2)
        d1 = JalaliDatetime(1361, 6, 15, 10, 1)
        d2 = JalaliDatetime(1361, 6, 15, 10, 2)
        self.assertRaises(TypeError, d1.__add__, invalid_object)
        self.assertRaises(TypeError, d1.__sub__, invalid_object)
        self.assertRaises(TypeError, d1.__lt__, invalid_object)
        self.assertRaises(TypeError, d1.__gt__, invalid_object)
        self.assertRaises(TypeError, d1.__eq__, invalid_object)
        self.assertFalse(d1 == 0)
        self.assertTrue(d1 == d1.todatetime())
        self.assertTrue(d1 < d2)
        self.assertTrue(d1 <= d1.copy())
        self.assertFalse(d1 > d2)
        self.assertTrue(d1 >= d1.copy())

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
