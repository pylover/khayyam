# -*- coding: utf-8 -*-
from .directive import CompositeDirective
__author__ = 'vahid'

class LocalDateFormatDirective(CompositeDirective):
    format_string = "%A %D %B %N"


class LocalShortDatetimeFormatDirective(CompositeDirective):
    format_string = "%a %d %b %y %H:%M"


class LocalASCIIShortDatetimeFormatDirective(CompositeDirective):
    format_string = "%e %d %g %y %H:%M"


class LocalDatetimeFormatDirective(CompositeDirective):
    format_string = "%A %d %B %Y %I:%M:%S %p"


class LocalASCIIDatetimeFormatDirective(CompositeDirective):
    format_string = "%E %d %G %Y %I:%M:%S %t"


class LocalTimeFormatDirective(CompositeDirective):
    format_string = "%I:%M:%S %p"

