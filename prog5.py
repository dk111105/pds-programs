import numpy as np
bags = np.random.randint(0, 11, (5,3))
print("No. of balls in each bag:\n", bags, "\n")
np.add(bags, 3, out=bags[0])
np.subtract(bags, 3, out=bags[2])
print("Final number of bags in each bag:\n", bags, "\n")
