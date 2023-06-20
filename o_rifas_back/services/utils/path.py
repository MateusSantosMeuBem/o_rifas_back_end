"""
Functions to handle paths in project.
"""

from os.path import (
    abspath,
    dirname,
    join,
)

ROOT_PATH = join(dirname(abspath(__file__)), '..', '..')
