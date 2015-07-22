# -*- coding: utf-8 -*-
from .directive import Directive
from khayyam.compat import get_unicode

__author__ = 'vahid'

_mapping = [
    (u'۰', u'0'),
    (u'۱', u'1'),
    (u'۲', u'2'),
    (u'۳', u'3'),
    (u'۴', u'4'),
    (u'۵', u'5'),
    (u'۶', u'6'),
    (u'۷', u'7'),
    (u'۸', u'8'),
    (u'۹', u'9'),
]

eng_to_persian_dict = {e: p for p, e in _mapping}
persian_to_eng_dict = {p: e for p, e in _mapping}

eng_to_persian = lambda s: ''.join([eng_to_persian_dict[c] if c in eng_to_persian_dict else c for c in s])
persian_to_eng = lambda s: ''.join([persian_to_eng_dict[c] if c in persian_to_eng_dict else c for c in s])


class PersianNumberDirective(Directive):
    def __init__(self, key, name, regex):
        super(PersianNumberDirective, self).__init__(key, name, regex, get_unicode)

    def format(self, i):
        return eng_to_persian(i)

    def post_parser(self, ctx, formatter):
        exp = ctx[self.name]
        if exp.strip() != '':
            ctx[self.name] = int(persian_to_eng(exp))
