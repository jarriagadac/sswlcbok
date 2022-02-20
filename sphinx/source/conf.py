# -- Project information -----------------------------------------------------

project = "SSWLCBOK"
copyright = "2022, Juan Arriagada"
author = "Juan Arriagada"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx_last_updated_by_git",
]

templates_path = ["_templates"]

language = "es"

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_title = f"SSWLCBOK v{release}"
html_baseurl = "https://sswlcbok.com"

html_theme = "alabaster"

html_static_path = ["_static"]
