# -*- coding: utf-8 -*-
import re
from .base import Directive
from .persian import PersianNumberDirective, persian_to_eng
from datetime import timedelta
from khayyam.timezones import Timezone
__author__ = 'vahid'


class PersianUTCOffsetDirective(PersianNumberDirective):
    """
    Representing offset from UTC in persian form. only for timezone-aware instances.

    """

    def format(self, d):
        if not d.tzinfo:
            return ''
        seconds = d.utcoffset().total_seconds()
        return super(PersianUTCOffsetDirective, self).format('%s%.2d:%.2d' % (
            '+' if seconds >= 0 else '-',
            int(seconds / 3600),
            int((seconds % 3600) / 60),
        ))

    def post_parser(self, ctx, formatter):
        exp = ctx[self.name]
        if exp.strip() != '':
            ctx['utcoffset'] = persian_to_eng(exp)


class TimezoneNameDirective(Directive):
    """
    Representing the timezone name. only for timezone-aware instances.

    """
    def format(self, d):
        if d.tzinfo:
            return d.tzname()
        return ''
