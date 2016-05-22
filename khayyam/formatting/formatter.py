# -*- coding: utf-8 -*-
import re
from khayyam.formatting import constants as consts
from .directives import DATE_FORMAT_DIRECTIVES
__author__ = 'vahid'


class BaseFormatter(object):
    pass


class JalaliDateFormatter(BaseFormatter):

    _post_parsers = [
        'persianday',
        'persiandayzeropadded',
        'persiandayofyear',
        'persiandayofyearzeropadded',
        'persianmonth',
        'persianmonthzeropadded',
        'persianyear',
        'persianyearzeropadded',
        'persianshortyear',
        'persianshortyearzeropadded',
        'localdateformat',
        'monthabbr',
        'monthabbr_ascii',
        'monthname',
        'monthnameascii',
        'shortyear',
        'dayofyear',
    ]

    def __init__(self, format_string, directive_db=None):
        if not directive_db:
            directive_db = DATE_FORMAT_DIRECTIVES
        self.format_string = format_string
        self.directives = directive_db
        self.directives_by_key = {d.key: d for d in self.directives}
        self.directives_by_name = {d.name: d for d in self.directives}
        self._parser_regex = self._create_parser_regex()

    def _create_parser_regex(self):
        regex = u'^'
        index = 0
        for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, self.format_string):
            directive_key = m.group()[1:]
            if directive_key not in self.directives_by_key:
                continue
            directive = self.directives_by_key[directive_key]
            if index < m.start():
                regex += self.format_string[index:m.start()]
            index = m.end()
            if directive.key == u'%':
                regex += u'%'
                continue
            regex += u'(?P<%(group_name)s>%(regexp)s)' % dict(
                group_name=directive.key,
                regexp=directive.regex
            )
        regex += self.format_string[index:]
        regex += u'$'
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
            result += directive.format(jalali_date)
            index = match.end()
        result += self.format_string[index:]
        return result

    @staticmethod
    def filter_persian_digit(s):
        for p, e in consts.PERSIAN_DIGIT_MAPPING:
            s = s.replace(p[1], p[0])
        return s

    def _parse(self, date_string):
        m = re.match(self.parser_regex, self.filter_persian_digit(date_string))
        if not m:
            raise ValueError(u"time data '%s' does not match format '%s' with generated regex: '%s'" % (
                date_string, self.format_string, self.parser_regex))
        result = {}
        for directive_key, v in m.groupdict().items():
            if directive_key == 'percent':
                continue
            if directive_key not in self.directives_by_key:
                raise ValueError(u'directive key: %%%s was not exists.' % directive_key)
            directive = self.directives_by_key[directive_key]
            if not directive.type_:
                continue
            result[directive.name] = directive.type_(v)
        return result

    @property
    def post_parsers(self):
        return self._post_parsers

    def _parse_post_processor(self, parse_result):
        for directive_name in self.post_parsers:
            if directive_name in parse_result:
                self.directives_by_name[directive_name].post_parser(parse_result, self)

    def parse(self, date_string):
        result = self._parse(date_string)
        self._parse_post_processor(result)
        return result


class JalaliDatetimeFormatter(JalaliDateFormatter):
    _post_parsers = [
        'persianday',
        'persiandayzeropadded',
        'persiandayofyear',
        'persiandayofyearzeropadded',
        'persianmonth',
        'persianmonthzeropadded',
        'persianyear',
        'persianyearzeropadded',
        'persianshortyear',
        'persianshortyearzeropadded',
        'persianmicrosecond',
        'persianhour12',
        'persianhour12zeropadded',
        'persianhour24',
        'persianhour24zeropadded',
        'persianminute',
        'persianminutezeropadded',
        'persiansecond',
        'persiansecondzeropadded',
        'persianutcoffset',
        'localdateformat',
        'localshortdatetimeformat',
        'localshortdatetimeformatascii',
        'localdatetimeformat',
        'localdatetimeformatascii',
        'localtimeformat',
        'monthabbr',
        'monthabbr_ascii',
        'monthname',
        'monthnameascii',
        'ampm',
        'ampmascii',
        'shortyear',
        'dayofyear',
        'utcoffset'
    ]

    def __init__(self, format_string, directive_db=None):
        if not directive_db:
            from .directives import DATETIME_FORMAT_DIRECTIVES
            directive_db = DATETIME_FORMAT_DIRECTIVES
        super(JalaliDatetimeFormatter, self).__init__(format_string, directive_db=directive_db)
