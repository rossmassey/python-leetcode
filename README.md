#### Run Tests

python3 -m unittest discover -s tests

#### Generate Documentation
1. `make html`

#### Documentation Guide

1. follow format of two sum docstring
2. create `doc/source/leetcode/xxxx_problem.rst`
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

Automate documentation generation
