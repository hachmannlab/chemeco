# __name__ = "chemeco"
__version__ = "0.1.0"
__author__ = ["Mojtaba Haghighatlari (mojtabah@buffalo.edu)", "Johannes Hachmann (hachmann@buffalo.edu)"]

from chemeco.wrappers.engine import run as ChemEcoRun
from chemeco.notebooks import ChemEcoNotebook

import sys
sys.dont_write_bytecode = True
