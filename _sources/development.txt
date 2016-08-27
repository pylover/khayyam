Development & Contribution
==========================

At first, any contribution is appreciated.


Please provide the full black-box & white-box test cases, and pass all tests in the `khayyam/test` directory
for both versions of python before supplying any pull-request.


Making development environment:

.. code-block:: console

  $ cd workspace
  $ git clone <Your fork Url>
  $ cd khayyam
  $ python setup.py build_ext --inplace
  $ pip install -e .


Do some changes and make a pull request.

Testing
^^^^^^^

Testing source codes:
"""""""""""""""""""""

Install nose:

.. code-block:: console

  $ pip install nose
  $ cd path/to/khayyam
  $ nosetests
  .............................
  ----------------------------------------------------------------------
  Ran 29 tests in 1.565s

  OK


Without nose:

.. code-block:: console

  $ cd path/to/khayyam
  $ python setup.py test
  running test
  running egg_info
  writing Khayyam.egg-info/PKG-INFO
  writing top-level names to Khayyam.egg-info/top_level.txt
  writing dependency_links to Khayyam.egg-info/dependency_links.txt
  reading manifest file 'Khayyam.egg-info/SOURCES.txt'
  reading manifest template 'MANIFEST.in'
  writing manifest file 'Khayyam.egg-info/SOURCES.txt'
  running build_ext
  test_dst (khayyam.tests.test_teh_tz.TestTehTz) ... ok
  test_add (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_algorithm (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_iso_format (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_lt_gt_le_ge_ne_eg (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_now (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_replace (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_repr (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_strftime_strptime (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_sub (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_to_from_datetime (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_today (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_utcnow (khayyam.tests.test_jalali_datetime.TestJalaliDateTime) ... ok
  test_add (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_algorithm (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_days_in_month (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_instantiate (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_is_leap (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_iso_calendar (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_iso_format (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_lt_gt_le_ge_ne_eg (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_ordinal (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_replace (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_repr (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_strftime (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_strptime (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_sub (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_to_from_date (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok
  test_to_from_julian_day (khayyam.tests.test_jalali_date.TestJalaliDate) ... ok

  ----------------------------------------------------------------------
  Ran 29 tests in 1.665s

  OK


Document authoring
^^^^^^^^^^^^^^^^^^

Clone/checkout the `gh-pages` branch from Github alongside the master branch working copy directory :

.. code-block:: console

  $ cd path/to/khayyam
  $ cd ..
  $ git clone -b gh-pages <Your fork url> khayyam.io

Build in-project documents: `docs/html`

.. code-block:: console

  $ cd path/to/khayyam/sphinx
  $ make html

Build `khayyam.io` documents: `../../khayyam.io`

.. code-block:: console

  $ cd path/to/khayyam/sphinx
  $ make khayyam.io


Or watch for changes:

.. code-block:: console

  $ apt-get install inotify-tools
  $ ./watch


Start the document http server locally:

.. code-block:: console

  $ gem install jekyll
  $ cd path/to/khayyam.io
  $ jekyll serve -w

And then browse the `http://127.0.0.1:4000/ <http://127.0.0.1:4000/>`_.

Testing document code snippets:
"""""""""""""""""""""""""""""""

Install required packages:

.. code-block:: console

  $ pip install rtl
  $ cd path/to/khayyam/sphinx
  $ make doctest
