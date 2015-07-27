# -*- coding: utf-8 -*-
from khayyam import SATURDAY, MONDAY
from khayyam.compat import get_unicode
from khayyam.formatting import constants as consts
from .directive import Directive, CompositeDateDirective, CompositeDatetimeDirective
from .day import \
    PersianDayDirective, \
    DayOfYearDirective, \
    PersianDayOfYearDirective
from .month import PersianMonthDirective
from .ampm import AmPmDirective, AmPmASCIIDirective
from .time import \
    PersianMicrosecondDirective, \
    PersianHour12Directive, \
    PersianHour24Directive, \
    PersianSecondDirective, \
    PersianMinuteDirective
from .year import \
    ShortYearDirective, \
    PersianYearDirective, \
    PersianShortYearDirective
from .tz import UTCOffsetDirective, TimezoneNameDirective, PersianUTCOffsetDirective

__author__ = 'vahid'

DATE_FORMAT_DIRECTIVES = [

    # YEAR
    Directive('Y', 'year', consts.YEAR_REGEX, int, lambda d: '%.4d' % d.year),
    ShortYearDirective('y', 'shortyear', consts.SHORT_YEAR_REGEX, int),
    PersianYearDirective('N', 'persianyear', consts.PERSIAN_YEAR_REGEX),
    PersianYearDirective('O', 'persianyearzeropadded', consts.PERSIAN_YEAR_ZERO_PADDED_REGEX,
                         zero_padding=True, zero_padding_length=4),
    PersianShortYearDirective('n', 'persianshortyear', consts.PERSIAN_SHORT_YEAR_REGEX, ),
    PersianShortYearDirective('u', 'persianshortyearzeropadded', consts.PERSIAN_SHORT_YEAR_ZERO_PADDED_REGEX,
                              zero_padding=True),

    # MONTH
    PersianMonthDirective('R', 'persianmonth', consts.PERSIAN_MONTH_REGEX),
    PersianMonthDirective('P', 'persianmonthzeropadded', consts.PERSIAN_MONTH_ZERO_PADDED_REGEX, zero_padding=True),
    Directive('m', 'month', consts.MONTH_REGEX, int, lambda d: '%.2d' % d.month),
    Directive('b', 'monthabbr', consts.PERSIAN_MONTH_ABBRS_REGEX, get_unicode, lambda d: d.monthabbr(),
              lambda ctx, f: ctx.update(
                  {'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == ctx['monthabbr']][0][0]})),
    Directive('B', 'monthname', consts.PERSIAN_MONTH_NAMES_REGEX, get_unicode, lambda d: d.monthname(),
              lambda ctx, f: ctx.update(
                  {'month': [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES.items() if v == ctx['monthname']][0][0]})),
    Directive('g', 'monthabbr_ascii', consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX, get_unicode,
              lambda d: d.monthabbr_ascii(),
              lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS_ASCII.items() if
                                                   v == ctx['monthabbr_ascii']][0][0]})),
    Directive('G', 'monthnameascii', consts.PERSIAN_MONTH_NAMES_ASCII_REGEX, get_unicode,
              lambda d: d.monthnameascii(),
              lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES_ASCII.items() if
                                                   v == ctx['monthnameascii']][0][0]})),

    # DAY
    Directive('d', 'day', consts.DAY_REGEX, int, lambda d: '%.2d' % d.day),
    PersianDayDirective('D', 'persianday', consts.PERSIAN_DAY_REGEX),
    PersianDayDirective('K', 'persiandayzeropadded', consts.PERSIAN_DAY_ZERO_PADDED_REGEX, zero_padding=True),
    DayOfYearDirective('j', 'dayofyear', consts.DAY_OF_YEAR_REGEX, int),
    PersianDayOfYearDirective('J', 'persiandayofyear', consts.PERSIAN_DAY_OF_YEAR_REGEX),
    PersianDayOfYearDirective('V', 'persiandayofyearzeropadded', consts.PERSIAN_DAY_OF_YEAR_ZERO_PADDED_REGEX,
                              zero_padding=True, zero_padding_length=3),

    # WEEK
    Directive('w', 'weekday', consts.WEEKDAY_REGEX, int, lambda d: '%d' % d.weekday()),
    Directive('W', 'weekofyear', consts.WEEK_OF_YEAR_REGEX, int, lambda d: '%.2d' % d.weekofyear(SATURDAY)),
    Directive('U', 'weekofyear', consts.WEEK_OF_YEAR_REGEX, int, lambda d: '%.2d' % d.weekofyear(MONDAY)),
    Directive('a', 'weekdayabbr', consts.PERSIAN_WEEKDAY_ABBRS_REGEX, get_unicode, lambda d: d.weekdayabbr()),
    Directive('A', 'weekdayname', consts.PERSIAN_WEEKDAY_NAMES_REGEX, get_unicode, lambda d: d.weekdayname()),
    Directive('e', 'weekdayabbrascii', consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX, get_unicode,
              lambda d: d.weekdayabbrascii()),
    Directive('E', 'weekdaynameascii', consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX, get_unicode,
              lambda d: d.weekdaynameascii()),

    # COMPOSITE
    CompositeDateDirective('x', 'localdateformat', '%s %s %s %s' % (
        consts.PERSIAN_WEEKDAY_NAMES_REGEX,
        consts.PERSIAN_DAY_REGEX,
        consts.PERSIAN_MONTH_NAMES_REGEX,
        consts.PERSIAN_YEAR_REGEX
    ), "%A %D %B %N"),

    # MISCELLANEOUS
    Directive('%', 'percent', '%', None, lambda d: '%', ),
]

