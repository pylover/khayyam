# -*- coding: utf-8 -*-
from __future__ import division
from datetime import timedelta

from khayyam.formatting import JalaliTimedeltaFormatter


class JalaliTimedelta(timedelta):
    _parts = None

    @classmethod
    def formatterfactory(cls, fmt):
        return JalaliTimedeltaFormatter(fmt)

    def strftime(self, format_string):
        """
        Format codes referring to hours, minutes or seconds will see 0 values.
        For a complete list of formatting directives, see :doc:`/directives`.

        :param format_string: The format string.
        :return: A string representing the date, controlled by an explicit format string
        :rtype: unicode
        """
        return self.formatterfactory(format_string).format(self)

    @classmethod
    def strptime(cls, date_string, fmt):
        """
        Return a :py:class:`khayyam.JalaliTimedelta` corresponding to *date_string*, parsed according to format.

        :py:class:`ValueError` is raised if the *date_string* and format can't be parsed with
        :py:class:`khayyam.formatting.JalaliTimedeltaFormatter` instance returned by
        :py:meth:`khayyam.JalaliTimedelta.formatterfactory` method.

        :param date_string: str The representing date & time in specified format.
        :param fmt: str The format string.
        :return: Jalali timedelta object.
        :rtype: :py:class:`khayyam.JalaliTimedelta`
        """

        result = cls.formatterfactory(fmt).parse(date_string)
        #
        # def assert_a_xor_b(a, b):
        #     if a in result:
        #         if b in result:
        #             raise ValueError('Cannot use %s and %s, together.' % (a, b))
        #         result[b] = result[a]
        #         del result[a]
        #
        # assert_a_xor_b('total_hours', 'hours')
        # assert_a_xor_b('total_minutes', 'minutes')

        result = {k: v for k, v in result.items() if k in (
            'days', 'hours', 'minutes', 'seconds', 'milliseconds', 'microseconds'
        )}

        return cls(**result)

    def _calculate_parts(self):
        # days, seconds, microseconds
        remaining_seconds = self.seconds
        hours = remaining_seconds // 3600  # 1-23
        remaining_seconds %= 3600
        total_hours = self.days * 24 + hours + remaining_seconds / 3600

        minutes = remaining_seconds / 60  # 1-59
        remaining_seconds %= 60
        total_minutes = total_hours * 60 + remaining_seconds / 60
        seconds = remaining_seconds  # 1-59

        self._parts = {
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'total_hours': total_hours,
            'total_minutes': total_minutes
        }

    @property
    def parts(self):
        if self._parts is None:
            self._calculate_parts()
        return self._parts

    @property
    def hours(self):
        return self.parts['hours']

    @property
    def total_hours(self):
        return self.parts['total_hours']

    @property
    def minutes(self):
        return self.parts['minutes']

    @property
    def total_minutes(self):
        return self.parts['total_minutes']