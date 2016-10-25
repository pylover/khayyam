
import re
from datetime import timedelta

from khayyam.compat import get_unicode, basestring_
from khayyam.algorithms import get_days_in_jalali_year
from khayyam.timezones import Timezone
from khayyam.formatting.constants import DAY_OF_YEAR_REGEX, LATIN_TO_PERSIAN, PERSIAN_TO_LATIN, \
    PERSIAN_DAY_OF_YEAR_REGEX, HOUR12_REGEX, AM_PM, AM_PM_ASCII, UTC_OFFSET_FORMAT_REGEX, \
    PERSIAN_UTC_OFFSET_FORMAT_REGEX, TZ_NAME_FORMAT_REGEX


def persian(s):  # FIXME: Rename it to `persian_digits`
    if not isinstance(s, basestring_):
        s = get_unicode(s)
    return ''.join([LATIN_TO_PERSIAN.get(c, c) for c in s])


def latin_digit(s):
    if not isinstance(s, basestring_):
        s = get_unicode(s)
    return ''.join([PERSIAN_TO_LATIN.get(c, c) for c in s])


class Directive(object):
    """
    Base class for all formatting directives.

    """

    def __init__(self, key, regex, name=None, type_=None, formatter=None, pre_parser=None, post_parser=None):
        self.key = key
        self.regex = regex
        self.name = name
        self.type_ = type_
        if formatter:
            self.format = formatter
        if post_parser:
            self.post_parser = post_parser
        if pre_parser:
            self.pre_parser = pre_parser

    def coerce_type(self, v):
        return v if self.type_ is None else self.type_(v)

    @property
    def target_name(self):
        return self.name or self.key

    @property
    def require_post_parsing(self):
        return hasattr(self, 'post_parser')

    def __repr__(self):
        return '%' + self.key

    def parse(self, ctx, v):
        ctx[self.target_name] = self.coerce_type(v)

    def format(self, d):  # pragma: no cover
        """
        In overridden method, It Should return string representation of the given argument.

        :param d: a value to format
        :return: Formatted value.
        :rtype: str
        """
        raise NotImplementedError


class DayOfYearDirective(Directive):
    """
    Representing day of year.
    """

    def __init__(self, key, regex=None, zero_padded=True):
        self.zero_padded = zero_padded
        super(DayOfYearDirective, self).__init__(key, regex or DAY_OF_YEAR_REGEX, type_=int)

    def format(self, d):
        return ('%.3d' if self.zero_padded else '%d') % d.dayofyear()

    def post_parser(self, ctx, formatter):
        _dayofyear = ctx[self.key]
        if 'year' not in ctx:
            ctx['year'] = 1
        if 'month' in ctx:
            del ctx['month']
        if 'day' in ctx:
            del ctx['day']

        max_days = get_days_in_jalali_year(ctx['year'])
        if _dayofyear > max_days:
            raise ValueError(
                'Invalid dayofyear: %.3d for year %.4d. Valid values are: 1-%s' % (
                    _dayofyear,
                    ctx['year'],
                    max_days))
        from khayyam import JalaliDate
        d = JalaliDate(year=ctx['year']) + timedelta(days=_dayofyear-1)
        ctx.update(
            month=d.month,
            day=d.day
        )


class PersianDayOfYearDirective(DayOfYearDirective):
    """
    Representing day of year in persian.
    """

    def __init__(self, key, regex=None, zero_padded=False, **kw):
        super(PersianDayOfYearDirective, self).__init__(
            key, regex=regex or PERSIAN_DAY_OF_YEAR_REGEX, zero_padded=zero_padded, **kw)

    def format(self, d):
        return persian(super(PersianDayOfYearDirective, self).format(d))


class CompositeDirective(Directive):
    """
    A chain of directives.

    """

    def __init__(self, key, regex, format_string, **kw):
        self.format_string = format_string
        super(CompositeDirective, self).__init__(key, regex, type_=get_unicode, **kw)

    def format(self, d):
        return d.strftime(self.format_string)

    def post_parser(self, ctx, formatter):
        ctx.update(formatter.parse(self.format_string, ctx[self.key]))


class Hour12Directive(Directive):

    def __init__(self, key, regex=None, **kw):
        super(Hour12Directive, self).__init__(
            key,
            regex or HOUR12_REGEX,
            type_=int,
            **kw
        )

    def format(self, d):
        return '%.2d' % d.hour12()

    def post_parser(self, ctx, formatter):
        hour12 = ctx[self.key]
        ctx['hour'] = (0 if hour12 == 12 else hour12) \
            if ('p' in ctx and AM_PM[0] == ctx['p']) or ('t' in ctx and AM_PM_ASCII[0] == ctx['t']) \
            else (hour12 + (12 if hour12 < 12 else 0))


class UTCOffsetDirective(Directive):
    """
    Representing offset from UTC. only for timezone-aware instances.

    """

    def __init__(self, key, regex=None, **kw):
        super(UTCOffsetDirective, self).__init__(
            key,
            regex or UTC_OFFSET_FORMAT_REGEX,
            type_=get_unicode,
            **kw
        )

    def format(self, d):
        if not d.tzinfo:
            return ''
        seconds = d.utcoffset().total_seconds()
        return '%s%.2d:%.2d' % (
            '+' if seconds >= 0 else '-',
            int(seconds / 3600),
            int((seconds % 3600) / 60),
        )

    def post_parser(self, ctx, formatter):
        exp = ctx[self.key]
        if exp.strip() == '':
            return
        regex = '(?P<posneg>[-+]?)(?P<hour>\d{2}):(?P<minute>\d{2})'
        match = re.match(regex, exp)
        d = match.groupdict()
        posneg = lambda i: 0 - i if d['posneg'] == '-' else i
        hours = int(d['hour'])
        minutes = int(d['minute'])
        if not hours and not minutes:
            return
        ctx.update(tzinfo=Timezone(timedelta(hours=posneg(hours), minutes=posneg(minutes))))


class PersianUTCOffsetDirective(UTCOffsetDirective):

    def __init__(self, key, **kw):
        super(PersianUTCOffsetDirective, self).__init__(
            key,
            PERSIAN_UTC_OFFSET_FORMAT_REGEX,
            pre_parser=latin_digit,
            **kw
        )

    def format(self, d):
        return persian(super(PersianUTCOffsetDirective, self).format(d))


class TimezoneNameDirective(Directive):

    def __init__(self, key):
        super(TimezoneNameDirective, self).__init__(
            key,
            TZ_NAME_FORMAT_REGEX,
            name='tzname',
            type_=get_unicode
        )

    def format(self, d):
        if d.tzinfo:
            return d.tzname()
        return ''
