import compute as compute
# import compute_cython as compute
# import compute_cython2 as compute
# import compute_cython3 as compute
import time


start_time = time.clock()
compute.f_compute(3.2, 6.9, 1000000)
end_time = time.clock()
print("run 1 time: %f s" % (end_time - start_time))

start_time = time.clock()
lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
for i in range(1000000):
    compute.spherical_distance(lon1, lat1, lon2, lat2)
end_time = time.clock()
print("run 2 time: %f s" % (end_time - start_time))


"""
1. 
run 1 time: 0.651578 s
run 2 time: 1.620753 s

run 1 time: 0.286562 s
run 2 time: 1.247603 s


2.
run 1 time: 0.573591 s
run 2 time: 1.538987 s

run 1 time: 0.234744 s
run 2 time: 0.937928 s


3.
run 1 time: 0.002526 s
run 2 time: 1.525995 s

run 1 time: 0.001535 s
run 2 time: 0.871575 s


4.
run 1 time: 0.002509 s
run 2 time: 0.382405 s

run 1 time: 0.001375 s
run 2 time: 0.421578 s

"""
