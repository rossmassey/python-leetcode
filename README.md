# Python Leetcode Solutions

![Python logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## Requirements

- python (>3.8)
- pip

0. (Optional) Activate venv

    `pip -m venv venv; source venv/bin/activate`

1. Install dependencies
    
    `pip install -r requirements.txt` 

## Start a new problem
`python scripts/template_generator/template_generator.py`

This will autofill a `q_XXXX_title.py` template under `src/leetcode/`

See documentation for how to use

## Testing

#### Doctest
1. `cd docs && make doctest`

#### Run Unit Tests (deprecated)
1. `python3 -m unittest`

`unittest` comes with python

Not using at moment

## Sphinx Documentation

#### Generate Documentation
1. `cd docs && make clean html`
2. `index.html` can be found under `docs/build/html/`

#### Documentation Webserver
1. `python scripts/preview-docs.py`
2. This will run a webserver at http://localhost:8000
3. This also runs doctest

Press `r` to re-build/re-test, and `q` to quit

#### Published Documentation

[![Deploy Documentation](https://github.com/rossmassey/python-leetcode/actions/workflows/gh-pages.yml/badge.svg?branch=main)](https://github.com/rossmassey/python-leetcode/actions/workflows/gh-pages.yml)

The `gh-pages.yml` action builds and publishes the Sphinx docs to GitHub pages

It is accessible at: https://rossmassey.github.io/python-leetcode/
