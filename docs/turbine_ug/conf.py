# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Swimlane'
copyright = '2024, Swimlane'
author = 'Swimlane'
release = '24.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration test

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel', 
    #'sphinx_sitemap',
    #'sphinx_search.extension',
]

# Specify the URL of your documentation root
html_baseurl = 'https://docs.swimlane.com/turbine'

# Optional: If you're using versioning, specify the current version
# sitemap_version = 'v1.0'

templates_path = ['../../_templates']

# Specify root document
root_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#read the docs theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['../../_static']
html_last_updated_fmt= ''
html_use_opensearch=''
# Disable copying of source files to the output directory
html_copy_source = False
# Suffix for the source links
html_sourcelink_suffix = '.rst'

# Include the custom JavaScript file
html_js_files = [
    '../../_staticfeedback.js',
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

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    (root_doc, 'TurbineUG.tex', 'Turbine UG Documentation', 'Swimlane', 'manual'),
]

# Optionally, you can configure additional LaTeX settings
latex_elements = {
    'papersize': 'a4paper',
    'fontpkg': '\\usepackage{times}',
    'figure_align': 'htbp',
}

# You can also customize the LaTeX preamble if needed
latex_elements['preamble'] = r'''
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{}
\fancyhead[C]{Turbine UG Documentation}
\fancyhead[R]{}
'''
