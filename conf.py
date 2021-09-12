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
