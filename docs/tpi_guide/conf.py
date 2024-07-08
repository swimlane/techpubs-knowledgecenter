# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Swimlane'
copyright = '2024, Swimlane'
author = 'Swimlane'
release = '24.2.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration test

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',   
]


templates_path = ['../../_templates']
exclude_patterns = []

# Specify root document
root_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#read the docs theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['../../_static']
html_last_updated_fmt= ''
html_use_opensearch=''

# Include the custom JavaScript file
html_js_files = [
    'feedback.js',
]

# Add the name of your CSS file to the html_css_files list
html_css_files = ['custom.css']  # Replace 'custom.css' with the name of your CSS file

# Add custom CSS files
#html_css_files = [
 #   'dark.css',   # Dark theme styles
#]

# Add custom JavaScript files
#html_js_files = [
 #   'theme-toggle.js',
#]

# -- Options for LaTeX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    % Additional preamble stuff here
    ''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    (root_doc, 'tpi_guide.tex', 'Turbine Platform Installer Guide', 'Swimlane', 'manual'),
]
