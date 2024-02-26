import os
import sys

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Leetcode Solutions'
copyright = '2024, Ross Massey'
author = 'Ross Massey'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# repo root location
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# docs source location
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

extensions = [
    'sphinx.ext.autodoc',   # html generation from docstrings
    'sphinx.ext.viewcode',  # source code in documentation
    'sphinx.ext.doctest',   # evaluate >>> expressions
    'sphinx.ext.napoleon',  # support google style docstring
    'sphinx.ext.mathjax',   # LaTeX support
]

from components.line_directive import setup as line_directive_setup

templates_path = ['_templates']
exclude_patterns = []

# only show final name (x instead of src.x)
add_module_names = False

# show line numbers in view source code
viewcode_line_numbers = True

# do not sort alphabetically
autodoc_member_order = 'bysource'

doctest_global_setup = '''
from src.leetcode import *
from src.common import *
'''
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# add css
html_css_files = ['css/custom.css']

# -- Setup -------------------------------------------------------------------


def skip(app, what, name, obj, would_skip, options):
    """
    Allows the __init__ method to be autodoc
    """
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.add_css_file('css/custom.css')
    app.connect("autodoc-skip-member", skip)

    line_directive_setup(app)
