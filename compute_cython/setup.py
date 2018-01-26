from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = cythonize("compute_cython.pyx")
# ext_modules = cythonize("compute_cython2.pyx")
# ext_modules = cythonize("compute_cython3.pyx")

setup(
    name="Compute pyx",
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
