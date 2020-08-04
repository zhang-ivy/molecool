"""
molecool
A Python package for analyzing and visualizing molecular structure. For MSF bootcamp.
"""

# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .molecool import build_bond_list
from .visualize import draw_molecule, bond_histogram

import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
