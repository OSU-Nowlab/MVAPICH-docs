# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MVAPICH'
copyright = '2024, NOWLAB'
author = 'NOWLAB'

release = '3.0'
version = '3.0.x'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
