# -*- coding: utf-8 -*-
import unittest
from khayyam.timezones import TehranTimezone, Timezone
from khayyam import JalaliDatetime
from datetime import datetime, timedelta
__author__ = 'vahid'


class TestTehTz(unittest.TestCase):
    
    def setUp(self):
        self.teh_tz = TehranTimezone()
        self.dt = datetime(2000, 1, 1)
        self.dtz = datetime(2000, 1, 1, tzinfo=self.teh_tz)
        self.another_tz = Timezone(timedelta(hours=5))
        self.zero_tz = Timezone(timedelta())

    def test_dst(self):
        naive_time = JalaliDatetime(1390, 12, 29, 1, 1, 1, 1)
        dst_aware_time = JalaliDatetime(1390, 12, 29, 1, 1, 1, 1, tzinfo=self.teh_tz)
        dst_time = dst_aware_time + timedelta(5)
        self.assertIsNotNone(dst_time.dst(), "invalid dst")
        self.assertEqual(dst_aware_time.dst(), timedelta(0), "invalid dst")
        self.assertIsNone(naive_time.dst(), "invalid dst")

    def test_repr(self):
        t = TehranTimezone()
        self.assertEqual(type(repr(t)), str)
        self.assertEqual(repr(t), '+03:30 dst:60')

    def test_fromutc(self):
        self.assertRaises(ValueError, self.teh_tz.fromutc, JalaliDatetime(1390, 12, 29, 1, 1, 1, 1, tzinfo=self.another_tz))
        self.assertRaises(ValueError, self.teh_tz.fromutc, JalaliDatetime(1390, 12, 29, 1, 1, 1, 1))
        self.assertEqual(
            self.teh_tz.fromutc(JalaliDatetime(1390, 2, 1, 1, 1, 1, 1, tzinfo=self.teh_tz)),
            JalaliDatetime(1390, 2, 1, 5, 31, 1, 1, tzinfo=self.teh_tz)
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()        
