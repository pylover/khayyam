# -*- coding: utf-8 -*-
import unittest
from khayyam.timezones import TehranTimezone
from khayyam import JalaliDatetime
from datetime import datetime, timedelta

class TestTehTz(unittest.TestCase):
    
    def setUp(self):
        self.tz = TehranTimezone()
        self.dt = datetime(2000, 1, 1)
        self.dtz = datetime(2000, 1, 1, tzinfo=self.tz)

#    def first_test(self):
#        n = datetime.now()
#        n.astimezone(self.tz)
        
    def test_dst(self):
        naive_time = JalaliDatetime(1390, 12, 29, 1, 1, 1, 1)
        nodst_time = JalaliDatetime(1390, 12, 29, 1, 1, 1, 1, tzinfo=self.tz)
        dst_time = nodst_time + timedelta(5)
        self.assertIsNotNone(dst_time.dst(), "invalid dst")
        self.assertEqual(nodst_time.dst(), timedelta(0), "invalid dst")
        self.assertIsNone(naive_time.dst(), "invalid dst")

        
    
if __name__ == '__main__':
    unittest.main()        
