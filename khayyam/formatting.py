# -*- coding: utf-8 -*-
import re
from khayyam.constants import SATURDAY
__author__ = 'vahid'


class JalaliDateFormatter(object):
    """
    =========    =======
    Directive    Meaning
    =========    =======
    %a           Locale’s abbreviated weekday name.
    %A           Locale’s full weekday name.
    %b           Locale’s abbreviated month name.
    %B           Locale’s full month name.
    %d           Day of the month as a decimal number [01,31].
    %j           Day of the year as a decimal number [001,366].
    %m           Month as a decimal number [01,12].
    %w           Weekday as a decimal number [0(Saturday),6(Friday)].
    %W           Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
    %x           Locale’s appropriate date representation.
    %y           Year without century as a decimal number [00,99].
    %Y           Year with century as a decimal number.
    %e           ASCII Locale’s abbreviated weekday name.
    %E           ASCII Locale’s full weekday name.
    %g           ASCII Locale’s abbreviated month name.
    %G           ASCII Locale’s full month name.
    %%           A literal '%' character.
    =========    =======
    """

    # TODO: _first_day_of_week = SATURDAY
    _directives = {
        '%a': ('', lambda d: d.weekdayabbr()),
        '%A': ('', lambda d: d.weekdayname()),
        '%b': ('', lambda d: d.monthabbr()),
        '%B': ('', lambda d: d.monthname()),
        '%j': ('', lambda d: '%.3d' % d.dayofyear()),
        '%w': ('', lambda d: '%d' % d.weekday()),
        '%W': ('', lambda d: '%.2d' % d.weekofyear(SATURDAY)),
        '%x': ('', lambda d: d.localformat()),
        '%y': ('', lambda d: '%.2d' % (d.year % 100)),
        '%Y': ('\d{4}', lambda d: '%.4d' % d.year),
        '%e': ('', lambda d: d.weekdayabbr_ascii()),
        '%E': ('', lambda d: d.weekdayname_ascii()),
        '%g': ('', lambda d: d.monthabbr_ascii()),
        '%G': ('', lambda d: d.monthname_ascii()),
        '%m': ('', lambda d: '%.2d' % d.month),
        '%d': ('', lambda d: '%.2d' % d.day),
        '%%': ('', lambda d: '%'),
    }

    def __init__(self, format):
        self._format = format

    def update_format(self, format):
        self._format = format

    def format(self, jalali_date):
        return self.__class__.format(jalali_date, self._format)

    @classmethod
    def format(cls, jalali_date, fmt):
        result = ''
        index = 0
        for m in re.finditer('%[a-zA-Z%]', fmt):
            directive = m.group()
            if directive in cls._directives:
                if index < m.start():
                    result += fmt[index:m.start()]
                result += cls._directives[directive][1](jalali_date)
                index = m.end()
        return result


    def parse(self, date_string):
        pass
