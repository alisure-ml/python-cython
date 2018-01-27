from distutils.core import setup
from Cython.Build import cythonize

setup(
    # ext_modules=cythonize("atoi_cython.pyx")
    ext_modules=cythonize("external_cython.pyx")
)