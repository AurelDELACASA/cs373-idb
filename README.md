SmashDB

### Build Status

[![Master Build Status](https://travis-ci.org/lee-benjamin/cs373-idb.svg?branch=master)](https://travis-ci.org/lee-benjamin/cs373-idb)

[![dev Build Status](https://travis-ci.org/lee-benjamin/cs373-idb.svg?branch=dev)](https://travis-ci.org/lee-benjamin/cs373-idb)

### Dependencies

* python3.5
* pip3

pip packages:

* virtualenv
* flask

### Deployment

Install necessary dependencies, then run `make start-server` from the root directory of the repo.

When using an apache-less environment, bind `app.py` to port 80 and change `app.js` to make API calls with `/api/path` instead of `http://localhost/api/path`
