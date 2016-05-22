# -*- coding: utf-8 -*-
from .directive import Directive
from khayyam.compat import get_unicode
from khayyam.formatting.constants import PERSIAN_DIGIT_MAPPING

__author__ = 'vahid'


eng_to_persian_dict = {e: p[0] for p, e in PERSIAN_DIGIT_MAPPING}
persian_to_eng_dict = {p[0]: e for p, e in PERSIAN_DIGIT_MAPPING}

eng_to_persian = lambda s: ''.join([eng_to_persian_dict[c] if c in eng_to_persian_dict else c for c in s])
persian_to_eng = lambda s: ''.join([persian_to_eng_dict[c] if c in persian_to_eng_dict else c for c in s])


class PersianNumberDirective(Directive):
    def __init__(self, key, name, regex, zero_padding=False, zero_padding_length=2):
        self.zero_padding = zero_padding
        self.zero_padding_length = zero_padding_length
        super(PersianNumberDirective, self).__init__(key, name, regex, get_unicode)

    def format(self, i):
        if self.zero_padding:
            fmt = '%%.%dd' % self.zero_padding_length
            return eng_to_persian(fmt % i)
        elif isinstance(i, int):
            return eng_to_persian(str(i))
        else:
            return eng_to_persian(i)

    def post_parser(self, ctx, formatter):
        exp = ctx[self.name]
        if exp.strip() != '':
            ctx[self.name] = int(persian_to_eng(exp))
