# Python Leetcode Solutions

## Requirements

- python3
- pip

1. `pip install -r requirements.txt` 

## Start a new problem

#### Generate cookies.txt
1. download extension such as https://github.com/hrdl-github/cookies-txt
2. visit `leetcode.com`, click on extension icon, click 'Current site'
3. save Netscape HTTP Cookie File to `scripts/leetcode_api/` named `cookies.txt`


#### Generate new solution template
1. `python3 scripts/template_generator/main.py`
2. this will autofill a `q_XXXX_title.py` template under `src/leetcode/`

TODO: 
- generate unittest file?

## Testing

#### Run Unit Tests
1. `python3 -m unittest`

`unittest` comes with python

#### Doctest
1. `cd docs && make doctest`

## Sphinx Documentation

#### Generate Documentation
1. `cd docs && make clean html`
2. `index.html` can be found under `docs/build/html/`

#### Documentation Webserver
1. `python3 scripts/preview-docs.py`
2. this will run a webserver at http://localhost:8000
3. this also runs doctest

press `r` to re-build/re-test, and `q` to quit

#### Documentation Guide
1. follow format of `q_0001_two_sum` docstring
2. create `docs/source/leetcode/xxxx_problem.rst`
```rst
.. _XXXX_problem:

Problem
-------

.. automodule:: leetcode.q_xxxx_problem
   :members:
```
3. update `neetcode.rst` for link matching rst label `_problem` above
```
:ref:`problem`
```
4. add to toctree directive at bottom of `neetcode.rst`
```
:In Order:

.. toctree::
   :maxdepth: 1

   leetcode/XXXX_problem
```
