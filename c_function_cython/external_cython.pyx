cdef extern from "math.h":
    double sin(double x)

def sin_cython(x):
    return sin(x)
