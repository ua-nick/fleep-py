import time
import fleep


file = open("testfile", "rb").read(128)

times = []

for i in range(100000):
    time_ = time.time()
    fleep.get(file)
    times.append(time.time() - time_)

print(max(times))
