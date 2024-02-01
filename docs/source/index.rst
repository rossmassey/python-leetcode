.. this is the index page of the sphinx documentation
..
.. the toctree directives are used to import other .rst files
.. they can be hidden to only display in sidebar

#########################
Python Leetcode Solutions
#########################

.. _python-leetcode: https://github.com/rossmassey/python-leetcode
.. _leetcode: https://leetcode.com/

*WELCOME* to the documentation page for `python-leetcode`_ repo.

.. toctree::
   :maxdepth: 3
   :caption: ✏️ Problems

   neetcode

:☑️ Tests:
    .. image:: https://github.com/rossmassey/python-leetcode/actions/workflows/doctest.yml/badge.svg
        :target: https://github.com/rossmassey/python-leetcode/actions/workflows/doctest.yml

:☑️ Documentation:
    .. image:: https://github.com/rossmassey/python-leetcode/actions/workflows/gh-pages.yml/badge.svg
        :target: https://github.com/rossmassey/python-leetcode/actions/workflows/gh-pages.yml



How repo is used
----------------

#. Start or complete a new problem on `leetcode`_
#. Run ``template_generator`` with problem ``num`` to create all the repo files
#. Add additional information for problem such as running time and strategy
#. Use ``preview_docs`` to make sure documentation correct and doctest pass
#. Commit and push to GitHub


.. toctree::
   :maxdepth: 1
   :caption: 📝️ Articles
   :hidden:

   folder_structure
   testing
   doc_overview
   problem_format

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: 🖥️ API Documentation

   template_generator_documentation
   preview_docs_documentation
   leetcode_classes


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: 📚 External Docs

   rossmassey.fetch-leetcode-problem <https://rossmassey.github.io/fetch-leetcode-problem/>
   Python Docs <https://docs.python.org/3/>
   Sphinx <https://www.sphinx-doc.org/en/master/>

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: 🌏 Other Links

   Github Repo <https://github.com/rossmassey/python-leetcode>
   Leetcode <https://leetcode.com/>


Modules
=======

* :ref:`modindex`
