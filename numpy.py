 import time
import numpy as np

x = np.random.rand(1000000000)

start = time.time()
# mean calculated using numpy - takes around 1 to 2 seconds to execute
mean_np = np.mean(x)
print(mean_np, time.time()-start)
