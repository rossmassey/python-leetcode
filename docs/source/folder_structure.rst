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

.. _reStructuredText: https://docutils.sourceforge.io/rst.html

This is where the Sphinx `reStructuredText`_ and configuration files are.

:🎨 _static/css/custom.css:
    custom CSS styles for this documentation

:⚙️ conf.py:
    where the Sphinx configuration and metadata is.

:📁 leetcode/:
    used for the automodule ``.rst`` files (imports to create documentation)

:📄 *.rst:
    these are articles containing ``toctree`` directives and information

See :ref:`documentation-guide` for more info

requirements.txt
================

This lists the dependencies of this repo to be installed by pip.

.. warning::
    It is recommended to isolate your environment using a tool like ``venv``

scripts/
========

This is where scripts for managing this repo are.

:✍️ template_generator/:
    will auto create solution and doc files for a given problem by fetching
    info from leetcode

:🔍 preview_docs.py:
    will start a local server for previewing the Sphinx docs.

src/
====

This is where the solved problems are

:📁 common/:
    modules with common leetcode classes shared among problems

:📁 leetcode/:
    modules containing solution classes/functions

See :ref:`format` for more info

tests/ (``Deprecated``)
=======================

This is where unittests for the solved leetcode problems are.

Doctest seems like better choice, so this is unused for now.
