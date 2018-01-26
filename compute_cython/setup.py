from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name="Compute pyx",
    ext_modules=cythonize("compute_cython.pyx")
)
