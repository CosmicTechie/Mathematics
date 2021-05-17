'''
In how many ways can 10 balls be picked, 7 red out of 10 and 3 blue out of 8?
'''
import math

red=math.factorial(10)/((math.factorial(7))*math.factorial(3))
blue=math.factorial(8)/((math.factorial(3))*math.factorial(5))
print(red*blue)

#Output
'''
6720.0
'''
