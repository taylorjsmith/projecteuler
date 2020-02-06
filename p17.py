################################################################################
# Project Euler Problem 17: Number letter counts
# 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
# letters. The use of "and" when writing out numbers is in compliance 
# with British usage.
################################################################################

def numToWords(num):
    numWordsOnes = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numWordsTeens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    numWordsTens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num == 0:
        return ""

    if num >= 1 and num <= 9:
        return numWordsOnes[num]
    
    if num >= 10 and num <= 99:
        if num >= 11 and num <= 19:
            return numWordsTeens[num - 10]
        else:
            tensDigit = num // 10
            onesDigit = num - (tensDigit * 10)

            return numWordsTens[tensDigit] + numToWords(onesDigit)

    if num >= 100 and num <= 999:
        andString = "and"
        hundredsDigit = num // 100
        tensDigit = (num - (hundredsDigit * 100)) // 10
        onesDigit = (num - (hundredsDigit * 100) - (tensDigit * 10))

        if ((tensDigit * 10) + onesDigit) == 0:
            andString = ""

        return numWordsOnes[hundredsDigit] + "hundred" + andString + numToWords((tensDigit * 10) + onesDigit)

    if num == 1000:
        return "onethousand"

wordStrLength = 0

for i in range(1, 1001, 1):
    wordStrLength = wordStrLength + len(numToWords(i))

print(wordStrLength)
