# -*- coding: utf-8 -*-
from khayyam import SATURDAY, MONDAY
from khayyam.compat import get_unicode
from khayyam.formatting import constants as consts
from .directive import Directive
from .day import PersianDayDirective
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
    DayOfYearDirective, \
    PersianDayOfYearDirective, \
    PersianYearDirective, \
    PersianShortYearDirective
from .local import \
    LocalShortDatetimeFormatDirective, \
    LocalDatetimeFormatDirective, \
    LocalASCIIShortDatetimeFormatDirective, \
    LocalASCIIDatetimeFormatDirective, \
    LocalDateFormatDirective, \
    LocalTimeFormatDirective
from .tz import UTCOffsetDirective, TimezoneNameDirective, PersianUTCOffsetDirective
__author__ = 'vahid'


DATE_FORMAT_DIRECTIVES = [
    ShortYearDirective(),
    DayOfYearDirective(),
    LocalDateFormatDirective(),
    PersianDayDirective(),
    PersianDayOfYearDirective(),
    PersianMonthDirective(),
    PersianYearDirective(),
    PersianShortYearDirective(),
    PersianSecondDirective(),
    PersianMinuteDirective(),
    PersianUTCOffsetDirective(),
    Directive(
        'Y',
        'year',
        consts.YEAR_REGEX,
        int,
        lambda d: '%.4d' % d.year,
    ),
    Directive(
        'm',
        'month',
        consts.MONTH_REGEX,
        int,
        lambda d: '%.2d' % d.month,
    ),
    Directive(
        'b',
        'monthabbr',
        consts.PERSIAN_MONTH_ABBRS_REGEX,
        get_unicode,
        lambda d: d.monthabbr(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == ctx['monthabbr']][0][0]})
    ),
    Directive(
        'B',
        'monthname',
        consts.PERSIAN_MONTH_NAMES_REGEX,
        get_unicode,
        lambda d: d.monthname(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES.items() if v == ctx['monthname']][0][0]})
    ),
    Directive(
        'g',
        'monthabbr_ascii',
        consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
        get_unicode,
        lambda d: d.monthabbr_ascii(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS_ASCII.items() if v == ctx['monthabbr_ascii']][0][0]})
    ),
    Directive(
        'G',
        'monthname_ascii',
        consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
        get_unicode,
        lambda d: d.monthname_ascii(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES_ASCII.items() if v == ctx['monthname_ascii']][0][0]})
    ),
    Directive(
        'w',
        'weekday',
        consts.WEEKDAY_REGEX,
        int,
        lambda d: '%d' % d.weekday(),
    ),
    Directive(
        'W',
        'weekofyear',
        consts.WEEK_OF_YEAR_REGEX,
        int,
        lambda d: '%.2d' % d.weekofyear(SATURDAY),
    ),
    Directive(
        'U',
        'weekofyear',
        consts.WEEK_OF_YEAR_REGEX,
        int,
        lambda d: '%.2d' % d.weekofyear(MONDAY),
    ),
    Directive(
        'a',
        'weekdayabbr',
        consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
        get_unicode,
        lambda d: d.weekdayabbr(),
    ),
    Directive(
        'A',
        'weekdayname',
        consts.PERSIAN_WEEKDAY_NAMES_REGEX,
        get_unicode,
        lambda d: d.weekdayname(),
    ),
    Directive(
        'e',
        'weekdayabbr_ascii',
        consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
        get_unicode,
        lambda d: d.weekdayabbr_ascii(),
    ),
    Directive(
        'E',
        'weekdayname_ascii',
        consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
        get_unicode,
        lambda d: d.weekdayname_ascii(),
    ),
    Directive(
        'd',
        'day',
        consts.DAY_REGEX,
        int,
        lambda d: '%.2d' % d.day,
    ),
    Directive(
        '%',
        'percent',
        '%',
        None,
        lambda d: '%',
    ),
]


TIME_FORMAT_DIRECTIVES = [
    AmPmDirective(),
    AmPmASCIIDirective(),
    LocalShortDatetimeFormatDirective(),
    LocalDatetimeFormatDirective(),
    LocalASCIIShortDatetimeFormatDirective(),
    LocalASCIIDatetimeFormatDirective(),
    LocalTimeFormatDirective(),
    UTCOffsetDirective(),
    TimezoneNameDirective(),
    PersianMicrosecondDirective(),
    PersianHour12Directive(),
    PersianHour24Directive(),
    Directive(
        'H',
        'hour',
        consts.HOUR24_REGEX,
        int,
        lambda d: '%.2d' % d.hour,
    ),
    Directive(
        'I',
        'hour12',
        consts.HOUR12_REGEX,
        int,
        lambda d: '%.2d' % d.hour12()
    ),
    Directive(
        'M',
        'minute',
        consts.MINUTE_REGEX,
        int,
        lambda d: '%.2d' % d.minute,
    ),
    Directive(
        'S',
        'second',
        consts.SECOND_REGEX,
        int,
        lambda d: '%.2d' % d.second,
    ),
    Directive(
        'f',
        'microsecond',
        consts.MICROSECOND_REGEX,
        int,
        lambda d: '%.6d' % d.microsecond
    ),
    # --------SUPPORTED--------
]

DATETIME_FORMAT_DIRECTIVES = DATE_FORMAT_DIRECTIVES + TIME_FORMAT_DIRECTIVES

__all__ = [
    'Directive',
    'LocalDatetimeFormatDirective',
    'AmPmDirective', 
    'AmPmASCIIDirective',
    'ShortYearDirective',
    'DayOfYearDirective',
    'LocalShortDatetimeFormatDirective',
    'LocalDatetimeFormatDirective',
    'LocalASCIIShortDatetimeFormatDirective', 
    'LocalASCIIDatetimeFormatDirective', 
    'LocalDateFormatDirective', 
    'LocalTimeFormatDirective',
    'UTCOffsetDirective',
    'TimezoneNameDirective',
]

"""
Available directives: k l u v K L O P R T V
"""
