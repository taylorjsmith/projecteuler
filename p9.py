################################################################################
# Project Euler Problem 9: Special Pythagorean triplet
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
################################################################################

goal = 1000
found = False

for a in range(2, ((goal - 3) // 3), 1):
    for b in range((a + 1), ((goal - a) // 2), 1):
        c = goal - a - b

        if b >= c:
            break
        else:
            if (a * a) + (b * b) == (c * c):
                found = True
                break

    if found == True:
        break

prod = a * b * c
print(prod)
