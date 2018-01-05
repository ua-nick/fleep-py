import time
import fleep


with open("testfile", "rb") as file:
    stream = file.read(128)

times = []
min_time = 0.0
max_time = 0.0

for i in range(10000):
    time_1 = time.time()
    fleep.get(stream)
    time_2 = time.time() - time_1
    times.append(time_2)
    max_time = time_2 if time_2 > max_time else max_time
    min_time = time_2 if time_2 < min_time else min_time

print("min:", round(min_time, 7))
print("max:", round(max_time, 7))
print("avg:", round(sum(times)/len(times), 7))
