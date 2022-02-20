# -- Project information -----------------------------------------------------

project = "SSWLCBOK"
copyright = "2022, Juan Arriagada"
author = "Juan Arriagada"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.duration",
]

templates_path = ["_templates"]

language = "es"

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_title = f"SSWLCBOK v{release}"

html_theme = "furo"

html_static_path = ["_static"]

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/jarriagadac/sswlcbok",
            "html": "",
            "class": "fa-solid fa-github fa-2x",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/sswlcbok",
            "html": "",
            "class": "fa-solid fa-twitter fa-2x",
        },
    ],
}