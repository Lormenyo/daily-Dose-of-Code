# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings



#only works for 2 test cases
def makeAnagram1(a, b):
    diff = (len(a) - len(set(a))) + (len(b)-len(set(b)))
    return len(set(a) ^ set(b)) + diff

def makeAnagram2(a,b):
    a = sorted(list(a))
    b = sorted(list(b))

    return sum(aElement != bElement for aElement, bElement in zip(a, b) ) + abs(len(a)-len(b))

print(makeAnagram1("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))

#----------- PASSED ALL TEST CASES ---------------Í
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    
    def makeDict(string):
        stringDict = {}
        for letter in string:
            stringDict[letter] = stringDict.get(letter, 0) + 1
        return stringDict
    
    def countMinDifference(dict1, dict2):
        minDif = 0
        visited = []
        for letter in dict1:
            visited.append(letter)
            if dict2.get(letter, 0) != dict1[letter]:
                minDif += abs((dict1[letter] - dict2.get(letter, 0)))
                
        for letter in dict2:
            if dict1.get(letter, 0) != dict2[letter] and letter not in visited:
                minDif += abs((dict2[letter] - dict1.get(letter, 0)))
                
        return minDif
    
    aDict = makeDict(a)
    bDict = makeDict(b)
            
    return countMinDifference(aDict, bDict)
                

    