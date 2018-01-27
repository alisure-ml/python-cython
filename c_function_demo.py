from c_function_cython import atoi_cython

n = atoi_cython.parse_s_to_i(b"11")
print(type(n))

from c_function_cython import external_cython
n = external_cython.sin_cython(10.0)
print(n)