Formatting and Parsing directives
=================================

JalaliDate directives
---------------------

=========    =======================    ==============
Directive    Example                    Meaning
=========    =======================    ==============
%y           00 - 99                    Year without century as a zero padded decimal number.
%Y           1 - 3178                   Year with century as a decimal number.
%n           ۱ - ۹۹                     Year without century as a decimal number in persian form.
%u           ۰۱ - ۹۹                    Year without century as a zero padded decimal number in persian form.
%N           ۱ - ۳۱۷۸                   Year with century as a decimal number in persian form.
%O           ۰۰۰۱ - ۳۱۷۸                Year with century as a zero padded decimal number in persian form.
%m           01 - 12                    Month as a decimal number.
%R           ۱ - ۱۲                     Month as a decimal number in persian form.
%P           ۰۱ - ۱۲                    Month as a zero padded decimal number in persian form.
%b           فر, ار, خر, تی, ...        Month name in persian abbreviated style.
%B           فروردین, اردیبهشت, ...     Month name in persian.
%g           F, O, Kh, T, Mo, ...       Month name in persian abbreviated ASCII style.
%G           Farvardin, Tir, ...        Month name in persian ASCII style.
%a           ش, ی, د, ...               Weekday name in persian abbreviated style.
%e           Sh, Y, D, Se, Ch, P, J     Weekday name in persian abbreviated ASCII style.
%A           شنبه, یکشنبه, ...          Weekday name in persian.
%E           Shanbeh, Yekshanbeh, ..    Weekday name in persian ASCII style.
%w           0(Saturday), 6(Friday)     Weekday as a decimal number.
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
%H           00 - 23                                    Hour (24-hour clock) as a zero padded ASCII decimal number.
%k           ۱ - ۲۳                                     Hour (24-hour clock) as a decimal number in persian form.
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