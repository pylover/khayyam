# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta, time, datetime
from khayyam.algorithms_pure import gregorian_date_from_julian_day
import khayyam
from khayyam.formatting import JalaliDatetimeFormatter, AM_PM, AM_PM_ASCII
from khayyam.helpers import force_encoded_string_output
__author__ = 'vahid'


class JalaliDatetime(khayyam.JalaliDate):
    """
    Inherited from :py:class:`khayyam.JalaliDate`.

    Represent a moment in :doc:`/persiancalendar`.

    The first parameter can be an integer,
    :py:class:`datetime.date`, :py:class:`khayyam.JalaliDate`,
    :py:class:`datetime.datetime` or :py:class:`khayyam.JalaliDatetime`.

    You may create this object by passing `julian_day` parameter.


    :param year: jalali year
    :param month: 1-12
    :param day: 1-31
    :param hour: 0-23
    :param minute: 0-59
    :param second: 0-59
    :param microsecond: 0-999999
    :param tzinfo: Timezone info
    :param julian_day:

    :type year: :py:class:`int` | :py:class:`datetime.date` | :py:class:`khayyam.JalaliDate`
    :type month: int
    :type day: int
    :type hour: int
    :type minute: int
    :type second: int
    :type microsecond: int
    :type tzinfo: :py:class:`datetime.tzinfo`
    :type julian_day: int


    :return: An object representing a moment persian calendar.
    :rtype: :py:class:`khayyam.JalaliDatetime`

    """

    #: Represent the earlier moment which supported by this class.
    min = (khayyam.MINYEAR, 1, 1)

    #: Represent the last moment which supported by this class.
    max = (khayyam.MAXYEAR, 12, 29, 23, 59, 59, 999999)

    resolution = timedelta(microseconds=1)

    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0,
                 microsecond=0, tzinfo=None, julian_day=None):

        if isinstance(year, JalaliDatetime):
            year, month, day, hour, minute, second, microsecond = \
                year.year, year.month, year.day, year.hour, year.minute, year.second, year.microsecond
        elif isinstance(year, datetime):
            hour, minute, second, microsecond = year.hour, year.minute, year.second, year.microsecond
            if not tzinfo:
                tzinfo = year.tzinfo

        khayyam.JalaliDate.__init__(self, year, month, day, julian_day)
        self._time = time(hour, minute, second, microsecond, tzinfo)

    ##############
    # Properties #
    ##############

    @property
    def hour(self):
        """
        :getter: Returns the hour
        :setter: Sets the hour
        :type: int
        """
        return self._time.hour

    @hour.setter
    def hour(self, val):
        self._time.hour = val

    @property
    def minute(self):
        """
        :getter: Returns the minute
        :setter: Sets the minute
        :type: int
        """
        return self._time.minute

    @minute.setter
    def minute(self, val):
        self._time.minute = val

    @property
    def second(self):
        """
        :getter: Returns the second
        :setter: Sets the second
        :type: int
        """
        return self._time.second

    @second.setter
    def second(self, val):
        self._time.second = val

    @property
    def microsecond(self):
        """
        :getter: Returns the microsecond
        :setter: Sets the microsecond
        :type: int
        """
        return self._time.microsecond

    @microsecond.setter
    def microsecond(self, val):
        self._time.microsecond = val

    @property
    def tzinfo(self):
        """
        :getter: Returns the timezone info
        :setter: Sets(change) the timezone info
        :type: :py:class:`datetime.tzinfo`
        """
        return self._time.tzinfo

    @tzinfo.setter
    def tzinfo(self, val):
        self._time.tzinfo = val

    ##################
    # Static Methods #
    ##################

    @staticmethod
    def formatterfactory(fmt):
        return JalaliDatetimeFormatter(fmt)

    #################
    # Class Methods #
    #################

    @classmethod
    def now(cls, tz=None):
        """
        If optional argument tz is None or not specified, this is like today(), but,
        if possible, supplies more precision than can be gotten from going through a
        :py:func:`time.time()` timestamp (for example,
        this may be possible on platforms supplying the C gettimeofday() function).
        
        Else tz must be an instance of a :py:class:`datetime.tzinfo` subclass,
        and the current date and time are converted to tz's time zone.
        In this case the result is equivalent to `tz.fromutc(JalaliDatetime.utcnow().replace(tzinfo=tz))`.
        See also :py:meth:`khayyam.JalaliDate.today` and :py:meth:`khayyam.JalaliDatetime.utcnow`.

        :return: the current local date and time
        :rtype: :py:class:`khayyam.JalaliDatetime`
        """
        return cls(datetime.now(tz))

    @classmethod
    def utcnow(cls):
        """
        This is like :py:meth:`khayyam.JalaliDatetime.now`, but returns the current
        UTC date and time, as a naive datetime object.

        :return: The current UTC date and time, with tzinfo None.
        :rtype: :py:class:`khayyam.JalaliDatetime`
        """
        return cls(datetime.utcnow())

    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        """
        If optional argument tz is None or not specified, the timestamp is converted to
        the platform's local date and time, and the returned datetime object is naive.
        
        Else tz must be an instance of a class :py:class:`datetime.tzinfo` subclass,
        and the timestamp is converted to tz's time zone. In this case the result is
        equivalent to `tz.fromutc(JalaliDatetime.utcfromtimestamp(timestamp).replace(tzinfo=tz))`.
        
        This method may raise `ValueError`, if the timestamp is out of the range of values
        supported by the platform C localtime() or gmtime() functions.
        It's common for this to be restricted to years in 1970 through 2038.

        Note that on non-POSIX systems that include leap seconds in their
        notion of a timestamp, leap seconds are ignored by fromtimestamp(), and then
        it's possible to have two timestamps differing by a second that yield
        identical datetime objects. See also :py:class:`khayyam.JalaliDatetime.utcfromtimestamp`.

        :return: The local date and time corresponding to the POSIX timestamp,
                such as is returned by :py:func:`time.time()`.

        :rtype: :py:class:`khayyam.JalaliDatetime`
        """
        return cls(datetime.fromtimestamp(timestamp, tz=tz))

    @classmethod
    def utcfromtimestamp(cls, timestamp):
        """
        This may raise ValueError, if the timestamp is
        out of the range of values supported by the platform C gmtime()
        function. It's common for this to be restricted to years in 1970
        through 2038. See also :py:meth:`khayyam.JalaliDatetime.fromtimestamp`.

        :return: The UTC datetime corresponding to the POSIX timestamp,
                with tzinfo None.

        :rtype: :py:class:`khayyam.JalaliDatetime`
        """
        return cls(datetime.utcfromtimestamp(timestamp))

    @classmethod
    def fromordinal(cls, ordinal):
        """
        Return the jalali datetime corresponding to the proleptic Gregorian ordinal,
        where January 1 of year 1 has ordinal 1. ValueError is
        raised unless 1 <= ordinal <= datetime.max.toordinal(). The hour, minute, second
        and microsecond of the result are all 0, and tzinfo is None.
        """
        return cls(datetime.fromordinal(ordinal))

    @classmethod
    def combine(cls, date, _time):
        """
        Return a new jalali datetime object whose date members are equal to the given date object's, and whose _time and tzinfo members are equal to the given _time object's. For any datetime object d, d == datetime.combine(d.date(), d.timetz()). If date is a datetime object, its _time and tzinfo members are ignored.
        """
        if isinstance(date, (JalaliDatetime, khayyam.JalaliDate)):
            date = date.todatetime()
        return cls(datetime.combine(date, _time))

    @classmethod
    def strptime(cls, date_string, fmt):
        result = cls.formatterfactory(fmt).parse(date_string)
        result = {k: v for k, v in result.items() if k in (
            'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'tzinfo')}
        return cls(**result)

    ####################
    # Instance Methods #
    ####################

    def todatetime(self):
        arr = gregorian_date_from_julian_day(self.tojulianday())
        return datetime(int(arr[0]), int(arr[1]), int(arr[2]), self.hour, self.minute, self.second, self.microsecond,
                        self.tzinfo)

    def date(self):
        return khayyam.JalaliDate(self.year, self.month, self.day)

    def time(self):
        return time(self.hour, self.minute, self.second, self.microsecond)

    def timetz(self):
        return time(self.hour, self.minute, self.second, self.microsecond, self.tzinfo)

    def replace(self, year=None, month=None, day=None, hour=None,
                minute=None, second=None, microsecond=None, tzinfo=None):
        """
        Without adjusting the the and time based tzinfo
        """
        year, month, day = self._validate(
            year if year else self.year,
            month if month else self.month,
            day if day else self.day
        )

        result = JalaliDatetime(year,
                                month,
                                day,
                                self.hour if hour is None else hour,
                                self.minute if minute is None else minute,
                                self.second if second is None else second,
                                self.microsecond if microsecond is None else microsecond,
                                self.tzinfo if tzinfo is None else tzinfo)
        return result

    def astimezone(self, tz):
        if self.tzinfo is tz:
            return self
        if self.tzinfo:
            utc = self - self.utcoffset()
        else:
            utc = self
        return tz.fromutc(utc.replace(tzinfo=tz))

    def utcoffset(self):
        if self.tzinfo:
            return self.tzinfo.utcoffset(self)
        else:
            return None

    def dst(self):
        """
        If tzinfo is None, returns None, else returns self.tzinfo.dst(self), and raises an exception if the latter doesn’t return None, or a timedelta object representing a whole number of minutes with magnitude less than one day.
        """
        if self.tzinfo:
            return self.tzinfo.dst(self)
        else:
            return None

    def tzname(self):
        if self.tzinfo:
            return self.tzinfo.tzname(self)
        else:
            return None

    def isoformat(self, sep='T'):
        """
        Return a string representing the date and time in ISO 8601 format, YYYY-MM-DDTHH:MM:SS.mmmmmm or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS

        If utcoffset() does not return None, a 6-character string is appended, giving the UTC offset in (signed) hours and minutes: YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM or, if microsecond is 0 YYYY-MM-DDTHH:MM:SS+HH:MM
        """
        return self.strftime('%Y-%m-%d' + sep + '%H:%M:%S.%f%z')

    def localshortformat(self):
        return self.strftime('%a %d %b %y %H:%M')

    def localshortformatascii(self):
        return self.strftime('%e %d %g %y %H:%M')

    def localdatetimeformat(self):
        return self.strftime('%A %d %B %Y %I:%M:%S %p')

    def localdatetimeformatascii(self):
        return self.strftime('%E %d %G %Y %I:%M:%S %t')

    def localtimeformat(self):
        return self.strftime('%I:%M:%S %p')

    def hour12(self):
        res = self.hour
        if res > 12:
            res -= 12
        elif res == 0:
            res = 12
        return res

    def ampm(self):
        if self.hour < 12:
            return AM_PM[0]
        return AM_PM[1]

    def ampmascii(self):
        if self.hour < 12:
            return AM_PM_ASCII[0]
        return AM_PM_ASCII[1]

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
        return (self.date() - khayyam.JalaliDate(self.year, 1, 1)).days + 1

    ###################
    # Special Members #
    ###################

    def __unicode__(self):
        return 'khayyam.JalaliDatetime(%s, %s, %s, %s, %s, %s, %s%s, %s)' % (
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.microsecond,
            ', tzinfo=%s' % self.tzinfo.__unicode__() if self.tzinfo else '',
            self.weekdaynameascii()
        )


    __repr__ = force_encoded_string_output(__unicode__)

    def __str__(self):
        return self.isoformat(sep=' ')

    def __add__(self, x):
        if isinstance(x, timedelta):
            return JalaliDatetime(x + self.todatetime())

        raise ValueError('JalaliDatetime object can added by timedelta or JalaliDate object')

    def __sub__(self, x):
        if isinstance(x, timedelta):
            return JalaliDatetime(self.todatetime() - x)
        elif isinstance(x, JalaliDatetime):
            return self.todatetime() - x.todatetime()
        elif isinstance(x, khayyam.JalaliDate):
            return self.todatetime() - JalaliDatetime(x).todatetime()

        raise ValueError('JalaliDatetime object can added by timedelta, JalaliDatetime or JalaliDate object')

    def __lt__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDate'
        return self.todatetime() < x.todatetime()

    def __le__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDatetime'
        return self.todatetime() <= x.todatetime()

    def __hash__(self):
        return super(JalaliDatetime, self).__hash__() ^ \
            hash(self.hour) ^ \
            hash(self.minute) ^ \
            hash(self.second) ^ \
            hash(self.microsecond) ^ \
            hash(self.tzinfo)

    def __eq__(self, x):
        if not x:
            return False
        if isinstance(x, datetime):
            return self.todatetime().__eq__(x)
        elif isinstance(x, JalaliDatetime):
            return hash(self) == hash(x)
        else:
            raise ValueError('Comparison only allowed with JalaliDatetime and datetime.datetime objects.')

    def __gt__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDatetime'
        return self.todatetime() > x.todatetime()

    def __ge__(self, x):
        assert isinstance(x, JalaliDatetime), 'Comparison just allow with JalaliDate'
        return self.todatetime() >= x.todatetime()


# # Class attributes
JalaliDatetime.min = JalaliDatetime(*JalaliDatetime.min)
JalaliDatetime.max = JalaliDatetime(*JalaliDatetime.max)