TIME_FORMAT_DIRECTIVES = [

    # HOUR
    Directive('H', 'hour', consts.HOUR24_REGEX, int, lambda d: '%.2d' % d.hour),
    PersianHour24Directive('k', 'persianhour24', consts.PERSIAN_HOUR24_REGEX),
    PersianHour24Directive('h', 'persianhour24zeropadded', consts.PERSIAN_HOUR24_ZERO_PADDED_REGEX, zero_padding=True),
    Directive('I', 'hour12', consts.HOUR12_REGEX, int, lambda d: '%.2d' % d.hour12()),
    PersianHour12Directive('l', 'persianhour12', consts.PERSIAN_HOUR12_REGEX),
    PersianHour12Directive('i', 'persianhour12zeropadded', consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX, zero_padding=True),

    # MINUTE
    Directive('M', 'minute', consts.MINUTE_REGEX, int, lambda d: '%.2d' % d.minute),
    PersianMinuteDirective('v', 'persianminute', consts.PERSIAN_MINUTE_REGEX),
    PersianMinuteDirective('r', 'persianminutezeropadded', consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX, zero_padding=True),

    # SECOND
    Directive('S', 'second', consts.SECOND_REGEX, int, lambda d: '%.2d' % d.second),
    PersianSecondDirective('L', 'persiansecond', consts.PERSIAN_SECOND_REGEX),
    PersianSecondDirective('s', 'persiansecondzeropadded', consts.PERSIAN_SECOND_ZERO_PADDED_REGEX, zero_padding=True),

    # MICROSECOND
    Directive('f', 'microsecond', consts.MICROSECOND_REGEX, int, lambda d: '%.6d' % d.microsecond),
    PersianMicrosecondDirective('F', 'persianmicrosecond', consts.PERSIAN_MICROSECOND_REGEX),

    # AMP-PM
    AmPmDirective('p', 'ampm', consts.AM_PM_REGEX),
    AmPmASCIIDirective('t', 'ampmascii', consts.AM_PM_ASCII_REGEX),

    # TIMEZONE
    UTCOffsetDirective('z', 'utcoffset', consts.UTC_OFFSET_FORMAT_REGEX, get_unicode),
    TimezoneNameDirective('Z', 'tzname', consts.TZ_NAME_FORMAT_REGEX, get_unicode),
    PersianUTCOffsetDirective('o', 'persianutcoffset', consts.PERSIAN_UTC_OFFSET_FORMAT_REGEX),

    # COMPOSITE
    CompositeDatetimeDirective('c', 'localshortdatetimeformat', '%s %s %s %s %s:%s' % (
        consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
        consts.PERSIAN_DAY_REGEX,
        consts.PERSIAN_MONTH_ABBRS_REGEX,
        consts.PERSIAN_SHORT_YEAR_REGEX,
        consts.PERSIAN_HOUR24_REGEX,
        consts.PERSIAN_MINUTE_REGEX
    ), "%a %D %b %n %k:%v"),
    CompositeDatetimeDirective('C', 'localdatetimeformat', '%s %s %s %s %s:%s:%s %s' % (
        consts.PERSIAN_WEEKDAY_NAMES_REGEX,
        consts.PERSIAN_DAY_REGEX,
        consts.PERSIAN_MONTH_NAMES_REGEX,
        consts.PERSIAN_YEAR_REGEX,
        consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX,
        consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX,
        consts.PERSIAN_SECOND_ZERO_PADDED_REGEX,
        consts.AM_PM_REGEX
    ), "%A %D %B %N %i:%r:%s %p"),
    CompositeDatetimeDirective('q', 'localshortdatetimeformatascii', '%s %s %s %s %s:%s' % (
        consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
        consts.DAY_REGEX,
        consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
        consts.SHORT_YEAR_REGEX,
        consts.HOUR24_REGEX,
        consts.MINUTE_REGEX
    ), "%e %d %g %y %H:%M"),
    CompositeDatetimeDirective('Q', 'localdatetimeformatascii', '%s %s %s %s %s:%s:%s %s' % (
        consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
        consts.DAY_REGEX,
        consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
        consts.YEAR_REGEX,
        consts.HOUR12_REGEX,
        consts.MINUTE_REGEX,
        consts.SECOND_REGEX,
        consts.AM_PM_ASCII_REGEX
    ), "%E %d %G %Y %I:%M:%S %t"),
    CompositeDatetimeDirective('X', 'localtimeformat', '%s:%s:%s %s' % (
        consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX,
        consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX,
        consts.PERSIAN_SECOND_ZERO_PADDED_REGEX,
        consts.AM_PM_REGEX
    ), "%i:%r:%s %p"),

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
]

"""
Available directives: T
"""
