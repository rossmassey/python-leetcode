*******
Testing
*******

Doctest
=======

.. _Doctest: https://docs.python.org/3/library/doctest.html

`Doctest`_ is the preferred testing method. They are the ``>>>`` snippets in
docstring. They are ran and compared with the line below.

.. code-block:: python

    >>> 2 + 2
    4

To run doctest, enter the ``docs/`` folder and run ``make doctest``. It will
write the output to stdout and and ``docs/build/doctest/output.txt``

:Example summary:

    (At the bottom of ``output.txt``)

.. code-block:: none

    Doctest summary
    ===============
        9 tests
        0 failures in tests
        0 failures in setup code
        0 failures in cleanup code

GitHub Action
-------------

.. image:: https://github.com/rossmassey/python-leetcode/actions/workflows/doctest.yml/badge.svg
    :target: https://github.com/rossmassey/python-leetcode/actions/workflows/doctest.yml


The ``.github/workflows/doctest.yml`` action will run Doctest when there is a
push to the repo. It can also ran by clicking **Run workflow** within GitHub.

The ``output.txt`` results are uploaded as a workflow artifact and can be viewed
on GitHub.
