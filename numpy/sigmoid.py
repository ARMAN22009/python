import numpy as np



def sigmoid(array):
    return 1/(1 + np.exp(-array))

a=np.arange(12).reshape(3,4)
print(sigmoid(a))


# sigmoid makes every number in between 0 to 1

# sigmoid(0) → 0.5

# sigmoid(large positive) → close to 1

# sigmoid(large negative) → close to 0

