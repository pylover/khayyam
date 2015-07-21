.. Khayyam documentation master file, created by
   sphinx-quickstart on Mon Jul 20 22:05:40 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Khayyam
=======

The khayyam module supplies classes for manipulating persian dates and times in both
simple and complex ways. While date and time arithmetic is supported, the focus of the
implementation is on efficient attribute extraction for output formatting and manipulation.

Currently both versions of python(2.x & 3.x) are supported.

As of the python's official documentation: There are two kinds of date and time objects:
“naive” and “aware”.

An aware object has sufficient knowledge of applicable algorithmic and political time
adjustments, such as time zone and daylight saving time information, to locate itself
relative to other aware objects. An aware object is used to represent a specific
moment in time that is not open to interpretation.

A naive object does not contain enough information to unambiguously locate itself
relative to other date/time objects. Whether a naive object represents
Coordinated Universal Time (UTC), local time, or time in some other timezone
is purely up to the program, just like it’s up to the program whether a
particular number represents metres, miles, or mass. Naive objects are easy
to understand and to work with, at the cost of ignoring some aspects of reality.

For applications requiring aware objects, :py:class:`khayyam.JalaliDate` and
:py:class:`khayyam.JalaliDatetime` objects have an optional time zone information
attribute, tzinfo, that can be set to an instance of a subclass of the abstract :py:class:`datetime.tzinfo` class, such as :py:class:`khayyam.Timezone` and or :py:class:`khayyam.TehranTimezone`.


The package's API is considered to be exactly the same as the :py:mod:`datetime` module,
so if you are familiar with the :py:mod:`datetime`, you can read the :ref:`migration`.


Contents:
---------

.. toctree::
   :maxdepth: 2

   overview
   migration
   installation
   sourcecode
   development
   persiancalendar
   api


Links:
------

* Python package index: `https://pypi.python.org/pypi/Khayyam <https://pypi.python.org/pypi/Khayyam>`_
* Source code on Github: `https://github.com/pylover/khayyam <https://github.com/pylover/khayyam>`_
* Main Page: `http://vahid.dobisel.com/khayyam/ <http://vahid.dobisel.com/khayyam/>`_


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

