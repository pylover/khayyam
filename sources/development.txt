Development & Contribution
==========================

At first, any contribution is appreciated.


Please provide the full black-box & white-box test cases, and pass all tests in the `khayyam/test` directory
for both versions of python before supplying any pull-request.


Making development environment::

  $ cd workspace
  $ git clone <Your fork Url>
  $ cd khayyam
  $ pip install -e .


Do some changes and make a pull request.

Testing
^^^^^^^

Install nose::

  $ pip install nose
  $ cd path/to/khayyam
  $ nosetests

Without nose::

  $ cd path/to/khayyam
  $ python tests/test_jalali_date.py
  $ python tests/test_jalali_datetime.py
  $ python tests/test_teh_tz.py


Document authoring
^^^^^^^^^^^^^^^^^^

Clone/checkout the `gh-pages` branch from Github alongside the master branch working copy directory ::

  $ cd path/to/khayyam
  $ cd ..
  $ git clone -b gh-pages <Your fork url>

Build Documents::

  $ cd path/to/khayyam/sphinx
  $ make html

Or watch for changes::

  $ apt-get install inotify-tools
  $ ./watch


Start the document http server locally::

  $ gem install jekyll
  $ cd path/to/khayyam.io
  $ jekyll serve -w

And then browse the `http://127.0.0.1:4000/ <http://127.0.0.1:4000/>`_.
