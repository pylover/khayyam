# -*- coding: utf-8 -*-
from __future__ import unicode_literals

PERSIAN_DIGIT_MAPPING = [
    (('\u06f0', '\u0660'), '0'),
    (('\u06f1', '\u0661'), '1'),
    (('\u06f2', '\u0662'), '2'),
    (('\u06f3', '\u0663'), '3'),
    (('\u06f4', '\u0664'), '4'),
    (('\u06f5', '\u0665'), '5'),
    (('\u06f6', '\u0666'), '6'),
    (('\u06f7', '\u0667'), '7'),
    (('\u06f8', '\u0668'), '8'),
    (('\u06f9', '\u0669'), '9'),
]


PERSIAN_WEEKDAY_NAMES = {
    0: 'شنبه',
    1: 'یکشنبه',
    2: 'دوشنبه',
    3: 'سه شنبه',
    4: 'چهارشنبه',
    5: 'پنجشنبه',
    6: 'جمعه'
}

PERSIAN_WEEKDAY_ABBRS = {
    0: 'ش',
    1: 'ی',
    2: 'د',
    3: 'س',
    4: 'چ',
    5: 'پ',
    6: 'ج'
}

PERSIAN_MONTH_NAMES = {
    1: 'فروردین',
    2: 'اردیبهشت',
    3: 'خرداد',
    4: 'تیر',
    5: 'مرداد',
    6: 'شهریور',
    7: 'مهر',
    8: 'آبان',
    9: 'آذر',
    10: 'دی',
    11: 'بهمن',
    12: 'اسفند'}

PERSIAN_MONTH_ABBRS = {
    1: 'فر',
    2: 'ار',
    3: 'خر',
    4: 'تی',
    5: 'مر',
    6: 'شه',
    7: 'مه',
    8: 'آب',
    9: 'آذ',
    10: 'دی',
    11: 'به',
    12: 'اس'}

PERSIAN_WEEKDAY_NAMES_ASCII = {
    0: 'Shanbeh',
    1: 'Yekshanbeh',
    2: 'Doshanbeh',
    3: 'Seshanbeh',
    4: 'Chaharshanbeh',
    5: 'Panjshanbeh',
    6: 'Jomeh',
}


PERSIAN_WEEKDAY_ABBRS_ASCII = {
    0: 'Sh',
    1: 'Y',
    2: 'D',
    3: 'Se',
    4: 'Ch',
    5: 'P',
    6: 'J'
}



PERSIAN_MONTH_NAMES_ASCII = {
    1: 'Farvardin',
    2: 'Ordibehesht',
    3: 'Khordad',
    4: 'Tir',
    5: 'Mordad',
    6: 'Shahrivar',
    7: 'Mehr',
    8: 'Aban',
    9: 'Azar',
    10: 'Dey',
    11: 'Bahman',
    12: 'Esfand'
}

PERSIAN_MONTH_ABBRS_ASCII = {
    1: 'F',
    2: 'O',
    3: 'Kh',
    4: 'T',
    5: 'Mo',
    6: 'Sh',
    7: 'M',
    8: 'Ab',
    9: 'Az',
    10: 'D',
    11: 'B',
    12: 'E'}



AM_PM = {
    0: 'ق.ظ',
    1: 'ب.ظ'
}

AM_PM_ASCII = {
    0: 'AM',
    1: 'PM'
}



FORMAT_DIRECTIVE_REGEX = '%[a-zA-Z%]'
YEAR_REGEX = '\d{1,4}'
SHORT_YEAR_REGEX = '\d{2}'
MONTH_REGEX = '([0]?[1-9]|1[0-2])'
DAY_REGEX = '([0]?[1-9]|[12]\d|3[01])' # 1-31
DAY_OF_YEAR_REGEX = '([0]{0,2}[1-9]|[0]?[1-9]\d|[12]\d{2}|3[0-5]\d|36[0-6])' # 1-366
WEEK_OF_YEAR_REGEX = '([0]?\d|[1-4]\d|5[0-3])'  # 0-53
WEEKDAY_REGEX = '[0-6]'
AM_PM_REGEX = '(%s)' % '|'.join(AM_PM.values())
AM_PM_ASCII_REGEX = '([aA][mM]|[pP][mM])'
HOUR12_REGEX = '(0[1-9]|1[0-2])'
HOUR24_REGEX = '([01]\d|2[0-3])'
MINUTE_REGEX = '([0]?\d|[1-5]\d)'
SECOND_REGEX = '([0]?\d|[1-5]\d)'
MICROSECOND_REGEX = '\d{1,6}'
UTC_OFFSET_FORMAT_REGEX = '([-+]?\d{2}:\d{2}|)'
TZ_NAME_FORMAT_REGEX='.+'

