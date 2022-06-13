#!/usr/bin/env python
"""
Credit to https://github.com/GalacticDynamics-Oxford/Agama/blob/master/setup.py for tools
"""
import pathlib
import distutils
from distutils.command.build_ext import build_ext
from distutils.cmd import Command
from distutils.core import setup

from src._build_utils import *
from src.Galaxia.constants import NAME, GALAXIA_SUBMODULE_NAME, SRC_DIR
from src.Galaxia.__metadata__ import *

ROOT_DIR = pathlib.Path(__file__).parent

long_description = ""


class MyBuildExt(build_ext):
    def run(self):
        check_galaxia_submodule(ROOT_DIR)
        build_and_install_galaxia(GALAXIA_SUBMODULE_NAME)


class MyTest(Command):
    description = 'run tests'
    user_options = []

    def initialize_options(self): pass

    def finalize_options(self): pass

    def run(self): pass


setup(name=NAME,
      version=__version__,
      author=__author__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__email__,
      url="https://github.com/athob/py-Galaxia",
      description="",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          __status__,
          "Environment :: Console",
          "Intended Audience :: Science/Research",
          __license__,
          "Natural Language :: English",
          "Operating System :: Unix",
          "Programming Language :: Python :: 3",
          "Topic :: Database",
          "Topic :: Scientific/Engineering :: Astronomy",
          "Topic :: Software Development :: Version Control :: Git"
      ],
      python_requires='>=3',
      packages=[NAME],
      package_dir={'': SRC_DIR},
      install_requires=['numpy', 'h5py', 'ebfpy'],
      ext_modules=[distutils.extension.Extension('', [])],
      cmdclass={'build_ext': MyBuildExt, 'test': MyTest},
      )
