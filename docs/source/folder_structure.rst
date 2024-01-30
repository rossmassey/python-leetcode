.. _folder_structure:

**************
Repo Structure
**************

.. code-block:: none

    .
    ├── README.md
    ├── docs/
    │   └── source/                     # sphinx doc source
    │       ├── _static/
    │       ├── _leetcode/
    |       ├── conf.py
    |       └── ...
    ├── requirements.txt
    ├── scripts/                        # useful scripts
    │   ├── preview_docs.py
    │   └── template_generator/
    ├── src/
    │   ├── common/                     # leetcode provided classes
    │   └── leetcode/                   # solved problems
    │       ├── q_0001_two_sum.py
    │       └── ...
    └── tests/
        └── leetcode/
            ├── test_0001_two_sum.py
            └── ...


README.md
=========

This contains information on the code repository and instructions for setting
it up.

docs/source/
============

This is where the Sphinx ``.rst`` and configuration files are.

``_static/`` contains custom ``.css`` file, ``leetcode/`` is used for the
automodule ``.rst`` files, and ``conf.py`` is where the Sphinx configuration
and metadata is.

requirements.txt
================

This lists the dependencies of this repo to be installed by pip.

It is recommended to isolate your environment using a tool like ``venv``.

scripts/
========

This is where scripts for managing this repo are.

``preview_docs.py`` will start a local server for previewing the Sphinx docs.

``template_generator/`` package will auto create solution and doc files for a
given problem.

src/
====

This is where the solved leetcode problems are, as well as leetcode provided
classes (such as ``ListNode``).

Each problem is in a file named ``q_num_title.py``, and contains
related problem info and doctest examples. They are contained in a ``class``
matching leetcode, but named ``Solution<num>`` instead of ``Solution``.

Docstrings are used in the Sphinx doc, which also evaluates doctest (``>>>``)
and reports results.

tests/
======

This is where unittests for the solved leetcode problems are.

Doctest seems like better choice, so this is unused for now.
