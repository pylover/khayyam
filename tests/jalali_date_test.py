# coding=UTF-8
'''
Created on Mar 7, 2011

@author: vahid
'''
import unittest
from khayyam import JalaliDate, MAXYEAR
from datetime import timedelta, date

class TestJalaliDate(unittest.TestCase):
    
    def setUp(self):
        self.leap_year = 1375
    
    def test_instantiate(self):
        
        jdate = JalaliDate(1376, 5, 23)
        self.assertFalse(jdate is None)
        
        self.assertRaises(ValueError, JalaliDate, MAXYEAR + 1, 5, 23)
        self.assertRaises(ValueError, JalaliDate, MAXYEAR, 13, 23)
        self.assertRaises(ValueError, JalaliDate, MAXYEAR, 12, 30)
        
    def test_is_leap(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        self.assertTrue(jdate.is_leap)
        
    def test_days_in_month(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        self.assertEqual(jdate.days_in_month, 30)
        
    def test_to_from_julian_day(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        jdate2 = JalaliDate.from_julian_days(jdate.tojulianday())
        
        self.assertEqual(jdate, jdate2)
        
    def test_to_from_date(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        jdate2 = JalaliDate.from_date(jdate.todate())
        self.assertEqual(jdate, jdate2)

    def test_iso_calendar(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        self.assertEqual(jdate.isocalendar(), (self.leap_year, 51, 6))
        
    def test_iso_format(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        self.assertEqual(jdate.isoformat(), '%s-12-23' % self.leap_year)

    def test_strftime(self):
        jdate = JalaliDate.strptime(JalaliDate(self.leap_year, 12, 23).isoformat(), '%Y-%m-%d')
        self.assertEqual(jdate.isoformat(), '%s-12-23' % self.leap_year)
        self.assertEqual(jdate.strftime('%a%A%b%B%d%j%m%w%x%y%Y%%%W'), u'پپنجشنبهاساسفند23359125پنجشنبه 23 اسفند 1375751375%51')

        d1 = JalaliDate(1361, 6, 15)
        self.assertEqual(d1.strftime('%a'), 'د')
        self.assertEqual(d1.strftime('%A'), 'دوشنبه')
        self.assertEqual(d1.strftime('%b'), 'شه')
        self.assertEqual(d1.strftime('%B'), 'شهریور')
        self.assertEqual(d1.strftime('%d'), '15')
        self.assertEqual(d1.strftime('%j'), '170')
        self.assertEqual(d1.strftime('%m'), '06')
        self.assertEqual(d1.strftime('%w'), '2')
        self.assertEqual(d1.strftime('%W'), '24')
        self.assertEqual(d1.strftime('%x'), 'دوشنبه 15 شهریور 1361')
        self.assertEqual(d1.strftime('%y'), '61')
        self.assertEqual(d1.strftime('%Y'), '1361')
        self.assertEqual(d1.strftime('%e'), 'D')
        self.assertEqual(d1.strftime('%E'), 'Doshanbeh')
        self.assertEqual(d1.strftime('%g'), 'Sh')
        self.assertEqual(d1.strftime('%G'), 'Shahrivar')
        self.assertEqual(d1.strftime('%%'), '%')

        self.assertEqual(
            d1.strftime('%a%A%b%B%d%j%m%w%W%x%y%Y%e%E%g%G%%'),
            'ددوشنبهشهشهریور1517006224دوشنبه 15 شهریور 1361611361DDoshanbehShShahrivar%')
        self.assertEqual(d1.strftime('%Y-%m-%d'), '1361-06-15')
        self.assertEqual(d1.strftime('اول%Y-%m-%dآخر'), 'اول1361-06-15آخر')


    def test_add(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        jdate2 = jdate + timedelta(10)
        
        self.assertEqual(jdate2, JalaliDate(self.leap_year + 1, 1, 3))
        
    def test_sub(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        jdate2 = jdate - timedelta(10)
        
        self.assertEqual(jdate2, JalaliDate(self.leap_year, 12, 13))
        
        jtimedelta = jdate - JalaliDate(self.leap_year - 1, 12, 1)
        
        self.assertEqual(jtimedelta, timedelta(387))
        
    def test_lt_gt_le_ge_ne_eg(self):
        jdate = JalaliDate(self.leap_year, 12, 23)
        jdate2 = JalaliDate(self.leap_year, 12, 24)
        jdate3 = JalaliDate(self.leap_year, 12, 24)
        
        self.assertTrue(jdate <= jdate2)
        self.assertTrue(jdate != jdate2)
        self.assertFalse(jdate > jdate2)
        self.assertTrue(jdate2 == jdate3)
    
    def test_ordinal(self):
        min = JalaliDate.fromordinal(1)
        max = JalaliDate.fromordinal(JalaliDate.max.toordinal())
        self.assertEqual(min.year, 1)
        self.assertEqual(min.month, 1)
        self.assertEqual(min.day, 1)
        self.assertEqual(min, JalaliDate.min)
        self.assertEqual(max, JalaliDate.max)

    def test_algorithm(self):
        min = date(623, 1, 1)
        max_days = 5000
        days = 0
        while True:
            dt = min + timedelta(days=days)
            jd = JalaliDate.from_date(dt)
            print('Processing day: %s' % jd)
            dt2 = jd.todate()
            self.assertEqual(dt, dt2)
            days += 1
            if days > max_days:
                break

    def test_replace(self):
        d1 = JalaliDate(1391, 12, 30)
        self.assertEqual(d1.replace(year=1395), JalaliDate(1395, 12, 30))
        self.assertEqual(d1.replace(month=1),   JalaliDate(1391, 1, 30))
        self.assertEqual(d1.replace(day=1),     JalaliDate(1391, 12, 1))
        self.assertRaises(ValueError, d1.replace, year=1392)

    def test_strptime(self):
        """
        %Z not working at all
        """

        # Test Year
        self.assertEqual(JalaliDate.strptime('1361', '%Y'), JalaliDate(1361))
        self.assertEqual(JalaliDate.strptime('1361%C', '%Y%C'), JalaliDate(1361))
        self.assertEqual(JalaliDate.strptime('اریا1361گلگشت', 'اریا%Yگلگشت'), JalaliDate(1361))

        # Test months
        for i in range(1, 13):
            self.assertEqual(JalaliDate.strptime(str(i), '%m'), JalaliDate(month=i))
        self.assertRaises(ValueError, JalaliDate.strptime, '13', '%m')
        self.assertRaises(ValueError, JalaliDate.strptime, '0', '%m')

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
        self.assertEqual(JalaliDate.strptime('1345 5', '%Y %j'), JalaliDate(year=1345, month=1, day=5))

        self.assertEqual(JalaliDate.strptime('1302 123 3 4', '%Y %j %m %d'), JalaliDate(year=1302, month=4, day=30))
        self.assertEqual(JalaliDate.strptime('1302 3 4', '%Y %m %d'), JalaliDate(year=1302, month=3, day=4))


        def check_format(jdate ,fmt):
            d_str = jdate.strftime(fmt)
            d2 = JalaliDate.strptime(d_str, fmt)
            self.assertEqual(jdate, d2)

        i = 0
        while i < 100: # * 365:
            i += 1
            d = JalaliDate.fromordinal(i)
            check_format(d ,"%Y-%m-%d %a%A%b%B%j") # "%j%m%w%W%x%y%Y%e%E%g%G%%")



if __name__ == '__main__':
    unittest.main()
