from demo_compute import compute
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
