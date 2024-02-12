.. _format:

**************
Problem Format
**************

This describes how the solved problem files are organized

:Filename:
    ``src/leetcode/q_XXXX_problem.py``

The ``class`` docstring contains information from leetcode. Each problem
is namespaced under ``SolutionXXXX`` where ``XXXX`` is the number (zero padded).

.. code-block:: python

    class SolutionXXXX:
        """
        `Difficulty <https://leetcode.com/problems/problem/>`_
        ------------------------------------------------

        .. sidebar:: Constraints

            * These are the problem constraints

        This is the problem description from leetcode

        :Example:

        >>> problem(input)
        expected output

        """

The ``def`` (function) docstring contains information about the function used to
solve the problem, and how it was solved.

.. note::

    It is made a ``@staticmethod`` so that it can be called without
    instantiating an object in the doctest examples.

    .. code-block:: python

        >>> SolutionXXXX.statically_defined_method(input)
        output


.. code-block:: python

        @staticmethod
        def problem(params) -> rtype:
            """
            This is the function that solves the problem

            Args:
               These are the function args

            Returns:
               This is what the function returns

            ------

            :Runtime:   ``O(x)``    <- Big-O runtime complexity
            :Space:     ``O(x)``    <- Extra space complexity, not including i/o

            :Strategy:

                This describes how the problem was solved

            """
            pass


Creating Repo Files
===================

Auto
----

``scripts/template_generator/template_generator.py`` generates files for new problems.

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
