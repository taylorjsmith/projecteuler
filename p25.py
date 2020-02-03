################################################################################
# Project Euler Problem 25: 1000-digit Fibonacci number
# 
# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.
# 
# Hence the first 12 terms will be:
# F_1 = 1
# ...
# F_12 = 144
# The 12th term, F_12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain 
# 1000 digits?
################################################################################

f1 = 1
f2 = 1
f3 = 0

currTermIndex = 2

while len(str(f3)) != 1000:
    currTermIndex = currTermIndex + 1
    f3 = f2 + f1
    f1 = f2
    f2 = f3

print(currTermIndex)
