# -*- coding: utf-8 -*-
from datetime import timedelta

from khayyam.formatting import JalaliTimedeltaFormatter


class JalaliTimedelta(timedelta):

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
        result = {k: v for k, v in result.items() if k in ('days', 'seconds', 'microseconds')}
        return cls(**result)
