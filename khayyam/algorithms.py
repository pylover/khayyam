# -*- coding: utf-8 -*-
import warnings

__author__ = 'vahid'

try:
    from .algorithms_c import \
        is_leap_year, \
        get_julian_day_from_gregorian

except ImportError:
    warnings.warn(
        "The Cython extension is not available. Switching to fallback python pure algorithms, "
        "so it's may be slower than C implementation of the algorithms.")
    from .algorithms_pure import \
        is_leap_year, \
        get_julian_day_from_gregorian

from .algorithms_pure import \
    days_in_month, \
    days_in_year, \
    gregorian_date_from_julian_day, \
    jalali_date_from_gregorian_date, \
    jalali_date_from_julian_day, \
    julian_day_from_jalali_date


