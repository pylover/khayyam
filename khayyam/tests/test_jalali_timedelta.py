# -*- coding: utf-8 -*-
import unittest

from khayyam import JalaliTimedelta


class TestJalaliTimedelta(unittest.TestCase):
    def setUp(self):
        pass

    def test_strftime_strptime(self):
        d1 = JalaliTimedelta(
            days=12,
            seconds=23,
            microseconds=12,
            milliseconds=3,
            minutes=45,
            hours=34567
        )
        self.assertEqual(d1.total_hours, 34855.75638888889)
        self.assertEqual(d1.strftime('%H'), '34855')
        self.assertEqual(d1.strftime('%I'), '07')
        self.assertEqual(d1.strftime('%k'), u'۳۴۸۵۵')
        self.assertEqual(d1.strftime('%h'), u'۰۷')
        self.assertEqual(d1.strftime('%M'), u'2091345')
        self.assertEqual(d1.strftime('%m'), u'45')
        self.assertEqual(d1.strftime('%S'), u'125480723')
        self.assertEqual(d1.strftime('%s'), u'23')
        self.assertEqual(d1.strftime('%f'), u'003012')
        self.assertEqual(d1.strftime('%t'), u'003')

        self.assertEqual(JalaliTimedelta.strptime('34855', '%H').total_seconds(), 125478000)
        self.assertEqual(JalaliTimedelta.strptime(u'۳۴۸۵۵', '%k').total_seconds(), 125478000)

        self.assertEqual(JalaliTimedelta.strptime('07', '%I').total_seconds(), 25200)
        self.assertEqual(JalaliTimedelta.strptime('34343 08', '%H %I').total_hours, 34343)
        self.assertEqual(JalaliTimedelta.strptime('34343 08', '%H %I').hours, 23)

        self.assertEqual(JalaliTimedelta.strptime('34855', '%M').total_seconds(), 2091300)
        self.assertEqual(JalaliTimedelta.strptime('07', '%m').total_seconds(), 420)
        self.assertEqual(JalaliTimedelta.strptime('34343 08', '%M %m').total_minutes, 34343)
        self.assertEqual(JalaliTimedelta.strptime('34343 08', '%M %m').minutes, 23)
        self.assertEqual(JalaliTimedelta.strptime('34343 08', '%S %s').total_seconds(), 34343)
        self.assertEqual(JalaliTimedelta.strptime('34343 08', '%S %s').seconds, 23)
        self.assertEqual(JalaliTimedelta.strptime('34343', '%f').microseconds, 34343)
        self.assertEqual(JalaliTimedelta.strptime('100', '%t').milliseconds, 100)

############################################
        # self.assertEqual(
        #     d1.strptime('Panjshanbeh 23 Esfand 1375 12:03:45 PM', '%Q'),
        #     d1 - timedelta(microseconds=34567))
        #
        # self.assertEqual(d1.isoformat(), '%s-12-23T12:03:45.034567' % self.leap_year)
        # tz_datetime = d1.astimezone(teh_tz)
        # self.assertEqual(tz_datetime.strftime('%Z'), 'Iran/Tehran')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
