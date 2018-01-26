from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

# ext_modules=cythonize("pure_cython.pyx")
# ext_modules=cythonize("pure_cython2.pyx")
ext_modules=cythonize("pure_cython3.pyx")

setup(
    name="types cython",
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
