# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import time
from khayyam.helpers import force_encoded_string_output
from khayyam.algorithms_pure import days_in_month, \
    is_leap_year, \
    get_julian_day_from_gregorian, \
    jalali_date_from_julian_day, \
    julian_day_from_jalali_date, \
    gregorian_date_from_julian_day
from khayyam import MAXYEAR, MINYEAR, SATURDAY
from khayyam.formatting import \
    JalaliDateFormatter, \
    PERSIAN_MONTH_ABBRS, \
    PERSIAN_MONTH_NAMES, \
    PERSIAN_WEEKDAY_ABBRS, \
    PERSIAN_WEEKDAY_NAMES, \
    PERSIAN_MONTH_ABBRS_ASCII, \
    PERSIAN_MONTH_NAMES_ASCII, \
    PERSIAN_WEEKDAY_ABBRS_ASCII, \
    PERSIAN_WEEKDAY_NAMES_ASCII

__author__ = 'vahid'


class JalaliDate(object):
    """
    Represent a day in :doc:`/persiancalendar`.

    The first parameter can be an integer, :py:class:`datetime.date` or :py:class:`khayyam.JalaliDate`.

    You may create this object by passing `julian_day` parameter.


    .. doctest::

        >>> from khayyam import JalaliDate
        >>> JalaliDate(julian_day=2445218)
        khayyam.JalaliDate(1361, 6, 15, Doshanbeh)

        >>> from datetime import date
        >>> JalaliDate(date(1982, 9, 6))
        khayyam.JalaliDate(1361, 6, 15, Doshanbeh)

        >>> JalaliDate(1361, 6, 15)
        khayyam.JalaliDate(1361, 6, 15, Doshanbeh)


    :param year: jalali year
    :param month: month 1-12
    :param day: day of month
    :param julian_day: julian day

    :type year: :py:class:`int` | :py:class:`datetime.date` | :py:class:`khayyam.JalaliDate`
    :type month: int
    :type day: int
    :type julian_day: int

    :return: A :py:class:`khayyam.JalaliDate` instance.
    :rtype: :py:class:`khayyam.JalaliDate`
    """

    #: Represent the minimum year which supported by this class.
    min = (MINYEAR, 1, 1)   # To be converted to JalaliDate at the bottom of this module

    #: Represent the maximum year which supported by this class.
    max = (MAXYEAR, 12, 29)

    resolution = datetime.timedelta(days=1)

    def __init__(self, year=1, month=1, day=1, julian_day=None):
        if isinstance(year, JalaliDate):
            jd = year
            year = jd.year
            month = jd.month
            day = jd.day
        elif isinstance(year, datetime.date):
            julian_day = get_julian_day_from_gregorian(year.year, year.month, year.day)

        if julian_day is not None:
            year, month, day = jalali_date_from_julian_day(julian_day)

        self.year, self.month, self.day = self._validate(year, month, day)

    @property
    def isleap(self):
        """
        `True` if the current instance is in a leap year.

        :type: bool
        """
        return is_leap_year(self.year)

    @property
    def daysinmonth(self):
        """
        Total days in the current month.

        :type: int
        """
        return days_in_month(self.year, self.month)

    @staticmethod
    def formatterfactory(fmt):
        """
        By default it will be return a :py:class:`khayyam.formatting.JalaliDateFormatter`
        instance based on given format string.

        :param fmt: see: :doc:`/directives`
        :type fmt: str
        :return: Formatter object, based on the given format string.
        :rtype: khayyam.formatting.BaseFormatter
        """
        return JalaliDateFormatter(fmt)

    @classmethod
    def today(cls):
        """
        :return: The current local date.
        :rtype: :py:class:`khayyam.JalaiDate`
        """
        return cls(datetime.date.today())

    @classmethod
    def fromtimestamp(cls, timestamp):
        """
        Such as is returned by :func:`time.time()`. This may raise :class:`ValueError`,
        if the timestamp is out of the range of values supported by the platform C localtime()
        function. It’s common for this to be restricted to years from 1970 through 2038.
        Note that on non-POSIX systems that include leap seconds in their notion of a
        timestamp, leap seconds are ignored by fromtimestamp().

        :return: Local date corresponding to the POSIX timestamp
        :rtype: :py:class:`khayyam.JalaiDate`

        """
        return cls(datetime.date.fromtimestamp(timestamp))

    @classmethod
    def fromordinal(cls, ordinal):
        """
        Where Farvardin 1 of year 1 has ordinal 1.

        ValueError is raised unless 1 <= ordinal <= `khayyam.jalaliDate(khayyam.MAXYEAR).toordinal()`.

        :return: The date corresponding to the proleptic Shamsi ordinal.
        :rtype: :py:class:`khayyam.JalaiDate`
        """
        return cls.min + datetime.timedelta(days=ordinal-1)

    @classmethod
    def strptime(cls, date_string, format):
        """
        This is opposite of the :py:meth:`khayyam.JalaliDate.strftime`,
        and used to parse date strings into date object.

        `ValueError` is raised if the date_string and format can’t be
        parsed by time.strptime() or if it returns a value which isn’t a time tuple. For a
        complete list of formatting directives, see :doc:`/directives`.


        :param date_string:
        :param format:
        :return: A :py:class:`khayyam.JalaliDate` corresponding to date_string, parsed according to format
        :rtype: :py:class:`khayyam.JalaiDate`
        """
        result = cls.formatterfactory(format).parse(date_string)
        result = {k:v for k, v in result.items() if k in ('year', 'month', 'day')}
        return cls(**result)

    @staticmethod
    def _validate(year, month, day):
        year = year if isinstance(year, int) else int(year)
        month = month if isinstance(month, int) else int(month)
        day = day if isinstance(day, int) else int(day)

        if year < MINYEAR or year > MAXYEAR:
            raise ValueError('Year must be between %s and %s, but it is: %s' % (MINYEAR, MAXYEAR, year))
        if month < 1 or month > 12:
            raise ValueError('Month must be between 1 and 12, but it is: %s' % month)
        _days_in_month = days_in_month(year, month)
        if day < 1 or day > _days_in_month:
            raise ValueError('Day must be between 1 and %s, but it is: %s' % (_days_in_month, day))
        return year, month, day

    def tojulianday(self):
        """
        :return: Julian day representing the current instance.
        :rtype: int
        """
        return julian_day_from_jalali_date(self.year, self.month, self.day)

    def copy(self):
        """
        It's equivalent to:

            >>> source_date = JalaliDate(1394, 3, 24)
            >>> JalaliDate(source_date.year, source_date.month, source_date.day)
            khayyam.JalaliDate(1394, 3, 24, Yekshanbeh)

        :return: A Copy of the current instance.
        :rtype: :py:class:`khayyam.JalaiDate`
        """
        return JalaliDate(self.year, self.month, self.day)

    def replace(self, year=None, month=None, day=None):
        """
        Replaces the given arguments on this instance, and return a new instance.

        :param year:
        :param month:
        :param day:
        :return: A :py:class:`khayyam.JalaliDate` with the same attributes, except for those
            attributes given new values by which keyword arguments are specified.
        """

        return JalaliDate(
            year if year else self.year,
            month if month else self.month,
            day if day else self.day
        )

    def todate(self):
        """
        Calculates the corresponding day in the gregorian calendar. this is the main use case of this library.

        :return: Corresponding date in gregorian calendar.
        :rtype: :py:class:`datetime.date`
        """
        arr = gregorian_date_from_julian_day(self.tojulianday())
        return datetime.date(int(arr[0]), int(arr[1]), int(arr[2]))

    def toordinal(self):
        """
        It's equivalent to:
        .. testsetup:: api-toordinal

            import khayyam
            from khayyam import JalaliDate

        .. doctestLL api-toordinal

            >>> d = JalaliDate(1361, 6, 15)
            >>> (d - JalaliDate(khayyam.MINYEAR)).days + 1

        :return: The corresponding proleptic Shamsi ordinal days.
        :rtype: int
        """
        return (self - self.min).days + 1

    def timetuple(self):
        """
        It's equivalent to:

            >>> time.struct_time((d.year, d.month, d.day, d.hour, d.minute, d.second, d.weekday(), dayofyear, [-1|1|0])) # doctest: +SKIP
            time.struct_time(tm_year=2015, tm_mon=7, tm_mday=28, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=209, tm_isdst=-1)


        The tm_isdst flag of the result is set according to the dst() method: `tzinfo`
        is None or dst() returns None, tm_isdst is set to -1; else if dst()
        returns a non-zero value, tm_isdst is set to 1; else tm_isdst is set to 0.


        :return: A :py:class:`time.struct_time` such as returned by time.localtime().
        :rtype: :py:class:`time.struct_time`
        """
        return time.struct_time((
            self.year,
            self.month,
            self.day,
            0,
            0,
            0,
            self.weekday(),
            self.dayofyear(),
            -1
        ))

    def weekday(self):
        """
        :rtype: int
        :return: The day of the week as an integer, where Saturday is 0 and Friday is 6.
        """
        return (self.todate().weekday() + 2) % 7

    def isoweekday(self):
        """
        :rtype: int
        :return: The day of the week as an integer, where Saturday is 1 and Friday is 7.
        """
        return self.weekday() + 1

    def isocalendar(self):
        """
        :rtype: tuple
        :return: Return a 3-tuple, (year, week number, isoweekday).
        """
        return self.year, self.weekofyear(SATURDAY), self.isoweekday()

    def isoformat(self):
        """
        :rtype: str
        :return: A string representing the date in ISO 8601 format, ‘YYYY-MM-DD’.
        For example:

            >>> JalaliDate(1361, 12, 4).isoformat() == '1361-12-04'
            True

        """
        return self.strftime('%Y-%m-%d')

    def strftime(self, format_string):
        """
        Format codes referring to hours, minutes or seconds will see 0 values.
        For a complete list of formatting directives, see :doc:`/directives`.

        :param format_string: The format string.
        :return: A string representing the date, controlled by an explicit format string
        :rtype: unicode
        """
        return self.formatterfactory(format_string).format(self)

    def weekdayname(self):
        """
        :return: The corresponding persian weekday name: [شنبه - جمعه]
        :rtype: unicode
        """
        return PERSIAN_WEEKDAY_NAMES[self.weekday()]

    def weekdayabbr(self):
        """
        :return: The corresponding persian weekday abbreviation: [ش ی د س چ پ ج]
        :rtype: unicode
        """
        return PERSIAN_WEEKDAY_ABBRS[self.weekday()]

    def weekdaynameascii(self):
        """
        :rtype: unicode
        :return: The corresponding persian weekday name in ASCII:
                [Shanbeh - Jomeh]
        """
        return PERSIAN_WEEKDAY_NAMES_ASCII[self.weekday()]

    def weekdayabbrascii(self):
        """
        :return: The corresponding persian weekday abbreviation in ASCII:
            [Sh, Y, D, Se, Ch, P, J]
        :rtype: unicode
        """
        return PERSIAN_WEEKDAY_ABBRS_ASCII[self.weekday()]

    def monthname(self):
        """
        :rtype: unicode
        :return: The corresponding persian month name: [فروردین - اسفند]
        """
        return PERSIAN_MONTH_NAMES[self.month]

    def monthabbr(self):
        """
        :rtype: unicode
        :return: The corresponding persian month abbreviation:
                [فر, ار, خر, تی, مر, شه, مه, آب, آذ, دی, به, اس]
        """
        return PERSIAN_MONTH_ABBRS[self.month]

    def monthabbr_ascii(self):
        """
        :rtype: unicode
        :return: The corresponding persian month abbreviation in ASCII: [F, O , Kh ... E].
        """
        return PERSIAN_MONTH_ABBRS_ASCII[self.month]

    def monthnameascii(self):
        """
        :rtype: unicode
        :return: The corresponding persian month name in ASCII:
            [Farvardin - Esfand]
        """
        return PERSIAN_MONTH_NAMES_ASCII[self.month]

    def localdateformat(self):
        """
        It's equivalent to:

        .. testsetup:: api-localdateformat

            from __future__ import print_function
            from khayyam import JalaliDate

        .. doctest:: api-localdateformat

            >>> print(JalaliDate(1361, 6, 15).strftime('%A %D %B %N'))
            دوشنبه ۱۵ شهریور ۱۳۶۱

        For example:

        .. doctest:: api-localdateformat

            >>> print(JalaliDate(1394, 5, 6).localdateformat())
            سه شنبه ۶ مرداد ۱۳۹۴


        :return: Appropriate localized string representing a persian day
        :rtype: unicode
        """
        return self.strftime('%A %D %B %N')

    def firstdayofyear(self):
        """
        As it's name says: it's referring to a :py:class:`JalaliDate`
        representing the first day of current instance's year.

        :return: First day of corresponding year.
        :rtype: :py:class:`JalaliDate`
        """
        return JalaliDate(self.year, 1, 1)

    def dayofyear(self):
        """
        :return: Day of year az integer: 1-35[5,6]
        :rtype: int
        """
        return (self - self.firstdayofyear()).days + 1

    def weekofyear(self, first_day_of_week=SATURDAY):
        """weekofyear(first_day_of_week=SATURDAY)

        :param first_day_of_week: One of the
                :py:data:`khayyam.SATURDAY`,
                :py:data:`khayyam.SUNDAY`,
                :py:data:`khayyam.MONDAY`,
                :py:data:`khayyam.TUESDAY`,
                :py:data:`khayyam.WEDNESDAY`,
                :py:data:`khayyam.THURSDAY` or
                :py:data:`khayyam.FRIDAY`
        :return: The week number of the year.
        :rtype: int
        """
        first_day_of_year = self.firstdayofyear()
        days = (self - first_day_of_year).days
        offset = first_day_of_week - first_day_of_year.weekday()
        if offset < 0:
            offset += 7

        if days < offset:
            return 0

        return int((days - offset) / 7 + 1)

    ###################
    # Special Members #
    ###################

    __format__ = strftime

    def __str__(self):
        return self.isoformat()

    @force_encoded_string_output
    def __repr__(self):
        return 'khayyam.JalaliDate(%s, %s, %s, %s)' % \
               (self.year, self.month, self.day, self.weekdaynameascii())

    def __add__(self, x):
        if isinstance(x, datetime.timedelta):
            days = self.tojulianday() + x.days
            return JalaliDate(julian_day=days)

        raise ValueError('JalaliDate object can added by timedelta or JalaliDate object')

    def __sub__(self, x):
        if isinstance(x, datetime.timedelta):
            days = self.tojulianday() - x.days
            return JalaliDate(julian_day=days)
        elif isinstance(x, JalaliDate):
            days = self.tojulianday() - x.tojulianday()
            return datetime.timedelta(days=days)

        raise ValueError('JalaliDate object can added by timedelta or JalaliDate object')

    def __lt__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.tojulianday() < x.tojulianday()

    def __le__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.tojulianday() <= x.tojulianday()

    def __hash__(self):
        return hash(self.year) ^ hash(self.month) ^ hash(self.day)

    def __eq__(self, x):
        if not x:
            return False
        if isinstance(x, datetime.date):
            return self.todate().__eq__(x)
        elif isinstance(x, JalaliDate):
            return hash(self) == hash(x)
        else:
            raise ValueError('Comparison only allowed with JalaliDate and datetime.date objects.')

    def __ne__(self, x):
        return not self.__eq__(x)

    def __gt__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.tojulianday() > x.tojulianday()

    def __ge__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.tojulianday() >= x.tojulianday()


# Class attributes
JalaliDate.min = JalaliDate(*JalaliDate.min)
JalaliDate.max = JalaliDate(*JalaliDate.max)

