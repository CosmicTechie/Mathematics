from itertools import combinations
from itertools import permutations
import numpy as np
import math
arr=np.array(['H','O','R','S','E'])
print(list(combinations(arr,2)))
print("Combinations",len(list(combinations(arr,2))))
print(list(permutations(arr,2)))
print("Permutations",len(list(permutations(arr,2))))



