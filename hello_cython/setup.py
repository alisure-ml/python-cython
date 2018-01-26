from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name="Hello pyx",
    ext_modules=cythonize("hello.pyx")
)

