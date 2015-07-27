#!/bin/bash

set -e


nosetests
cd sphinx
make doctest
make html
make github.io
