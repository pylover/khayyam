# -*- coding: utf-8 -*-
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
        return ctx

    def format(self, d):
        return d

