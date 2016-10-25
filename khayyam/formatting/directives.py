
from datetime import timedelta

from khayyam.compat import get_unicode
from khayyam.algorithms import get_days_in_jalali_year
from khayyam.formatting.constants import DAY_OF_YEAR_REGEX, LATIN_TO_PERSIAN, PERSIAN_DAY_OF_YEAR_REGEX


def persian(s):
    if not isinstance(s, basestring):
        s = get_unicode(s)
    return ''.join([LATIN_TO_PERSIAN.get(c, c) for c in s])


class Directive(object):
    """
    Base class for all formatting directives.

    """

    def __init__(self, key, regex, name=None, type_=None, formatter=None, post_parser=None):
        self.key = key
        self.regex = regex
        self.name = name
        self.type_ = type_
        if formatter:
            self.format = formatter
        if post_parser:
            self.post_parser = post_parser

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
