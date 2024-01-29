.. _documentation-guide:

**************************
How documentation is built
**************************

.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _Google Style Guide: https://google.github.io/styleguide/pyguide.html#383-functions-and-methods

Documentation is located under the ``docs/`` folder

It is built with `Sphinx`_

**Class** level documentation details problem information, overview, constraints,
and examples (that can be tested wtih ``doctest``)

**Function** level documentation details function information as well as notes on
which strategy was employed and the time/space complexity

Docstring Args/Returns format follows the `Google Style Guide`_


Building Docs
^^^^^^^^^^^^^
Under the `docs/` folder, run the following:

    * ``make clean`` - removes old build
    * ``make html`` - generates html version of documentation
    * ``make doctest`` - runs ``doctest`` to evaluate ``>>>`` examples

``scripts/template_generator/preview-docs.py`` will clean and build the HTMl
documentation, as well as evaluate the example tests

It will start a web server that can accessed at http://localhost:8000

Automated Doc Generation
^^^^^^^^^^^^^^^^^^^^^^^^
``scripts/template_generator/main.py`` generates docstring for new problems

It also

    * creates ``docs/source/leetocode/XXXX_problem.rst`` for ``automodule``
    * updates ``docs/source/neetcode.rst`` references

See :ref:`Template Generator Documentation <template-generator-doc>` for more information

Manual Guide
^^^^^^^^^^^^

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

