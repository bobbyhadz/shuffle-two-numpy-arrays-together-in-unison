# Shuffle two NumPy Arrays the same way (in Unison)

import numpy as np

arr1 = np.array([[2, 4], [3, 5], [6, 8]])
arr2 = np.array([3, 4, 5])

perm = np.random.permutation(len(arr1))
print(perm)

print('-' * 50)

print(arr1[perm])

print('-' * 50)

print(arr2[perm])