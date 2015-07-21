Introduction
============

Basic Usage
-----------

Importing
^^^^^^^^^
::

  from khayyam import *

This will imports
:py:class:`khayyam.JalaliDate`,
:py:class:`khayyam.JalaliDatetime`,
:py:class:`khayyam.Timezone`,
:py:class:`khayyam.TehranTimezone`,
:py:obj:`khayyam.constants.MINYEAR`,
:py:obj:`khayyam.constants.MAXYEAR`,
:py:obj:`khayyam.constants.SATURDAY`,
:py:obj:`khayyam.constants.SUNDAY`,
:py:obj:`khayyam.constants.MONDAY`,
:py:obj:`khayyam.constants.THURSDAY`,
:py:obj:`khayyam.constants.WEDNESDAY`
:py:obj:`khayyam.constants.TUESDAY`
:py:obj:`khayyam.constants.FRIDAY`


Current date and time
^^^^^^^^^^^^^^^^^^^^^

::

  >>> JalaliDatetime.now()
  khayyam.JalaliDatetime(1394, 4, 30, 20, 49, 55, 205834, Seshanbeh)

  >>> print(JalaliDatetime.now())
  1394-04-30 20:56:20.991585

DST aware::

  >>> print(JalaliDatetime.now(TehranTimezone()))
  1394-04-30 19:59:12.935506+04:30

  >>> print(JalaliDatetime.now(TehranTimezone()) - timedelta(days=6*30))
  1393-11-02 20:01:11.663719+03:30

As you see, the DST offset in the second statement is `+3:30`. so
the :py:class:`khayyam.TehranTimezone` is supporting `daylight saving time` properly.

Today::

  >>> JalaliDate.today()
  khayyam.JalaliDate(1394, 4, 30, Seshanbeh)

  >>> print(JalaliDate.today())
  1394-4-30

Formatting
^^^^^^^^^^

All format directives which supported by python's native :ref:`strftime-strptime-behavior` are supported by this library, plus:

* `%g`
* `%G`




Overview
========


To convert a jalali datetime to python's standard datetime::

   In [1]: import khayyam

   In [2]: khayyam.JalaliDatetime.now().to_datetime()
   Out[2]: datetime.datetime(2012, 4, 14, 1, 21, 8, 842241)

   In [3]: khayyam.JalaliDate.today().to_date()
   Out[3]: datetime.date(2012, 4, 14)

To create jalali datetime from python's standard datetime::

   In [1]: import khayyam,datetime

   In [2]: now = datetime.datetime.now()

   In [3]: jalali_now = khayyam.JalaliDatetime.from_datetime(now)

   In [4]: print jalali_now
   1391-1-26T1:31:10.34972

To format you can use the native python's `datetime.strftime`_ function::

   In [1]: import khayyam

   In [2]: now = khayyam.JalaliDatetime.now()

   In [3]: print now.strftime("%Y-%m-%d %H:%M:%S")
   1391-1-26 1:26:28

   In [4]: print now.strftime("%C")
   شنبه 26 فروردین 1391 1:26:28 ق.ظ

   In [5]: print now.strftime("%c")
   ش 26 فر 91 1:26

Using timezone::

   In [1]: import khayyam

   In [2]: now = khayyam.JalaliDatetime.now(khayyam.teh_tz)

   In [3]: now
   Out[3]: khayyam.JalaliDatetime(1391, 1, 26, 1, 32, 49, 108209, tzinfo=<khayyam.tehran_timezone.TehTz object at 0x8a6812c>)

   In [4]: now.dst()
   Out[4]: datetime.timedelta(0, 3600)

   In [5]: now.tzinfo
   Out[5]: <khayyam.tehran_timezone.TehTz object at 0x8a6812c>


.. _datetime.strftime: http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior