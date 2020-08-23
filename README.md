lagoon-python
=============

[![PyPI version](https://badge.fury.io/py/lagoon-python.svg)](http://badge.fury.io/py/lagoon-python)

[lagoon-python](https://github.com/rrajaravi/lagoon-python) is the official Python client for [lagoon](https://github.com/sourcepirate/lagoon), aAn inmemory and highly concurrent bloom filter service based on json-rpc.

### Installation

lagoon-python supports:

- Python (3.5, 3.6, 3.7, 3.8)

#### Install from Pypi

```bash
pip install lagoon-python
```

### Usage

```python

# Create a new client
import lagoon
client = lagoon.connect('YOUR_LAGOON_HOSTNAME', 'LAGOON_SERVICE_PORT')

# Create a collection
collection1 = client.create_collection("collection1")

# create a key in the collection
client.set_key("collection1", "key1")

# check if a key exist in the collection
client.has_key("collection1", "key1")

# delete collection
client.delete_collection("collection1")
```

### Contributing

First, make sure you can run the test suite. Tests are run via py.test

Install test requirements

```bash
pip install .[test]

py.test
# with coverage
py.test --cov lagoon --cov-report html
# with setuppy
python setup.py test
# lint with setup.py
python setup.py lint 
# check lint
python setup.py lint --check
```

Install black and flake8

```
pip install .[ci]
```

Install git hooks to avoid pushing invalid code (git commit will run `black` and `flake8`)

### Releasing a new version

In order to release new version you need to be a maintainer on Pypi.

- Update CHANGELOG
- Update the version on setup.py
- Commit and push to Github
- Create a new tag for the version (eg. `v1.1.0`)
- Create a new dist with python `python setup.py sdist`
- Upload the new distributable with twine `twine upload dist/lagoon-python-VERSION-NAME.tar.gz`

If unsure you can also test using the Pypi test servers `twine upload --repository-url https://test.pypi.org/legacy/ dist/lagoon-python-VERSION-NAME.tar.gz`
