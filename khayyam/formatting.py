# -*- coding: utf-8 -*-
import khayyam.constants as consts
__author__ = 'vahid'

# TODO: _first_day_of_week = SATURDAY
FORMAT_DIRECTIVE_REGEX = '%[a-zA-Z%]'
FORMAT_DIRECTIVES = {
    '%a': ('weekdayabbr',       consts.PERSIAN_WEEKDAY_ABBRS_REGEX, lambda d: d.weekdayabbr(), None),
    '%A': ('weekdayname',       consts.PERSIAN_WEEKDAY_NAMES_REGEX, lambda d: d.weekdayname(), None),
    '%b': ('monthabbr',         consts.PERSIAN_MONTH_ABBRS_REGEX, lambda d: d.monthabbr(), None),
    '%B': ('monthname',         consts.PERSIAN_MONTH_NAMES_REGEX, lambda d: d.monthname(), None),
    '%j': ('dayofyear',         '\d{1,3}', lambda d: '%.3d' % d.dayofyear(), int),
    '%w': ('weekday',           '', lambda d: '%d' % d.weekday(), None),
    '%W': ('weekofyear',        '', lambda d: '%.2d' % d.weekofyear(consts.SATURDAY), None),
    '%x': ('localformat',       '', lambda d: d.localformat(), None),
    '%y': ('short_year',        '\d{2}', lambda d: '%.2d' % (d.year % 100), None),
    '%Y': ('year',              '\d{4}', lambda d: '%.4d' % d.year, lambda v: int(v)),
    '%e': ('weekdayabbr_ascii', '', lambda d: d.weekdayabbr_ascii(), None),
    '%E': ('weekdayname_ascii', '', lambda d: d.weekdayname_ascii(), None),
    '%g': ('monthabbr_ascii',   '', lambda d: d.monthabbr_ascii(), None),
    '%G': ('monthname_ascii',   '', lambda d: d.monthname_ascii(), None),
    '%m': ('month',             '([0]?[1-9]|1[0-2])', lambda d: '%.2d' % d.month, int),
    '%d': ('day',               '([0]?[1-9]|[12]\d|3[01])', lambda d: '%.2d' % d.day, int),
    '%%': ('percent',           '', lambda d: '%', None),
}






