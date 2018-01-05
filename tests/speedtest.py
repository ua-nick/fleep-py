import time
import fleep

with open("testfile", "rb") as file:
    stream = file.read(128)

times = []

for i in range(10000):
    time_ = time.time()
    fleep.get(stream)
    times.append(time.time() - time_)

print("min:", round(min(times), 7))
print("max:", round(max(times), 7))
print("avg:", round(sum(times)/len(times), 7))
