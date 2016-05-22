# -*- coding: utf-8 -*-
from khayyam.compat import get_unicode
__author__ = 'vahid'


class Directive(object):
    def __init__(self, key, name, regex, type_, formatter=None, post_parser=None):
        self.key = key
        self.name = name
        self.regex = regex
        self.type_ = type_
        if formatter:
            self.format = formatter
        if post_parser:
            self.post_parser = post_parser

    def __repr__(self):
        return '%' + self.key

    def post_parser(self, ctx, formatter):
        pass

    def format(self, d):
        return d


class CompositeDateDirective(Directive):
    format_string = None

    def __init__(self, key, name, regex, format_string=None, **kw):
        if format_string:
            self.format_string = format_string
            self._sub_formatter = None
        super(CompositeDateDirective, self).__init__(key, name, regex, get_unicode, **kw)

    def _create_formatter(self):
        from khayyam.formatting import JalaliDateFormatter
        return JalaliDateFormatter(self.format_string)

    @property
    def sub_formatter(self):
        if not self._sub_formatter:
            self._sub_formatter = self._create_formatter()
        return self._sub_formatter

    def format(self, d):
        return d.strftime(self.format_string)

    def post_parser(self, ctx, formatter):
        ctx.update(self.sub_formatter.parse(ctx[self.name]))


class CompositeDatetimeDirective(CompositeDateDirective):
    format_string = None

    def _create_formatter(self):
        from khayyam.formatting import JalaliDatetimeFormatter
        return JalaliDatetimeFormatter(self.format_string)