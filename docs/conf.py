# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime

import ctwrap

# -- Project information -----------------------------------------------------

year = datetime.date.today().year
project = 'useful'
author = ctwrap.__author__
copyright = '2018-{}, {}'.format(year-2000, author)

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = useful.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinxarg.ext'
]

suppress_warnings = [
    'nbsphinx.localfile',
]

autodoc_default_flags = ['members', 'no-undoc-members'] # 'show-inheritance',
autodoc_member_order = 'bysource' # 'groupwise', 'alphabetical'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'github_user': 'microcombustion',
    'github_repo': 'ctwrap',
    'github_banner': False,
    'github_button': True,
    'github_type': 'star',
    'github_count': False,
    'show_powered_by': True,
    'page_width': '1010px',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# save plots when executing notebooks.
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg'}",
]
