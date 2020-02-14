################################################################################
# Project Euler Problem 22: Names scores
# 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
# containing over five-thousand first names, begin by sorting it into 
# alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain 
# a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 x 53 = 49714.
# 
# What is the total of all the name scores in the file?
################################################################################

def letterToNumeric(word):
    return sum((ord(c) - 64) for c in word)

namesList = []
namesSum = 0

names = open('p22_names.txt', 'r')
namesListTemp = names.read()
namesListTemp = namesListTemp.split(',')
names.close()

for name in namesListTemp:
    name = name.replace('\"', '')
    namesList.append(name)

namesList = sorted(namesList)

for i in range(0, len(namesList), 1):
    namesSum = namesSum + (letterToNumeric(namesList[i]) * (i + 1))

print(namesSum)
