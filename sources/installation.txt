Installation
============

Prerequisites
-------------


Debian

.. code-block:: console

  $ apt-get install build-essential

And python 2 headers:

.. code-block:: console

  $ apt-get install python-dev

Or, python 3 headers:

.. code-block:: console

  $ apt-get install python3-dev

For windows , you have to install Microsoft Visual Studio or C++ build tools, see:

 * `Python Windows Compilers <https://wiki.python.org/moin/WindowsCompilers>`_
 * `Building Python 3 on Windows with Visual Studio Express <http://www.clemens-sielaff.com/building-python-3-on-windows-with-visual-studio-express>`_,
 * `Microsoft Visual C++ Compiler for Python 2.7 <https://www.microsoft.com/en-us/download/details.aspx?id=44266>`_
 * `A Guide to Building Python 2.x and 3.x Extensions for Windows <http://www.falatic.com/index.php/120/a-guide-to-building-python-2-x-and-3-x-extensions-for-windows>`_.


From PyPI
---------

pip:

.. code-block:: console

  $ pip install khayyam

Specific version:

.. code-block:: console

  $ pip install "khayyam>=2.9.6"

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

  $ pip install git+https://github.com/pylover/khayyam.git