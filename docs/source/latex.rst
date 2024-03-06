.. _latex:

*************
LaTeX Support
*************

.. _MathJax: https://www.mathjax.org/

:math:`\LaTeX{}` support is provided by the ``sphinx.ext.mathjax`` extension.

This keeps the LaTeX syntax in the HTML file, and uses the JavaScript package
`MathJax`_ to render in the browser.

.. note::

    For LaTeX in Python docstrings, either a raw string (``r""" ... """``)
    must be used or the slashes (``\``) must be escaped (``\\``)

Inline math
-----------

.. code-block:: latex

    Euler's identity is the equality :math:`e^{i\pi} = -1`


Euler's identity is the equality :math:`e^{i\pi} = -1`

Multiline math
--------------

.. code-block:: latex

    .. math::

        \begin{align*}
                            & \textbf{Mean Squared Error} \\
            \text{MSE}      &= \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{f}(x_i))^2, \\
            \hat{f}(x_i)    &= \text{the prediction that} \ \hat{f} \ \text{gives for the} \ i\text{th observation.}
        \end{align*}

.. math::

    \begin{align*}
                        & \textbf{Mean Squared Error} \\
        \text{MSE}      &= \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{f}(x_i))^2, \\
        \hat{f}(x_i)    &= \text{the prediction that} \ \hat{f} \ \text{gives for the} \ i\text{th observation.}
    \end{align*}
