'''
Created on Jan 15, 2011

@author: vahid
'''
import os
from setuptools import setup, find_packages
import re

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__),'khayyam3', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'",re.S).match(v_file.read()).group(1)


setup(
    name="Khayyam3",
    version=package_version,
    packages=find_packages(),
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="https://github.com/183amir/khayyam3",
    description="Khayyam3(Jalali Persian Datetime) library. This is fork of the original khayyam library which supports both Python 2.6 above and Python 3. The original Khayyam library is available at: https://pypi.python.org/pypi/Khayyam",
    zip_safe=True,
    keywords="Khayyam3 Khayyam persian jalali date time datetime conversion",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: Freeware",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"],
    use_2to3=True
)
