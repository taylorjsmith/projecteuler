################################################################################
# Project Euler Problem 15: Lattice paths
# 
# Starting in the top left corner of a 2x2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# [diagram illustrating possible paths]
# 
# How many such routes are there through a 20x20 grid?
################################################################################

import math

def binom(n, k):
    return (math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))

n = 20
numPaths = binom((2 * n), n)
print(numPaths)
