# -*- coding: utf-8 -*-
import re
from datetime import timedelta
import khayyam.constants as consts
from khayyam.compat import get_unicode
from khayyam.algorithms import days_in_year
__author__ = 'vahid'


# TODO: _first_day_of_week = SATURDAY
FORMAT_DIRECTIVES = {

    '%Y': (
        'year',
        consts.YEAR_REGEX,
        lambda d: '%.4d' % d.year,
        lambda v: int(v)
    ),
    '%y': (
        'shortyear',
        consts.SHORT_YEAR_REGEX,
        lambda d: '%.2d' % (d.year % 100),
        int
    ),
    '%m': (
        'month',
        consts.MONTH_REGEX,
        lambda d: '%.2d' % d.month,
        int
    ),
    '%b': (
        'monthabbr',
        consts.PERSIAN_MONTH_ABBRS_REGEX,
        lambda d: d.monthabbr(),
        get_unicode
    ),
    '%B': (
        'monthname',
        consts.PERSIAN_MONTH_NAMES_REGEX,
        lambda d: d.monthname(),
        get_unicode
    ),
    '%g': (
        'monthabbr_ascii',
        consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
        lambda d: d.monthabbr_ascii(),
        get_unicode),
    '%G': (
        'monthname_ascii',
        consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
        lambda d: d.monthname_ascii(),
        get_unicode),
    '%w': (
        'weekday',
        consts.WEEKDAY_REGEX,
        lambda d: '%d' % d.weekday(),
        int
    ),
    '%W': (
        'weekofyear',
        consts.WEEK_OF_YEAR_REGEX,
        lambda d: '%.2d' % d.weekofyear(consts.SATURDAY),
        int
    ),
    '%a': (
        'weekdayabbr',
        consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
        lambda d: d.weekdayabbr(),
        get_unicode
    ),
    '%A': (
        'weekdayname',
        consts.PERSIAN_WEEKDAY_NAMES_REGEX,
        lambda d: d.weekdayname(),
        get_unicode
    ),
    '%e': (
        'weekdayabbr_ascii',
        consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
        lambda d: d.weekdayabbr_ascii(),
        get_unicode
    ),
    '%E': (
        'weekdayname_ascii',
        consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
        lambda d: d.weekdayname_ascii(),
        get_unicode
    ),
    '%d': (
        'day',
        consts.DAY_REGEX,
        lambda d: '%.2d' % d.day,
        int
    ),
    '%j': (
        'dayofyear',
        consts.DAY_OF_YEAR_REGEX,
        lambda d: '%.3d' % d.dayofyear(),
        int
    ),
    '%x': (
        'localformat',
        consts.LOCAL_FORMAT_REGEX,
        lambda d: d.localformat(),
        get_unicode),
    # --------SUPPORTED--------
    '%%': (
        'percent',
        '%',
        lambda d: '%',
        None
    ),
}


def format(jalali_date, fmt):
    result = ''
    index = 0
    for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, fmt):
        directive = m.group()
        if directive in FORMAT_DIRECTIVES:
            if index < m.start():
                result += fmt[index:m.start()]
            result += FORMAT_DIRECTIVES[directive][2](jalali_date)
            index = m.end()
    result += fmt[index:]
    return result


def parse(date_string, fmt):
    regex = '^'
    index = 0
    for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, fmt):
        directive = m.group()
        if directive not in FORMAT_DIRECTIVES:
            continue
        if index < m.start():
            regex += fmt[index:m.start()]
        index = m.end()
        if directive == '%%':
            regex += '%'
            continue
        group_name = directive[1:]
        regex += '(?P<%(group_name)s>%(regexp)s)' % dict(
            group_name=group_name,
            regexp=FORMAT_DIRECTIVES[directive][1]
        )
    regex += fmt[index:]

    regex += '$'
    m = re.match(regex, date_string)
    if not m:
        raise ValueError("time data '%s' does not match format '%s' with generated regex: '%s'" % (
            date_string, fmt, regex))

    result = {}
    for k, v in m.groupdict().items():
        if k == 'percent':
            continue
        directive_key = '%%%s' % k
        if directive_key not in FORMAT_DIRECTIVES:
            raise ValueError('directive key: %s was not exists.' % directive_key)
        directive = FORMAT_DIRECTIVES[directive_key]
        name = directive[0]
        validator = directive[3]
        if not validator:
            continue
        result[name] = validator(v)


    if 'localformat' in result:
        # TODO: Add this behavior to the documents
        regex = ' '.join([
            '(?P<weekdayname>%s)' % consts.PERSIAN_WEEKDAY_NAMES_REGEX,
            '(?P<day>%s)' % consts.DAY_REGEX,
            '(?P<monthname>%s)' % consts.PERSIAN_MONTH_NAMES_REGEX,
            '(?P<year>%s)' % consts.YEAR_REGEX
        ])

        match = re.match(regex, result['localformat'])
        d = match.groupdict()
        result.update(dict(
            weekdayname = FORMAT_DIRECTIVES['%A'][3](d['weekdayname']),
            day = FORMAT_DIRECTIVES['%d'][3](d['day']),
            monthname = FORMAT_DIRECTIVES['%B'][3](d['monthname']),
            year = FORMAT_DIRECTIVES['%Y'][3](d['year'])
        ))

    if 'monthabbr' in result:
        # TODO: Add this behavior to the documents
        # TODO: Smarter search, ا == آ and etc..
        abbr = result['monthabbr']
        m = [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == abbr]
        result['month'] = m[0][0]

    if 'monthabbr_ascii' in result:
        # TODO: Add this behavior to the documents
        abbr = result['monthabbr_ascii']
        m = [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS_ASCII.items() if v == abbr]
        result['month'] = m[0][0]

    if 'monthname' in result:
        # TODO: Add this behavior to the documents
        # TODO: Smarter search, ا == آ and etc..
        month_name = result['monthname']
        m = [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES.items() if v == month_name]
        result['month'] = m[0][0]

    if 'monthname_ascii' in result:
        # TODO: Add this behavior to the documents
        month_name = result['monthname_ascii']
        m = [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES_ASCII.items() if v == month_name]
        result['month'] = m[0][0]

    if 'shortyear' in result:
        # TODO: Add this behavior to the documents
        # TODO: Smarter search, ا == آ and etc..
        from khayyam import JalaliDate
        result['year'] = int(JalaliDate.today().year / 100) * 100 + result['shortyear']

    if 'dayofyear' in result:
        # TODO: Add this behavior to the documents
        _dayofyear = result['dayofyear']
        if 'year' not in result:
            result['year'] = 1
        if 'month' in result:
            del result['month']
        if 'day' in result:
            del result['day']

        max_days = days_in_year(result['year'])
        if _dayofyear > max_days:
            raise ValueError(
                'Invalid dayofyear: %.3d for year %.4d. Valid values are: 1-%s' \
                 % (_dayofyear, result['year'], max_days))
        from khayyam import JalaliDate
        d = JalaliDate(year=result['year']) + timedelta(days=_dayofyear-1)
        result.update(dict(
            month=d.month,
            day=d.day
        ))




    return result
