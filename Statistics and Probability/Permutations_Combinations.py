'''
Find the number of permutations and combinations that can be formed from the word HORSE taking two letters at a time.
'''


from itertools import combinations
from itertools import permutations
import numpy as np
import math
arr=np.array(['H','O','R','S','E'])
print(list(combinations(arr,2)))
print("Combinations",len(list(combinations(arr,2))))
print(list(permutations(arr,2)))
print("Permutations",len(list(permutations(arr,2))))

#Output
'''
[('H', 'O'), ('H', 'R'), ('H', 'S'), ('H', 'E'), ('O', 'R'), ('O', 'S'), ('O', 'E'), ('R', 'S'), ('R', 'E'), ('S', 'E')]
Combinations 10
[('H', 'O'), ('H', 'R'), ('H', 'S'), ('H', 'E'), ('O', 'H'), ('O', 'R'), ('O', 'S'), ('O', 'E'), ('R', 'H'), ('R', 'O'), ('R', 'S'), ('R', 'E'), ('S', 'H'), ('S', 'O'), ('S', 'R'), ('S', 'E'), ('E', 'H'), ('E', 'O'), ('E', 'R'), ('E', 'S')]
Permutations 20
'''