PERSIAN_YEAR_REGEX = '[۰۱۲۳۴۵۶۷۸۹]{1,4}'
PERSIAN_YEAR_ZERO_PADDED_REGEX = '[۰۱۲۳۴۵۶۷۸۹]{1,4}'
PERSIAN_SHORT_YEAR_REGEX = '(۰|[۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]?)'
PERSIAN_SHORT_YEAR_ZERO_PADDED_REGEX = '[۰۱۲۳۴۵۶۷۸۹]{1,2}'
PERSIAN_MONTH_REGEX = '([۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_MONTH_ZERO_PADDED_REGEX = '(۰[۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_DAY_REGEX = '([۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]|۳[۰۱])' # ۱-۳۱
PERSIAN_DAY_ZERO_PADDED_REGEX = '(۰[۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]|۳[۰۱])' # ۰۱-۳۱
PERSIAN_DAY_OF_YEAR_REGEX = '([۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]{2}|۳[۰۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹]|۳۶[۰۱۲۳۴۵۶])' # ۱-۳۶۶
PERSIAN_DAY_OF_YEAR_ZERO_PADDED_REGEX = '(۰۰[۱۲۳۴۵۶۷۸۹]|۰[۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]{2}|۳[۰۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹]|۳۶[۰۱۲۳۴۵۶])' # ۰۰۱-۳۶۶
PERSIAN_HOUR12_REGEX = '([۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_HOUR12_ZERO_PADDED_REGEX = '(۰[۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_HOUR24_REGEX = '([۰۱۲۳۴۵۶۷۸۹]|۱[۰۱۲۳۴۵۶۷۸۹]|۲[۰۱۲۳])'
PERSIAN_HOUR24_ZERO_PADDED_REGEX = '(۰[۰۱۲۳۴۵۶۷۸۹]|۱[۰۱۲۳۴۵۶۷۸۹]|۲[۰۱۲۳])'

PERSIAN_MINUTE_REGEX = '([۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'
PERSIAN_MINUTE_ZERO_PADDED_REGEX = '(۰[۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'

PERSIAN_SECOND_REGEX = '([۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'
PERSIAN_SECOND_ZERO_PADDED_REGEX = '(۰[۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'

PERSIAN_MICROSECOND_REGEX = '[۰۱۲۳۴۵۶۷۸۹]{1,6}'
PERSIAN_UTC_OFFSET_FORMAT_REGEX = '([-+]?[۰۱۲۳۴۵۶۷۸۹]{2}:[۰۱۲۳۴۵۶۷۸۹]{2}|)'
PERSIAN_WEEKDAY_NAMES_REGEX = '(%s)' % '|'.join(PERSIAN_WEEKDAY_NAMES.values())
PERSIAN_WEEKDAY_ABBRS_REGEX = '[%s]' % ''.join(PERSIAN_WEEKDAY_ABBRS.values())
PERSIAN_MONTH_NAMES_REGEX = '(%s)' % '|'.join(PERSIAN_MONTH_NAMES.values())
PERSIAN_MONTH_ABBRS_REGEX = '(%s)' % '|'.join(PERSIAN_MONTH_ABBRS.values())
PERSIAN_WEEKDAY_NAMES_ASCII_REGEX = '(%s)' % '|'.join(PERSIAN_WEEKDAY_NAMES_ASCII.values())
PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX = '(%s)' % '|'.join(PERSIAN_WEEKDAY_ABBRS_ASCII.values())
PERSIAN_MONTH_NAMES_ASCII_REGEX = '(%s)' % '|'.join(PERSIAN_MONTH_NAMES_ASCII.values())
PERSIAN_MONTH_ABBRS_ASCII_REGEX = '(%s)' % '|'.join(PERSIAN_MONTH_ABBRS_ASCII.values())
