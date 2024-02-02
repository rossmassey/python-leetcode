.. _documentation-guide:

**************************
How documentation is built
**************************

.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _Google Style Guide: https://google.github.io/styleguide/pyguide.html#383-functions-and-methods

Documentation is located under the ``docs/source/`` folder. It is built with `Sphinx`_.

.. note::

    For the docstrings on ``src/leetcode/`` solved problems:

    :Class docstring:

        * problem title
        * description
        * overview
        * constraints
        * examples

    :Function docstring:

        * function information
        * time/space complexity
        * notes on which strategy was used

Docstring Args/Returns format follows the `Google Style Guide`_.

Doctest
=======

Doctest are testable ``>>>`` examples in the docstring.

See :ref:`testing`

Doc Configuration
=================

Sphinx configuration is done in ``docs/source/conf.py``.

This includes metadata, extensions, python src location, and other options.


Building Docs
=============

Under the `docs/` folder, run the following:

    * ``make clean`` - removes old build
    * ``make html`` - generates html version of documentation
    * ``make doctest`` - runs ``doctest``

``scripts/template_generator/preview-docs.py`` also rebuilds the HTML
documentation, as well as evaluates the doctest.

It will start a web server that can accessed at http://localhost:8000

GitHub Action
-------------

.. image:: https://github.com/rossmassey/python-leetcode/actions/workflows/gh-pages.yml/badge.svg
    :target: https://github.com/rossmassey/python-leetcode/actions/workflows/gh-pages.yml

The ``.github/workflows/gh-pages.yml`` action will run build these docs and
publish them to GitHub pages. It can also ran by clicking **Run workflow**
within GitHub.

