# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will 
# occur the same number of times. 
# Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

# Example
# s='abc'
# This is a valid string because frequencies are {a:1, b:1, c:1}.

# s = 'abcc'
# This is a valid string because we can remove one c and have 1 of each character in the remaining string.

# s='abccc'
# This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a:1, b:1, c:2} .

# returns YES OR NO


#------------ 4 test cases failing ------------
def isValid(s):
    #if all values not same, check get the highest count and subtract 1
    
    def makeDict(s):
        stringDict = {}
        for letter in s:
            stringDict[letter] = stringDict.get(letter, 0) + 1
            
        return stringDict
    
    def checkValidString(counts):
        # the frequency of the first value in counts should be equal to 
        # length of counts if all letters have the same frequencies
        if (letterCounts.count(letterCounts[0]) == len(letterCounts)):
            return True
        return False
    
    # make dict, if all values are same return YES
    stringCount = makeDict(s)
    letterCounts = list(stringCount.values())
    if (checkValidString(letterCounts)):
        return 'YES'
    else:
        maxCount = max(letterCounts)
        maxIndex = letterCounts.index(maxCount)
        letterCounts[maxIndex] = maxCount - 1
        if (checkValidString(letterCounts)):
            return 'YES'
        else:
            return 'NO'
        