Formatting and Parsing directives
=================================

Drived from: `Python's strftime() and strptime() Behavior <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_

JalaliDate directives
---------------------

Latin Glyphs
^^^^^^^^^^^^

=========    ==============================================     ========================================================
Directive    Example                                            Meaning
=========    ==============================================     ========================================================
%a           Sh, Ye, Do, Se, Ch, Pa, Jo                         Locale’s abbreviated weekday name.
%A           Shanbeh, Yekshanbeh                                Locale’s full weekday name.
%w           0, 1, ..., 6                                       Weekday as a decimal number, where 0 is Saturday and 6 is friday.
%d           01, 02, ..., 31                                    Day of the month as a zero-padded decimal number.
%b           Fa, Or, Kh, Ti, Mo, Sh, Me, Ab, Az, De, Ba, Es     Locale’s abbreviated month name.
%B           Farvardin, Tir                                     Locale’s full month name in.
%m           01, 02, ..., 12                                    Month as a zero-padded decimal number.
%y           00, 01, ..., 99                                    Year without century as a zero-padded decimal number.
%Y           0001, 0002, ..., 1394, 1397, ..., 3000             Year with century as a decimal number.
%H           00, 01, ..., 23                                    Hour (24-hour clock) as a zero-padded decimal number.
%I           01, 02, ..., 12                                    Hour (12-hour clock) as a zero-padded decimal number.
%p           AM, PM                                             Locale’s equivalent of either AM or PM.
%M           00, 01, ..., 59                                    Minute as a zero-padded decimal number.
%S           00, 01, ..., 59                                    Second as a zero-padded decimal number.
%f           000000, 000001, ..., 999999                        Microsecond as a decimal number, zero-padded on the left.
%z           (empty), +0000, -0400, +1030                       UTC offset in the form +HHMM or -HHMM (empty string if the object is naive).
%Z           (empty), UTC, TEH                                  Time zone name (empty string if the object is naive).
%j           001, 002, ..., 366                                 Day of the year as a zero-padded decimal number.
***%U           00, 01, ..., 53                                    Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
***%W           00, 01, ..., 53                                    Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
%c           Do Sh 22 22:01:23 1361                             Locale’s appropriate date and time representation.
%x           16/08/1988                                         Locale’s appropriate date representation.
%X           21:30:00                                           Locale’s appropriate time representation.
%%           %                                                  A literal '%' character.
=========    ==============================================     ========================================================



Persian Glyphs
^^^^^^^^^^^^^^

=========    ==============================================     ========================================================
Directive    Example                                            Meaning
=========    ==============================================     ========================================================
%ap          ش, ی, د, س, چ, پ, ج                                Locale’s abbreviated weekday name.
%Ap          شنبه, یکشنبه                                       Locale’s full weekday name.
%wp          ۰, ۱, ..., ۶                                       Weekday as a decimal number, where 0 is Saturday and 6 is friday.
%dp          ۰۱, ۰۲, ..., ۳۱                                    Day of the month as a zero-padded decimal number.
%bp          فر, ار, خر, تی, مر, شه, مه, آب, آذ, دی, به, اس     Locale’s abbreviated month name.
%Bp          فروردین, اردیبهشت                                  Locale’s full month name in.
%mp          ۰۱, ۰۲, ..., ۱۲                                    Month as a zero-padded decimal number.
%yp          ۰۰, ۰۱, ..., ۹۹                                    Year without century as a zero-padded decimal number.
%Yp          ۰۰۰۱, ۰۰۰۲, ..., ۱۳۹۴, ۱۳۹۷, ..., ۳۰۰۰             Year with century as a decimal number.
%Hp          ۰۰, ۰۱, ..., ۲۳                                    Hour (24-hour clock) as a zero-padded decimal number.
%Ip          ۰۱, ۰۲, ..., ۱۲                                    Hour (12-hour clock) as a zero-padded decimal number.
%pp          AM, PM                                             Locale’s equivalent of either AM or PM.
%Mp          ۰۰, ۰۱, ..., ۵۹                                    Minute as a zero-padded decimal number.
%Sp          ۰۰, ۰۱, ..., ۵۹                                    Second as a zero-padded decimal number.
%fp          ۰۰۰۰۰۰, ۰۰۰۰۰۱, ..., ۹۹۹۹۹۹                        Microsecond as a decimal number, zero-padded on the left.
%zp          (empty), +۰۰:۰۰, -۰۴:۰۰, +۱۰:۳۰                    UTC offset in the form +HHMM or -HHMM (empty string if the object is naive).
%Zp          (empty), گرینویچ, تهران                            Time zone name (empty string if the object is naive).
%jp          ۰۰۱, ۰۰۲, ..., ۳۶۶                                 Day of the year as a zero-padded decimal number.
***%Up          ۰۰, ۰۱, ..., ۵۳                                    Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
***%Wp          ۰۰, ۰۱, ..., ۵۳                                    Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
%cp          د شه ۱۵ ۱۰:۰۱:۲۳ ۱۳۶۱                              Locale’s appropriate date and time representation.
%x           ۱۶/۰۸/۱۳۹۵                                         Locale’s appropriate date representation.
%X           21:30:00                                           Locale’s appropriate time representation.


=========    ==============================================     ========================================================

%y           00 - 99                                            Year without century as a zero padded decimal number.
%Y           1 - 3178                                           Year with century as a decimal number.
%n           ۱ - ۹۹                                             Year without century as a decimal number in persian form.
%u           ۰۱ - ۹۹                                            Year without century as a zero padded decimal number in persian form.
%N           ۱ - ۳۱۷۸                                           Year with century as a decimal number in persian form.
%O           ۰۰۰۱ - ۳۱۷۸                                        Year with century as a zero padded decimal number in persian form.
%m           01 - 12                                            Month as a decimal number.
%R           ۱ - ۱۲                                             Month as a decimal number in persian form.
%P           ۰۱ - ۱۲                                            Month as a zero padded decimal number in persian form.

%g           F, O, Kh, T, Mo, ...                               Month name in persian abbreviated ASCII style.
%G           Farvardin, Tir, ...                                Month name in persian ASCII style.

%T           Saturday, Sunday, ..       Weekday name in english ASCII style.
%W           00 - 53                    Week number of the year (SATURDAY as the first day of the week) as a decimal number . All days in a new year preceding the first Monday are considered to be in week 0.
%U           00 - 53                    Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
%d           01 - 31                    Day of the month as a zero padded decimal number in ASCII form.
%K           ۰۱ - ۳۱                    Day of the month as a zero padded decimal number in persian form.
%D           ۱ - ۳۱                     Day of the month as a decimal number in persian form.
%j           001 - 366                  Day of the year as a zero padded decimal number in ASCII form.
%V           ..۱ - ۳۶۶                  Day of the year as a zero padded decimal number in persian form.
%J           ۱ - ۳۶۶                    Day of the year as a decimal number in persian form.
%x           دوشنبه ۱۵ شهریور ۱۳۶۱      Persian appropriate date representation.
%%           %                          A literal '%' character.
=========    =======================    ==============


JalaliDatetime directives
-------------------------


=========    =======================================    ==============
Directive    Example                                    Meaning
=========    =======================================    ==============

=========    =======================================    ==============
%H           00 - 23                                    Hour (24-hour clock) as a zero padded ASCII decimal number.
%k           ۰ - ۲۳                                     Hour (24-hour clock) as a decimal number in persian form.
%h           ۰۰ - ۲۳                                    Hour (24-hour clock) as a zero padded decimal number in persian form.
%I           01 - 12                                    Hour (12-hour clock) as a zero padded ASCII decimal number.
%i           ۰۱ - ۱۲                                    Hour (12-hour clock) as a zero padded decimal number in persian form.
%l           ۱ - ۱۲                                     Hour (12-hour clock) as a decimal number in persian form.
%M           00 - 59                                    Minute as a zero padded ASCII decimal number.
%r           ۰۰ - ۵۹                                    Minute as a zero padded decimal number in persian form.
%v           ۰ - ۵۹                                     Minute as a decimal number in persian form.
%S           00 - 59                                    Second as a zero padded ASCII decimal number.
%s           ۰۰ - ۵۹                                    Second as a zero padded decimal number in persian form.
%L           ۰ - ۵۹                                     Second as a decimal number in persian form.
%f           0 - 999999                                 Microsecond as a zero padded ASCII decimal number.
%F           ۰۰۰۰۰۰ - ۹۹۹۹۹۹                            Microsecond as a zero padded decimal number in persian from.
%p           ق.ظ, ب.ظ                                   AM or PM in persian format.
%t           AM, PM                                     AM or PM in ASCII format.
%z           +04:30                                     UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).
%o           +۰۳:۳۰                                     UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive) in persian format.
%Z           Tehran                                     Time zone name (empty string if the object is naive).
%C           دوشنبه ۱۵ شهریور ۱۳۶۱ ۰۷:۳۴:۰۲ ب.ظ         Persian appropriate date and time representation.
%q           D 15 Sh 61 19:34                           ASCII appropriate short date and time representation.
%Q           Doshanbeh 15 Shahrivar 1361 07:34:02 PM    ASCII Locale’s appropriate date and time representation.
%X           ۰۷:۳۴:۰۲ ب.ظ                               Persian appropriate time representation.
=========    =======================================    ==============


JalaliTimedelta directives
--------------------------


=========    =======================================    ==============
Directive    Example                                    Meaning
=========    =======================================    ==============
%H           0 - ∞                                      Total Hours.
%K           ۱ - ∞                                      Total Hours in persian form.


%h           ۰۰ - ۲۳                                    Hour (24-hour clock) as a zero padded decimal number in persian form.
%I           01 - 12                                    Hour (12-hour clock) as a zero padded ASCII decimal number.
%i           ۰۱ - ۱۲                                    Hour (12-hour clock) as a zero padded decimal number in persian form.
%l           ۱ - ۱۲                                     Hour (12-hour clock) as a decimal number in persian form.
%M           00 - 59                                    Minute as a zero padded ASCII decimal number.
%r           ۰۰ - ۵۹                                    Minute as a zero padded decimal number in persian form.
%v           ۰ - ۵۹                                     Minute as a decimal number in persian form.
%S           00 - 59                                    Second as a zero padded ASCII decimal number.
%s           ۰۰ - ۵۹                                    Second as a zero padded decimal number in persian form.
%L           ۰ - ۵۹                                     Second as a decimal number in persian form.
%f           0 - 999999                                 Microsecond as a zero padded ASCII decimal number.
%F           ۰۰۰۰۰۰ - ۹۹۹۹۹۹                            Microsecond as a zero padded decimal number in persian from.
%p           ق.ظ, ب.ظ                                   AM or PM in persian format.
%t           AM, PM                                     AM or PM in ASCII format.
%z           +04:30                                     UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).
%o           +۰۳:۳۰                                     UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive) in persian format.
%Z           Tehran                                     Time zone name (empty string if the object is naive).
%c           د ۱۵ شه ۶۱ ۰:۰                             Persian appropriate short date and time representation.
%C           دوشنبه ۱۵ شهریور ۱۳۶۱ ۰۷:۳۴:۰۲ ب.ظ         Persian appropriate date and time representation.
%q           D 15 Sh 61 19:34                           ASCII appropriate short date and time representation.
%Q           Doshanbeh 15 Shahrivar 1361 07:34:02 PM    ASCII Locale’s appropriate date and time representation.
%X           ۰۷:۳۴:۰۲ ب.ظ                               Persian appropriate time representation.
=========    =======================================    ==============
a
b
d
e
g
j
k
m
n
u
w
x
y
#
A
B
D
E
G
J
N
O
P
R
T
U
V
W
Y
