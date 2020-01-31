################################################################################
# Project Euler Problem 4: Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
################################################################################

def isPalindrome(num):
    numStr = str(num)
    return numStr == numStr[::-1]

valOne = 100
valTwo = 999
largestPal = 0

while valOne < valTwo:
    while valTwo > (valTwo // 2):
        prod = valOne * valTwo
        if isPalindrome(prod) and (prod > largestPal):
            largestPal = prod
        valTwo = valTwo - 1
    valOne = valOne + 1
    valTwo = 999

print(largestPal)
