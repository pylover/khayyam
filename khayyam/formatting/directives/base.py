# -*- coding: utf-8 -*-
from khayyam.compat import get_unicode
__author__ = 'vahid'


class Directive(object):
    """
    Base class for all formatting directives.

    """

    def __init__(self, key, name, regex, type_, formatter=None, post_parser=None):
        self.key = key
        self.name = name
        self.regex = regex
        self.type_ = type_
        if formatter:
            self.format = formatter
        if post_parser:
            self.post_parser = post_parser

    def __repr__(self):  # pragma: no cover
        return '%' + self.key

    def post_parser(self, ctx, formatter):  # pragma: no cover
        """
        In overridden method, It should parse the formatted value from the given string.
        :param ctx:
        :param formatter:
        :return:
        """
        pass

    def format(self, d):  # pragma: no cover
        """
        In overridden method, It Should return string representation of the given argument.

        :param d: a value to format
        :return: Formatted value.
        :rtype: str
        """
        return d


class CompositeDateDirective(Directive):
    """
    A chain of directives, Representing a date.

    """

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
        """

        :return: The underlying formatter.
        :rtype: :py:class:`khayyam.JalaliDateFormatter`
        """
        if not self._sub_formatter:
            self._sub_formatter = self._create_formatter()
        return self._sub_formatter

    def format(self, d):
        return d.strftime(self.format_string)

    def post_parser(self, ctx, formatter):
        ctx.update(self.sub_formatter.parse(ctx[self.name]))


class CompositeDatetimeDirective(CompositeDateDirective):
    """
    A chain of directives, Representing a datetime.

    """
    format_string = None

    def _create_formatter(self):
        from khayyam.formatting import JalaliDatetimeFormatter
        return JalaliDatetimeFormatter(self.format_string)
