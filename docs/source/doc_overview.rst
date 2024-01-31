.. _documentation-guide:

**************************
How documentation is built
**************************

.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _Google Style Guide: https://google.github.io/styleguide/pyguide.html#383-functions-and-methods

Documentation is located under the ``docs/`` folder. It is built with `Sphinx`_.

.. note::

    For the documentation on ``src/leetcode/`` solved problems:

    :Class docstring:

    * details problem information, overview, constraints, and examples

    :Function docstring:

    * details function information, notes on which strategy was used, and the time/space complexity

Docstring Args/Returns format follows the `Google Style Guide`_.

Doctest
=======

Doctest are testable ``>>>`` examples in the docstring. Compares the output of
the ``>>>`` line with the line below it.

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

Writing Problem Docs
====================

Auto
----

``scripts/template_generator/main.py`` generates docstring for new problems.

It also

    * creates ``docs/source/leetocode/XXXX_problem.rst`` for ``automodule``
    * updates ``docs/source/neetcode.rst`` references

See :ref:`Template Generator Documentation <template-generator-doc>` for more
information.

Manual
------

#. Follow the format of ``q_0001_two_sum`` for docstring and module comment.
#. Create ``docs/source/leetcode/xxxx_problem.rst`` with following content:

    .. code-block:: rst

        .. _XXXX_problem:

        Problem
        -------

        .. automodule:: leetcode.q_xxxx_problem
           :members:

#. Replace ``XXXX - Title`` with ``:ref:`_XXXX_problem``` in ``neetcode.rst``
#. Add import to the ``toctree`` directive at the bottom of ``neetcode.rst``.

   .. code-block:: rst

        :In Order:

        .. toctree::
           :maxdepth: 1

           leetcode/XXXX_problem  <- add
