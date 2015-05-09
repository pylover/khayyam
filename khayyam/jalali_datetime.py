# -*- coding: utf-8 -*-
__author__ = 'vahid'


from datetime import timedelta, time, datetime
from time import struct_time
from .algorithms import get_julian_day_from_gregorian, \
    jalali_date_from_julian_day, \
    gregorian_date_from_julian_day, \
    parse

from .jalali_date import JalaliDate, MINYEAR, MAXYEAR
from khayyam.helpers import replace_if_match

AM_PM = {0: u'ق.ظ',
         1: u'ب.ظ'}


class JalaliDatetime(JalaliDate):
    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        if isinstance(year, JalaliDate):
            jd = year
            year = jd.year
            month = jd.month
            day = jd.day

        JalaliDate.__init__(self, year, month, day)
        self._time = time(hour, minute, second, microsecond, tzinfo)

    # #################
    ### Properties ###
    ##################


    def get_hour(self):
        return self._time.hour

    def set_hour(self, val):
        self._time.hour = val

    hour = property(get_hour, set_hour)

    def get_minute(self):
        return self._time.minute

    def set_minute(self, val):
        self._time.minute = val

    minute = property(get_minute, set_minute)

    def get_second(self):
        return self._time.second

    def set_second(self, val):
        self._time.second = val

    second = property(get_second, set_second)

    def get_microsecond(self):
        return self._time.microsecond

    def set_microsecond(self, val):
        self._time.microsecond = val

    microsecond = property(get_microsecond, set_microsecond)

    def get_tzinfo(self):
        return self._time.tzinfo

    def set_tzinfo(self, val):
        self._time.tzinfo = val

    tzinfo = property(get_tzinfo, set_tzinfo)


    #####################
    ### Class Methods ###
    #####################

    @classmethod
    def from_datetime(cls, dt, tz=None):
        julian_days = get_julian_day_from_gregorian(dt.year, dt.month, dt.day)
        arr = jalali_date_from_julian_day(julian_days)
        if not tz:
            tz = dt.tzinfo
        return cls(arr[0], arr[1], arr[2], dt.hour, dt.minute, dt.second, dt.microsecond, tz)

    @classmethod
    def now(cls, tz=None):
        """
        Return the current local date and _time. If optional argument tz is None or not specified, this is like today(), but, if possible, supplies more precision than can be gotten from going through a _time._time() timestamp (for example, this may be possible on platforms supplying the C gettimeofday() function).
        
        Else tz must be an instance of a class tzinfo subclass, and the current date and _time are converted to tz's _time zone. In this case the result is equivalent to tz.fromutc(datetime.utcnow().replace(tzinfo=tz)). See also today(), utcnow().        
        """
        return cls.from_datetime(datetime.now(tz))

    @classmethod
    def utcnow(cls):
        """
        Return the current UTC date and _time, with tzinfo None. This is like now(), but returns the current UTC date and _time, as a naive datetime object. See also now().
        """
        return cls.from_datetime(datetime.utcnow())

    @classmethod
    def dstnow(cls, tz):
        now = cls.now(tz=tz)
        return now + now.dst()

    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        """
        Return the local date and _time corresponding to the POSIX timestamp, such as is returned by _time._time(). If optional argument tz is None or not specified, the timestamp is converted to the platform's local date and _time, and the returned datetime object is naive.
        
        Else tz must be an instance of a class tzinfo subclass, and the timestamp is converted to tz's _time zone. In this case the result is equivalent to tz.fromutc(datetime.utcfromtimestamp(timestamp).replace(tzinfo=tz)).
        
        fromtimestamp() may raise ValueError, if the timestamp is out of the range of values supported by the platform C localtime() or gmtime() functions. It's common for this to be restricted to years in 1970 through 2038. Note that on non-POSIX systems that include leap seconds in their notion of a timestamp, leap seconds are ignored by fromtimestamp(), and then it's possible to have two timestamps differing by a second that yield identical datetime objects. See also utcfromtimestamp().
        """
        return cls.from_datetime(datetime.fromtimestamp(timestamp, tz=tz))

    @classmethod
    def utcfromtimestamp(cls, timestamp):
        """
        Return the UTC datetime corresponding to the POSIX timestamp, with tzinfo None. This may raise ValueError, if the timestamp is out of the range of values supported by the platform C gmtime() function. It's common for this to be restricted to years in 1970 through 2038. See also fromtimestamp().
        """
        return cls.from_datetime(datetime.utcfromtimestamp(timestamp))

    @classmethod
    def fromordinal(cls, ordinal):
        """
        Return the jalali datetime corresponding to the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1. ValueError is raised unless 1 <= ordinal <= datetime.max.toordinal(). The hour, minute, second and microsecond of the result are all 0, and tzinfo is None.
        """
        return cls.from_datetime(datetime.fromordinal(ordinal))

    @classmethod
    def combine(cls, date, _time):
        """
        Return a new jalali datetime object whose date members are equal to the given date object's, and whose _time and tzinfo members are equal to the given _time object's. For any datetime object d, d == datetime.combine(d.date(), d.timetz()). If date is a datetime object, its _time and tzinfo members are ignored.
        """
        if isinstance(date, (JalaliDatetime, JalaliDate)):
            date = date.to_datetime()
        return cls.from_datetime(datetime.combine(date, _time))


    @classmethod
    def strptime(cls, date_string, frmt):
        """
        Return a datetime corresponding to date_string, parsed according to format. This is equivalent to datetime(*(_time.strptime(date_string, format)[0:6])). ValueError is raised if the date_string and format can't be parsed by _time.strptime() or if it returns a value which isn't a _time tuple. See section strftime() and strptime() Behavior.
        '1387/4/12'
        '%Y/%m/%d'
        """
        # TODO: Implement full features of python, see: http://docs.python.org/library/datetime.html
        valid_codes = {'%Y': (4, 'year'),
                       '%m': (2, 'month'),
                       '%d': (2, 'day'),
                       '%H': (2, 'hour'),
                       '%M': (2, 'minute'),
                       '%S': (2, 'second'),
                       '%f': (6, 'microsecond')
        }

        return parse(cls, date_string, frmt, valid_codes)


    ########################
    ### Instance Methods ###
    ########################


    def to_datetime(self):
        arr = gregorian_date_from_julian_day(self.tojulianday())
        return datetime(int(arr[0]), int(arr[1]), int(arr[2]), self.hour, self.minute, self.second, self.microsecond,
                        self.tzinfo)

    def date(self):
        return JalaliDate(self.year, self.month, self.day)

    def time(self):
        return time(self.hour, self.minute, self.second, self.microsecond)

    def timetz(self):
        return time(self.hour, self.minute, self.second, self.microsecond, self.tzinfo)

    def replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                tzinfo=None):
        year, month, day = self._validate(
            year if year else self.year,
            month if month else self.month,
            day if day else self.day)

        result = JalaliDatetime(year, month, day, self.hour, self.minute, self.second, self.microsecond)

        if hour: result.hour = hour
        if minute: result.minute = minute
        if second: result.second = second
        if microsecond: result.microsecond
        if tzinfo: result.tzinfo
        return result

    def astimezone(self, tz):
        if self.tzinfo is tz:
            return self
        utc = (self - self.utcoffset()).replace(tzinfo=tz)
        return tz.fromutc(utc)

    def utcoffset(self):
        if self.tzinfo:
            return self.tzinfo.utcoffset(self)
        else:
            return None

    def dst(self):
        if self.tzinfo:
            return self.tzinfo.dst(self)
        else:
            return None

    def tzname(self):
        if self.tzinfo:
            return self.tzinfo.tzname()
        else:
            return None

    # Removed. By vahid
    # def timetuple(self):
    #     isdst = -1
    #     if self.tzinfo:
    #         if self.tzinfo.dst(self):
    #             isdst = 1
    #         else:
    #             isdst = 2
    #     return struct_time([
    #         self.year,
    #         self.month,
    #         self.day,
    #         self.hour,
    #         self.minute,
    #         self.second,
    #         self.weekday(),
    #         self.dayofyear(),
    #         isdst])
    #
    #
    # def utctimetuple(self):
    #     if not self.tzinfo:
    #         return self.timetuple()
    #     utc = self - self.utcoffset()
    #     return struct_time([
    #         utc.year,
    #         utc.month,
    #         utc.day,
    #         utc.hour,
    #         utc.minute,
    #         utc.second,
    #         utc.weekday(),
    #         utc.dayofyear(),
    #         0])


    def isoformat(self, sep='T'):
        return self.strftime('%Y-%m-%d' + sep + '%H:%M:%S.%f')

    def strftime(self, format):
        """
=========    =======
Directive    Meaning
=========    =======
%a            Locale’s abbreviated weekday name.     
%A            Locale’s full weekday name.     
%b            Locale’s abbreviated month name.     
%B            Locale’s full month name.     
%c            Locale’s appropriate short date and time representation.     
%C            Locale’s appropriate date and time representation.
%d            Day of the month as a decimal number [01,31].     
%f            Microsecond as a decimal number [0,999999], zero-padded on the left    (1)
%H            Hour (24-hour clock) as a decimal number [00,23].     
%I            Hour (12-hour clock) as a decimal number [01,12].     
%j            Day of the year as a decimal number [001,366].     
%m            Month as a decimal number [01,12].     
%M            Minute as a decimal number [00,59].     
%p            Locale’s equivalent of either AM or PM.    (2)
%S            Second as a decimal number [00,61].    (3)
%U            Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (4)
%w            Weekday as a decimal number [0(Saturday),6(Friday)].
%W            Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (4)
%x            Locale’s appropriate date representation.     
%X            Locale’s appropriate time representation.     
%y            Year without century as a decimal number [00,99].     
%Y            Year with century as a decimal number.     
%z            UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).    (5)
%Z            Time zone name (empty string if the object is naive).     
%%            A literal '%' character.
=========    =======
"""

        result = super(JalaliDatetime, self).strftime(format)

        result = replace_if_match(result, '%H', '%.2d' % self.hour)

        result = replace_if_match(result, '%I', '%.2d' % self.hour12())

        result = replace_if_match(result, '%M', '%.2d' % self.minute)

        result = replace_if_match(result, '%S', '%.2d' % self.second)

        result = replace_if_match(result, '%f', '%.6d' % self.microsecond)

        result = replace_if_match(result, '%c', self.localshortformat)
        result = replace_if_match(result, '%C', self.localformat)

        result = replace_if_match(result, '%p', self.ampm)

        result = replace_if_match(result, '%X', self.localtimeformat)

        result = replace_if_match(result, '%z', self.utcoffsetformat)

        result = replace_if_match(result, '%Z', self.tznameformat)

        return result

    def localshortformat(self):
        return self.strftime('%a %d %b %y %H:%M')

    def localformat(self):
        return self.strftime('%A %d %B %Y %I:%M:%S %p')

    def localtimeformat(self):
        return self.strftime('%I:%M:%S %p')

    def hour12(self):
        if self.hour > 12:
            return self.hour - 12
        return self.hour

    def ampm(self):
        if self.hour < 12:
            return AM_PM[0]
        return AM_PM[1]

    def utcoffsetformat(self):
        if self.tzinfo:
            td = self.utcoffset()
            _minutes = td.seconds / 60
            hours = _minutes / 60
            minutes = _minutes % 60
            return '%s%s' % (minutes, hours)
        return ''

    def tznameformat(self):
        return self.tzname() or ''

    def dayofyear(self):
        return (self.date() - JalaliDate(self.year, 1, 1)).days + 1


    def __repr__(self):
        return 'khayyam.JalaliDatetime(%s, %s, %s, %s, %s, %s, %s%s)' % \
               (self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond, \
                ', tzinfo=%s' % self.tzinfo if self.tzinfo else '')


    #################
    ### Operators ###
    #################

    def __add__(self, x):
        if isinstance(x, timedelta):
            return JalaliDatetime.from_datetime(self.to_datetime() + x)

        raise ValueError('JalaliDatetime object can added by timedelta or JalaliDate object')

    def __sub__(self, x):
        if isinstance(x, timedelta):
            return JalaliDatetime.from_datetime(self.to_datetime() - x)
        elif isinstance(x, JalaliDatetime):
            return self.to_datetime() - x.to_datetime()
        elif isinstance(x, JalaliDate):
            return self.to_datetime() - JalaliDatetime(x).to_datetime()

        raise ValueError('JalaliDatetime object can added by timedelta, JalaliDatetime or JalaliDate object')

    def __lt__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDate'
        return self.to_datetime() < x.to_datetime()

    def __le__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDatetime'
        return self.to_datetime() <= x.to_datetime()

    def __eq__(self, x):
        if not x:
            return False
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDatetime'
        return self.to_datetime() == x.to_datetime()

    def __ne__(self, x):
        if not x:
            return True
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDatetime'
        return self.to_datetime() != x.to_datetime()

    def __gt__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDatetime'
        return self.to_datetime() > x.to_datetime()

    def __ge__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDate'
        return self.to_datetime() >= x.to_datetime()

# # Class attributes
JalaliDatetime.min = JalaliDatetime(MINYEAR, 1, 1)
JalaliDatetime.max = JalaliDatetime(MAXYEAR, 12, 29, 23, 59, 59, 999999)
JalaliDatetime.resolution = timedelta(microseconds=1)

