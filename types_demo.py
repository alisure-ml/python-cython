import time
# from types_cython import pure_python as fun
# from types_cython import pure_cython as fun
# from types_cython import pure_cython2 as fun
from types_cython import pure_cython3 as fun

a = 1000000
b = 10
n = 1000000

start_time = time.clock()
fun.integrate_f(a, b, n)
end_time = time.clock()
print("run time: %f s" % (end_time - start_time))

"""
1.
run time: 0.657677 s

2.
run time: 0.555587 s

3.
run time: 0.086425 s

4.
run time: 0.051151 s

"""