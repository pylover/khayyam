Installation
============

Prerequisites
-------------

At first, you have to install cython, it's mandatory for build the c extension:

.. code-block:: console

  $ pip install cython

Of course if cython was not available, any preferred C compiler is enough to
build the included C source codes, for example: GCC, Visual C++, Cygwin & etc ... ::

Debian

.. code-block:: console

  $ apt-get install build-essential

And python 2 headers:

.. code-block:: console

  $ apt-get install python-dev

Or, python 3 headers:

.. code-block:: console

  $ apt-get install python3-dev

For windows , you have to install Microsoft Visual Studio, see:
  `here <http://www.clemens-sielaff.com/building-python-3-on-windows-with-visual-studio-express/>`_,
  `here <https://www.microsoft.com/en-us/download/details.aspx?id=44266>`_
  and
  `here <http://www.falatic.com/index.php/120/a-guide-to-building-python-2-x-and-3-x-extensions-for-windows>`_.


From PyPI
---------

pip:

.. code-block:: console

  $ pip install cython
  $ pip install khayyam

Specific version:

.. code-block:: console

  $ pip install "khayyam>=2.0.0"

easy_install:

.. code-block:: console

  $ easy_install khayyam


From Source
-----------

.. code-block:: console

  $ cd path/to/source/directory
  $ pip install .

or:

.. code-block:: console

  $ python setup.py install

You may use the source folder in-place as a python library in `sys.path`, so you have to
build the C extensions before using the library:

.. code-block:: console

  $ cd path/to/source/directory
  $ python setup.py build_ext --inplace


Development, editable:

.. code-block:: console

  $ cd path/to/source/directory
  $ python setup.py build_ext --inplace
  $ nosetests
  $ pip install -e .


From Github
-----------
Latest development code:

.. code-block:: console

  $ pip install cython
  $ pip install git+https://github.com/pylover/khayyam.git