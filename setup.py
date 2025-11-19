import sys
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext
import lxml

LXML_PATH = lxml.__path__[0]
INCLUDE_DIRS = [LXML_PATH, LXML_PATH + '/includes']

ext_modules = [
    Extension(
        "pydepta.trees_cython",
        ['pydepta/trees_cython.pyx'],
        include_dirs=INCLUDE_DIRS
    )
]

cmdclass = {'build_ext': build_ext}

setup(
      packages=find_packages(),
      cmdclass=cmdclass,
      ext_modules=ext_modules
)
