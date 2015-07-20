khayyam
=======

Jalali Date and Time types and algorithms for Python2 and Python3.

To Do
----------

  * API-Doc
  * Constructors act as converter: `JalaliDate(date)`
  * Create TehranDatetime object
  * Show weekday in __repr__
  * Add two methods: d.next(SATURDAY) & d.previous(WEDNESDAY)
  * Alphabetical number format
  * Naming conventions
  * setup.py pure python fallback switch
  * Use compiled regex if matters in performance
  * Readme:
    * Installation: (PYPI, Development version)
    * Testing
    * Parsing
    * Formatting
    * Conversions
    * Operators
    * Compatibility
    * Contribution
  

Change Log
----------

  * 2.0.0-alpha (2015-07-19) Incompatible with < 2.0.0
    * JalaliDate: method `localformat` renamed to `localdateformat`.
    * JalaliDatetime: method `localformat` renamed to `localdatetimeformat`.
    * JalaliDatetime: method `localshortformat_ascii` renamed to `localshortformatascii`.
    * JalaliDatetime: method `localdatetimeformat_ascii` renamed to `localdatetimeformatascii`.
    * JalaliDatetime: method `ampm_ascii` renamed to `ampmascii`.
    * JalaliDatetime: Migrating to New Formatter/Parser Engine
    * TehTz: renamed to TehranTimezone
    * Comparison and Timezones
    * Comparison with `datetime.date` & `datetime.datetime`
    * Fixing timezone bug
    
  * 1.1.0 (2015-07-17)
    * JalaliDate: New Formatter/Parser & full unittests.
    