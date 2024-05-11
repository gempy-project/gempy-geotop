import time
import os
import sys
import warnings

from sphinx_gallery.sorting import FileNameSortKey
import pyvista
import numpy as np

# External examples:
sys.path.insert(0, os.path.abspath('.'))
import make_external_gallery
make_external_gallery.make_example_gallery()

# -- PyVista settings -----------------------------------------------------

pyvista.set_error_output_file('errors.txt')
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True  # Not necessary - simply an insurance policy
pyvista.BUILDING_GALLERY = True
# Preferred plotting style for documentation
pyvista.set_plot_theme('document')
try:
    pyvista.rcParams['window_size'] = np.array([1024, 768]) * 2
except AttributeError:
    print("Could not set pyvista.rcParams['window_size'].")

# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath('./images/'), 'auto-generated/')

if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

import gempy  # ! This seems important to load pykeops c++ library properly
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# Load extensions
extensions = [
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.coverage',
        'sphinx.ext.mathjax',
        'sphinx.ext.viewcode',
        'sphinx.ext.githubpages',
        'sphinx.ext.napoleon',
        'sphinx_gallery.gen_gallery',
        "pyvista.ext.plot_directive",
        "sphinx_design",
        'sphinx_automodapi.automodapi',
        'sphinx_automodapi.smart_resolver',
]

linkcheck_retries = 3
linkcheck_timeout = 500

autosummary_generate = True
add_module_names = True
numpydoc_show_class_members = False

intersphinx_mapping = {
        'numpy'     : ('https://numpy.org/doc/stable/', None),
        'matplotlib': ('https://matplotlib.org/', None),
        'pyvista'   : ('https://docs.pyvista.org/', None),
        'pandas'    : ('https://pandas.pydata.org/pandas-docs/stable/', None),
        'xarray'    : ('http://xarray.pydata.org/en/stable/', None)
}

napoleon_google_docstring = True

description = 'DataHub for geoscientific data in Python.'

# The templates path.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'GemPy GeoTop'
author = 'GemPy GeoTop Team'
copyright = f'2023-{time.strftime("%Y")}, {author}'

# |version| and |today| tags (|release|-tag is not used).
version = 0.1
release = 0.1
today_fmt = '%d %B %Y'

# List of patterns to ignore, relative to source directory.
exclude_patterns = ['_build', '../tests']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Sphinx Gallery Options
sphinx_gallery_conf = {
        # path to your examples scripts
        "examples_dirs"          : [
                "../../examples/",
        ],
        # path where to save gallery generated examples
        "gallery_dirs"           : [
                "examples",
        ],
        # Patter to search for example files
        "filename_pattern"       : r"\.py",
        # Remove the "Download all examples" button from the top level gallery
        "download_all_examples"  : False,
        # Sort gallery example by file name instead of number of lines (default)
        "within_subsection_order": FileNameSortKey,
        # directory where function granular galleries are stored
        "backreferences_dir"     : 'gen_modules/backreferences',
        # Modules for which function level galleries are created.  In
        "doc_module"             : ('subsurface', 'numpy', 'pandas'),
        "image_scrapers"         : ('pyvista', 'matplotlib'),
        'first_notebook_cell'    : ("%matplotlib inline\n"
                                    "from pyvista import set_plot_theme\n"
                                    "set_plot_theme('document')"),
        'reference_url'          : {
                # The module you locally document uses None
                'subsurface': None,
                'numpy'     : 'https://numpy.org/doc/stable/'

        },
}

linkcheck_ignore = [r'https://github.com/cgre-aachen/gempy_data/raw/master/',
                    r'https://raw.githubusercontent.com/softwareunderground/subsurface/main/tests/data/borehole/'
                    ]

linkcheck_request_header = {
        '*'                 : {'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8'},
        'https://github.com': {}
}

# -- Options for HTML output ----------------------------------------------
html_static_path = ['_static']
html_logo = '_static/logos/vector-logo.png'
html_favicon = '_static/logos/favicon.ico'
html_sidebars = {
        '**': [
                'about.html',
                'navigation.html',
                'searchbox.html',
        ]
}

# Remove matplotlib agg warnings from generated doc when using plt.show
warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')


# -- CSS fixes --
def setup(app):
    app.add_css_file("style.css")
