# -*- coding: utf-8 -*-

PERSIAN_DIGIT_MAPPING = [
    ((u'\u06f0', u'\u0660'), u'0'),
    ((u'\u06f1', u'\u0661'), u'1'),
    ((u'\u06f2', u'\u0662'), u'2'),
    ((u'\u06f3', u'\u0663'), u'3'),
    ((u'\u06f4', u'\u0664'), u'4'),
    ((u'\u06f5', u'\u0665'), u'5'),
    ((u'\u06f6', u'\u0666'), u'6'),
    ((u'\u06f7', u'\u0667'), u'7'),
    ((u'\u06f8', u'\u0668'), u'8'),
    ((u'\u06f9', u'\u0669'), u'9'),
]



######################
# Parsing & Formatting
######################

PERSIAN_WEEKDAY_NAMES = {
    0: u'شنبه',
    1: u'یکشنبه',
    2: u'دوشنبه',
    3: u'سه شنبه',
    4: u'چهارشنبه',
    5: u'پنجشنبه',
    6: u'جمعه'
}

PERSIAN_WEEKDAY_ABBRS = {
    0: u'ش',
    1: u'ی',
    2: u'د',
    3: u'س',
    4: u'چ',
    5: u'پ',
    6: u'ج'
}

PERSIAN_MONTH_NAMES = {
    1: u'فروردین',
    2: u'اردیبهشت',
    3: u'خرداد',
    4: u'تیر',
    5: u'مرداد',
    6: u'شهریور',
    7: u'مهر',
    8: u'آبان',
    9: u'آذر',
    10: u'دی',
    11: u'بهمن',
    12: u'اسفند'}

PERSIAN_MONTH_ABBRS = {
    1: u'فر',
    2: u'ار',
    3: u'خر',
    4: u'تی',
    5: u'مر',
    6: u'شه',
    7: u'مه',
    8: u'آب',
    9: u'آذ',
    10: u'دی',
    11: u'به',
    12: u'اس'}

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
    0: u'ق.ظ',
    1: u'ب.ظ'
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
AM_PM_REGEX = u'(%s)' % u'|'.join(AM_PM.values())
AM_PM_ASCII_REGEX = '([aA][mM]|[pP][mM])'
HOUR12_REGEX = '(0[1-9]|1[0-2])'
HOUR24_REGEX = '([01]\d|2[0-3])'
MINUTE_REGEX = '([0]?\d|[1-5]\d)'
SECOND_REGEX = '([0]?\d|[1-5]\d)'
MICROSECOND_REGEX = '\d{1,6}'
UTC_OFFSET_FORMAT_REGEX = '([-+]?\d{2}:\d{2}|)'
TZ_NAME_FORMAT_REGEX='.+'

PERSIAN_YEAR_REGEX = u'[۰۱۲۳۴۵۶۷۸۹]{1,4}' # TODO: Remove zero-padding
PERSIAN_YEAR_ZERO_PADDED_REGEX = u'[۰۱۲۳۴۵۶۷۸۹]{1,4}'
PERSIAN_SHORT_YEAR_REGEX = u'(۰|[۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]?)'
PERSIAN_SHORT_YEAR_ZERO_PADDED_REGEX = u'[۰۱۲۳۴۵۶۷۸۹]{1,2}'
PERSIAN_MONTH_REGEX = u'([۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_MONTH_ZERO_PADDED_REGEX = u'(۰[۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_DAY_REGEX = u'([۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]|۳[۰۱])' # ۱-۳۱
PERSIAN_DAY_ZERO_PADDED_REGEX = u'(۰[۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]|۳[۰۱])' # ۰۱-۳۱
PERSIAN_DAY_OF_YEAR_REGEX = u'([۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]{2}|۳[۰۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹]|۳۶[۰۱۲۳۴۵۶])' # ۱-۳۶۶
PERSIAN_DAY_OF_YEAR_ZERO_PADDED_REGEX = u'(۰۰[۱۲۳۴۵۶۷۸۹]|۰[۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]|[۱۲][۰۱۲۳۴۵۶۷۸۹]{2}|۳[۰۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹]|۳۶[۰۱۲۳۴۵۶])' # ۰۰۱-۳۶۶
PERSIAN_HOUR12_REGEX = u'([۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_HOUR12_ZERO_PADDED_REGEX = u'(۰[۱۲۳۴۵۶۷۸۹]|۱[۰۱۲])'
PERSIAN_HOUR24_REGEX = u'([۰۱۲۳۴۵۶۷۸۹]|۱[۰۱۲۳۴۵۶۷۸۹]|۲[۰۱۲۳])'
PERSIAN_HOUR24_ZERO_PADDED_REGEX = u'(۰[۰۱۲۳۴۵۶۷۸۹]|۱[۰۱۲۳۴۵۶۷۸۹]|۲[۰۱۲۳])'

PERSIAN_MINUTE_REGEX = u'([۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'
PERSIAN_MINUTE_ZERO_PADDED_REGEX = u'(۰[۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'

PERSIAN_SECOND_REGEX = u'([۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'
PERSIAN_SECOND_ZERO_PADDED_REGEX = u'(۰[۰۱۲۳۴۵۶۷۸۹]|[۱۲۳۴۵][۰۱۲۳۴۵۶۷۸۹])'

PERSIAN_MICROSECOND_REGEX = u'[۰۱۲۳۴۵۶۷۸۹]{1,6}'
PERSIAN_UTC_OFFSET_FORMAT_REGEX = u'([-+]?[۰۱۲۳۴۵۶۷۸۹]{2}:[۰۱۲۳۴۵۶۷۸۹]{2}|)'
PERSIAN_WEEKDAY_NAMES_REGEX = u'(%s)' % '|'.join(PERSIAN_WEEKDAY_NAMES.values())
PERSIAN_WEEKDAY_ABBRS_REGEX = u'[%s]' % ''.join(PERSIAN_WEEKDAY_ABBRS.values())
PERSIAN_MONTH_NAMES_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_NAMES.values())
PERSIAN_MONTH_ABBRS_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_ABBRS.values())
PERSIAN_WEEKDAY_NAMES_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_WEEKDAY_NAMES_ASCII.values())
PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_WEEKDAY_ABBRS_ASCII.values())
PERSIAN_MONTH_NAMES_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_NAMES_ASCII.values())
PERSIAN_MONTH_ABBRS_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_ABBRS_ASCII.values())
