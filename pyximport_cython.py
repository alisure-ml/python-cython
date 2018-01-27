import demo_basic_python
demo_basic_python.fun_name(1.4)

import primes
print(primes.primes(1000))

# 采用pyximport的方式导入
import pyximport
pyximport.install(pyimport=False)

# 导入cython 1
import demo_basic_cython
demo_basic_cython.fun_name(1.4)

# 导入cython 2
import primes
print(primes.primes(1000))
