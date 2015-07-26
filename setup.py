# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

__author__ = 'vahid'

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'khayyam', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

# try:
#     from pypandoc import convert
#     read_md = lambda f: convert(f, 'rst')
# except ImportError:
#     print("warning: pypandoc module not found, could not convert Markdown to RST")
#     read_md = lambda f: open(f, 'r').read()


setup(
    name="Khayyam",
    version=package_version,
    packages=find_packages(),
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://khayyam.dobisel.com",
    description="Persian(Jalali) date and time library",
    zip_safe=True,
    keywords="Khayyam persian jalali date time datetime conversion",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    license="GPLv3",
    test_suite="khayyam.tests",
    tests_require=[
        'rtl'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Intended Audience :: Developers",
        "Natural Language :: Persian",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"],
)
