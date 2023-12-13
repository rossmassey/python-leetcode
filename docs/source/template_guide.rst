.. _template-guide:

Template Guide
--------------

.. code-block:: none

    template_generator
    ├── __init__.py
    ├── cookies.py                  # reads cookies.txt
    ├── cookies.txt                 # Netscape HTTP Cookie File
    ├── main.py
    ├── network.py                  # network calls
    ├── problem_parser.py           # parses problem content
    ├── template.py                 # writes template files
    └── templates
        ├── doc_template.txt
        └── question_template.txt


Run ``scripts/template_generator/main.py`` and enter the leetcode problem number to generate a solution
template at ``src/leetcode/q_XXXX_problem.py``

.. note::
    This will also create necessary files for the autodocumentation and
    ``doctest`` ready examples within the source file

    :ref:`See here <documentation-guide>` for more information

Cookies
-------

The ``LEETCODE_SESSION`` cookie is needed for the ``syncedCode`` GraphQL query

``cookies.py`` is used to read a Netscape HTTP Cookie File (``cookies.txt``), which can be generated
from leetcode.com using an extension such as this one:

https://github.com/hrdl-github/cookies-txt

Alternatively, using Chrome or Firefox dev tools:

#. Open **dev tools*** -> **Network** tab
#. Go to https://www.leetcode.com
#. Find an entry with File: ``/graphql/``, click the **Cookies** tab
#. Find the value for ``LEETCODE_SESSION``
#. Create ``cookies.txt`` under ``scripts/template_generator``
#. Replace ``<token_value>`` with the value for ``LEETCODE_SESSION`` for the content

.. code-block:: none

    .leetcode.com	TRUE	/	TRUE	1703486435	LEETCODE_SESSION	<token_value>
