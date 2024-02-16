.. _complexity:

***************************
Complexity Reference [#f1]_
***************************

Complexity Classes
==================

:``O(1)``:

    Does not depend on the input size

:``O(log n)``:

    **Logarithmic**, often halves the input size at each step

:``O(sqrt(n))``:

    **Square root**, note ``sqrt(n) = n / sqrt(n)``, so it is around middle of
    input

:``O(n)``:

    **Linear**, usually necessary to access each input element at least once

:``O(n log n)``:

    This often indicates sorting, or a data structure where each operation takes
    ``O(log n)``

:``O(n^2)``:

    **Quadratic**, often two nested loops

:``O(n^3)``:

    **Cubic**, often three nested loops

:``O(2^n)``:

    **Exponential**, often indicates the algorithm iterates through subsets

:``O(n!)``:

    **Factorial**, often indicates the algorithm iterates through all
    permutations of the input elements


Estimating Efficiency
=====================

.. csv-table::
   :widths: 10, 30
   :header-rows: 1

    "input Size", "required time complexity"
    "``n <= 10``", "``O(n!)``"
    "``n <= 20``", "``O(2^n)``"
    "``n <= 500``", "``O(n^3)``"
    "``n <= 5000``", "``O(n^2)``"
    "``n <= 10^6``", "``O(n log n)`` or ``O(n)``"
    "``n is large``", "``O(1)`` or ``O(log n)``"

.. rubric:: Footnotes

.. [#f1] Adapted from: Laaksonen, A. (2018). `Competitive Programmer's Handbook`. Helsinki.
