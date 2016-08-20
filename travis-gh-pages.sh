#!/usr/bin/env bash

# Clone/checkout the gh-pages branch from Github alongside the master branch working copy directory :
cd ..
git clone -b gh-pages git@github.com:pylover/khayyam.git khayyam.io

# Build in-project documents: docs/html
cd khayyam/sphinx
make html

# Build khayyam.io documents: ../../khayyam.io
make khayyam.io

# Commit & push
cd ../../khayyam.io/
git commit -am "From travis #$TRAVIS_JOB_ID"
git push origin gh-pages
