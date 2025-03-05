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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Swimlane'
copyright = '2024, Swimlane'
author = 'Swimlane'

# The full version, including alpha/beta/rc tags
release = '24.2'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx_togglebutton',
]

templates_path = ['_templates']
exclude_patterns = []

root_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['../../_static']

html_css_files = ['custom.css']



html_last_updated_fmt = ''
html_use_opensearch = ''
html_copy_source = False
html_sourcelink_suffix = '.rst'

html_js_files = [
    'feedback.js',
]

def setup(app):
    app.add_css_file('custom.css')

# Configuration for sphinx-togglebutton
togglebutton_hint = ""  # Removes the hint text
togglebutton_hint_hide = ""  # Removes the hide hint text
togglebutton_hint_show = ""  # Removes the show hint text
togglebutton_open_on_print = True  # Expands the sections by default when printing
togglebutton_open_by_default = True  # Expands the sections by default when viewing

# Add custom JavaScript
def setup(app):
    app.add_js_file('custom.js')

html_static_path = ['_static']


# Custom roles for desc and example
from docutils import nodes
from docutils.parsers.rst import roles

def desc_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [nodes.inline(rawtext, text, classes=['desc'])], []

def example_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [nodes.inline(rawtext, text, classes=['example'])], []

roles.register_local_role('desc', desc_role)
roles.register_local_role('example', example_role)

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_documents = [
    (root_doc, 'TurbineUG.tex', 'Turbine UG Documentation', 'Swimlane', 'manual'),
]

latex_elements = {
    'papersize': 'a4paper',
    'fontpkg': '\\usepackage{times}',
    'figure_align': 'htbp',
}

latex_elements['preamble'] = r'''
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{}
\fancyhead[C]{Turbine UG Documentation}
\fancyhead[R]{}
'''
