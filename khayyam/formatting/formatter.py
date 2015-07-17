# -*- coding: utf-8 -*-
import re
from datetime import timedelta
from .directives import DATE_FORMAT_DIRECTIVES
import khayyam.constants as consts
from khayyam.algorithms import days_in_year
__author__ = 'vahid'


class JalaliDateFormatter(object):
    def __init__(self, format_string, directive_db=DATE_FORMAT_DIRECTIVES):
        self.format_string = format_string
        self.directives = directive_db
        self.directives_by_key = {d.key:d for d in self.directives}
        self.directives_by_name = {d.name:d for d in self.directives}
        self._parser_regex = self._create_parser_regex()

    def _create_parser_regex(self):
        regex = '^'
        index = 0
        for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, self.format_string):
            directive_key = m.group()[1:]
            if directive_key not in self.directives_by_key:
                continue
            directive = self.directives_by_key[directive_key]
            if index < m.start():
                regex += self.format_string[index:m.start()]
            index = m.end()
            if directive.key == '%':
                regex += '%'
                continue
            regex += '(?P<%(group_name)s>%(regexp)s)' % dict(
                group_name=directive.key,
                regexp=directive.regex
            )
        regex += self.format_string[index:]
        regex += '$'
        return regex

    @property
    def parser_regex(self):
        return self._parser_regex

    def iter_format_directives(self):
        for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, self.format_string):
            key = m.group()[1:]
            if key in self.directives_by_key:
                yield m, self.directives_by_key[key]

    def format(self, jalali_date):
        result = ''
        index = 0
        for match, directive in self.iter_format_directives():
            if index < match.start():
                result += self.format_string[index:match.start()]
            result += directive.formatter(jalali_date)
            index = match.end()
        result += self.format_string[index:]
        return result

    def _parse(self, date_string):
        m = re.match(self.parser_regex, date_string)
        if not m:
            raise ValueError("time data '%s' does not match format '%s' with generated regex: '%s'" % (
                date_string, self.format_string, self.parser_regex))
        result = {}
        for directive_key, v in m.groupdict().items():
            if directive_key == 'percent':
                continue
            if directive_key not in self.directives_by_key:
                raise ValueError('directive key: %%%s was not exists.' % directive_key)
            directive = self.directives_by_key[directive_key]
            if not directive.type_:
                continue
            result[directive.name] = directive.type_(v)
        return result

    def _parse_post_processor(self, parse_result):
        if 'localformat' in parse_result:
            # TODO: Add this behavior to the documents
            regex = ' '.join([
                '(?P<weekdayname>%s)' % consts.PERSIAN_WEEKDAY_NAMES_REGEX,
                '(?P<day>%s)' % consts.DAY_REGEX,
                '(?P<monthname>%s)' % consts.PERSIAN_MONTH_NAMES_REGEX,
                '(?P<year>%s)' % consts.YEAR_REGEX
            ])

            match = re.match(regex, parse_result['localformat'])
            d = match.groupdict()
            parse_result.update(dict(
                weekdayname = self.directives_by_key['A'].type_(d['weekdayname']),
                day = self.directives_by_key['d'].type_(d['day']),
                monthname = self.directives_by_key['B'].type_(d['monthname']),
                year = self.directives_by_key['Y'].type_(d['year'])
            ))

        if 'monthabbr' in parse_result:
            # TODO: Add this behavior to the documents
            # TODO: Smarter search, ا == آ and etc..
            # abbr = parse_result['monthabbr']
            # m = [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == abbr]
            # parse_result['month'] = m[0][0]
            directive = self.directives_by_name['monthabbr']
            parse_result.update(directive.post_parser(parse_result))

        if 'monthabbr_ascii' in parse_result:
            # TODO: Add this behavior to the documents
            abbr = parse_result['monthabbr_ascii']
            m = [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS_ASCII.items() if v == abbr]
            parse_result['month'] = m[0][0]

        if 'monthname' in parse_result:
            # TODO: Add this behavior to the documents
            # TODO: Smarter search, ا == آ and etc..
            month_name = parse_result['monthname']
            m = [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES.items() if v == month_name]
            parse_result['month'] = m[0][0]

        if 'monthname_ascii' in parse_result:
            # TODO: Add this behavior to the documents
            month_name = parse_result['monthname_ascii']
            m = [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES_ASCII.items() if v == month_name]
            parse_result['month'] = m[0][0]

        if 'shortyear' in parse_result:
            # TODO: Add this behavior to the documents
            # TODO: Smarter search, ا == آ and etc..
            from khayyam import JalaliDate
            parse_result['year'] = int(JalaliDate.today().year / 100) * 100 + parse_result['shortyear']

        if 'dayofyear' in parse_result:
            # TODO: Add this behavior to the documents
            _dayofyear = parse_result['dayofyear']
            if 'year' not in parse_result:
                parse_result['year'] = 1
            if 'month' in parse_result:
                del parse_result['month']
            if 'day' in parse_result:
                del parse_result['day']

            max_days = days_in_year(parse_result['year'])
            if _dayofyear > max_days:
                raise ValueError(
                    'Invalid dayofyear: %.3d for year %.4d. Valid values are: 1-%s' \
                     % (_dayofyear, parse_result['year'], max_days))
            from khayyam import JalaliDate
            d = JalaliDate(year=parse_result['year']) + timedelta(days=_dayofyear-1)
            parse_result.update(dict(
                month=d.month,
                day=d.day
            ))

        return parse_result

    def parse(self, date_string):
        result = self._parse(date_string)
        self._parse_post_processor(result)
        return result

