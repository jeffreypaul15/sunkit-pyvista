# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config


# -- Project information -----------------------------------------------------

project = 'sunkit-pyvista'
copyright = '2021, '
author = ''

# The full version, including alpha/beta/rc tags
from sunkit_pyvista import __version__
release = __version__

# Use the sunpy theme
from sunpy_sphinx_theme.conf import *
from sphinx_gallery.sorting import ExampleTitleSortKey

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
    'sphinx_changelog',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_gallery.gen_gallery'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.

intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/python3.inv"),
    ),
    "numpy": (
        "https://numpy.org/doc/stable/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/numpy.inv"),
    ),
    "matplotlib": (
        "https://matplotlib.org/",
        (None, "http://www.astropy.org/astropy-data/intersphinx/matplotlib.inv"),
    ),
    "astropy": ("https://docs.astropy.org/en/stable/", None),
    "sunpy": ("https://docs.sunpy.org/en/stable", None),
    "pyvista": ("https://docs.pyvista.org/", None),
}

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

sphinx_gallery_conf = {
    'filename_pattern': '^((?!skip_).)*$',
    'examples_dirs': os.path.join('..', 'examples'),
    'within_subsection_order': ExampleTitleSortKey,
    'gallery_dirs': os.path.join('generated', 'gallery'),
    # Comes from the theme.
    'default_thumb_file': os.path.join(html_static_path[0], 'img', 'sunpy_icon_128x128.png'),
    'abort_on_example_error': False,
    'only_warn_on_example_error': True,
    'plot_gallery': True,
    'remove_config_comments': True,
    'doc_module': ('sunkit_pyvista'),
}
