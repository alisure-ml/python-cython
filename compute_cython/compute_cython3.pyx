cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)

def spherical_distance(float lon1, float lat1, float lon2, float lat2):
    cdef float radius = 3956
    cdef float pi = 3.14159265
    cdef float x = pi/180.0
    cdef float a,b,theta,distance
    a = (90.0 - lat1)*x
    b = (90.0 - lat2)*x
    theta = (lon2 - lon1)*x
    distance = acosf(cosf(a)*cosf(b)) + (sinf(a) * sinf(b) * cosf(theta))
    return radius * distance

def f_compute(double a, double x, int n):
    cdef int i
    cdef double s = 0
    cdef double dx = (x - a)/n
    for i in range(n):
        s += ((a + i * dx) ** 2 - (a + i * dx))
    return s * dx
