# -*- coding: utf-8 -*-
from khayyam.formatting import JalaliDateFormatter
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


class CompositeDirective(Directive):
    format_string = None

    def __init__(self, key, name, regex, **kw):
        super(CompositeDirective, self).__init__(key, name, regex, get_unicode, **kw)

    def format(self, d):
        return d.strftime(self.format_string)

    def post_parser(self, ctx, formatter):
        ctx.update(JalaliDateFormatter(self.format_string).parse(ctx[self.name]))