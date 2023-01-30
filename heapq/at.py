import numpy as np

test = np.ones((3,4))
print(test)
test[0:2,2:3] += 1
print(test)