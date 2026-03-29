# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Project'
copyright = '2024, Author'
author = 'Author'

version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# テーマの設定
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# メタタグの追加
html_context = {
    'display_github': False,
    'last_updated': True,
    'commit': False,
}
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# テーマの設定
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# メタタグの追加
html_context = {
    'display_github': False,
    'last_updated': True,
    'commit': False,
}
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# テーマの設定
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# メタタグの追加
html_context = {
    'display_github': False,
    'last_updated': True,
    'commit': False,
}
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# テーマの設定
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# メタタグの追加
html_context = {
    'display_github': False,
    'last_updated': True,
    'commit': False,
}
