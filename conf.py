# GENERAL CONF
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'nbsphinx',  # This lets us use notebooks
]

# I execute the notebooks manually in advance. If notebooks test the code,
# they should be run at build time.
nbsphinx_execute = 'never'
nbsphinx_allow_errors = True

# Add type of source files
source_suffix = ['.rst', '.md', '.ipynb']

# OPTIONS FOR HTML OUTPUT

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
        "github_url": "https://github.com/gilles13/",
        "twitter_url": "https://twitter.com/gillesfidani",
        "search_bar_text": "Search this site...",
        "navbar_end": ["search-field.html", "navbar-icon-links"],
        }
