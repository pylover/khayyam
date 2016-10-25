# -*- coding: utf-8 -*-
from khayyam.formatting import constants as consts

from .timedelta import TotalHoursDirective, TotalMinutesDirective, PersianTotalHoursDirective, \
    PersianHoursDirective


TIME_FORMAT_DIRECTIVES = [

    # # HOUR
    # Directive('H', 'hour', consts.HOUR24_REGEX, int, lambda d: '%.2d' % d.hour),
    # PersianHour24Directive('k', 'persianhour24', consts.PERSIAN_HOUR24_REGEX),
    # PersianHour24Directive('h', 'persianhour24zeropadded', consts.PERSIAN_HOUR24_ZERO_PADDED_REGEX, zero_padding=True),
    # Directive('I', 'hour12', consts.HOUR12_REGEX, int, lambda d: '%.2d' % d.hour12()),
    # PersianHour12Directive('l', 'persianhour12', consts.PERSIAN_HOUR12_REGEX),
    # PersianHour12Directive('i', 'persianhour12zeropadded', consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX, zero_padding=True),

    # # MINUTE
    # Directive('M', 'minute', consts.MINUTE_REGEX, int, lambda d: '%.2d' % d.minute),
    # PersianMinuteDirective('v', 'persianminute', consts.PERSIAN_MINUTE_REGEX),
    # PersianMinuteDirective('r', 'persianminutezeropadded', consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX, zero_padding=True),

    # # SECOND
    # Directive('S', 'second', consts.SECOND_REGEX, int, lambda d: '%.2d' % d.second),
    # PersianSecondDirective('L', 'persiansecond', consts.PERSIAN_SECOND_REGEX),
    # PersianSecondDirective('s', 'persiansecondzeropadded', consts.PERSIAN_SECOND_ZERO_PADDED_REGEX, zero_padding=True),

    # # MICROSECOND
    # Directive('f', 'microsecond', consts.MICROSECOND_REGEX, int, lambda d: '%.6d' % d.microsecond),
    # PersianMicrosecondDirective('F', 'persianmicrosecond', consts.PERSIAN_MICROSECOND_REGEX),

    # # AMP-PM
    # AmPmDirective('p', 'ampm', consts.AM_PM_REGEX),
    # AmPmASCIIDirective('t', 'ampmascii', consts.AM_PM_ASCII_REGEX),

    # # TIMEZONE
    # UTCOffsetDirective('z', 'utcoffset', consts.UTC_OFFSET_FORMAT_REGEX, get_unicode),
    # TimezoneNameDirective('Z', 'tzname', consts.TZ_NAME_FORMAT_REGEX, get_unicode),
    # PersianUTCOffsetDirective('o', 'persianutcoffset', consts.PERSIAN_UTC_OFFSET_FORMAT_REGEX),


]


TIMEDELTA_FORMAT_DIRECTIVES = [
    TotalHoursDirective('H', 'totalhours'),
    PersianTotalHoursDirective('k', 'persiantotalhours'),
    Directive('I', 'hours', consts.HOUR24_REGEX, int, lambda t: '%.2d' % t.hours),
    PersianHoursDirective('h', 'persianhours'),

    TotalMinutesDirective('M', 'totalminutes', consts.UNLIMITED_INT_REGEX, int, lambda t: '%d' % t.total_minutes),
    Directive('m', 'minutes', consts.MINUTE_REGEX, int, lambda t: '%.2d' % t.minutes),

]


DATETIME_FORMAT_DIRECTIVES = DATE_FORMAT_DIRECTIVES + TIME_FORMAT_DIRECTIVES

__all__ = [
    'Directive',
    'PersianDayDirective',
    'DayOfYearDirective',
    'PersianDayOfYearDirective',
    'PersianMonthDirective',
    'AmPmDirective',
    'AmPmASCIIDirective',
    'PersianMicrosecondDirective',
    'PersianHour12Directive',
    'PersianHour24Directive',
    'PersianSecondDirective',
    'PersianMinuteDirective',
    'ShortYearDirective',
    'PersianYearDirective',
    'PersianShortYearDirective',
    'UTCOffsetDirective',
    'TimezoneNameDirective',
    'PersianUTCOffsetDirective',
    'DATE_FORMAT_DIRECTIVES',
    'TIME_FORMAT_DIRECTIVES',
    'DATETIME_FORMAT_DIRECTIVES',
    'TIMEDELTA_FORMAT_DIRECTIVES',
    'TotalHoursDirective',
    'PersianTotalHoursDirective',
    'PersianHoursDirective',
    'TotalMinutesDirective'
]

"""
Available directives: T
"""
