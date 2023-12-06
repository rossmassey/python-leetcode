#### Run Tests

python3 -m unittest discover -s tests

#### Generate Documentation
1. `make html`
2. `index.html` can be found under `docs/build/html/`

#### Preview Documentation Script
1. `python3 scripts/preview-docs.py`
2. this will run a webserver at http://localhost:8000

#### Documentation Guide
1. follow format of two sum docstring
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
4. add to toc at bottom of `neetcode.rst`
```
:In Order:

.. toctree::
   :maxdepth: 1
    ...
   leetcode/XXXX_problem 
```
#### TODO

- Automate documentation generation
- Automate solution/test case generation
- Add these instructions to documentations
