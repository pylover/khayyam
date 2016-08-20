#!/usr/bin/env bash
set -e # Exit with nonzero exit code if anything fails

# Save some useful information
REPO=`git config remote.origin.url`
SHA=`git rev-parse --verify HEAD`

# Get the deploy key by using Travis's stored variables to decrypt deploy_key.enc
ENCRYPTED_KEY_VAR="encrypted_${ENCRYPTION_LABEL}_key"
ENCRYPTED_IV_VAR="encrypted_${ENCRYPTION_LABEL}_iv"
ENCRYPTED_KEY=${!ENCRYPTED_KEY_VAR}
ENCRYPTED_IV=${!ENCRYPTED_IV_VAR}
OUT_KEY="khayyam-travis-gh-pages"

openssl aes-256-cbc -K $ENCRYPTED_KEY -iv $ENCRYPTED_IV -in khayyam-travis-gh-pages.enc -out $OUT_KEY -d
chmod 600 $OUT_KEY
eval `ssh-agent -s`
ssh-add $OUT_KEY


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
git config user.name "Travis CI"
git config user.email "$COMMIT_AUTHOR_EMAIL"


git commit -am "Deploy to GitHub Pages: ${SHA}"
git --work-tree=./../../khayyam.io --git-dir=./../../khayyam.io/.git push origin gh-pages
