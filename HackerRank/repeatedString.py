import math

# this solution has memory issues
def repeatedString1(s, n):
    newString = s
    if len(s) < n:
        newString = (s * math.ceil(n/len(s)))[:n]
    else:
        newString = s[:n]
    return newString.count("a")
    

def repeatedString2(s, n):
    return round((n*s.count("a"))/len(s))


# print(repeatedString2("a", 100))
# print(repeatedString2("a", 1000000000000))
# print(repeatedString2("abc", 500))
# print(repeatedString2("abcac", 5))
# print(repeatedString2("abcac", 7))
# print(repeatedString2("bc", 7)) #0
# print(repeatedString2("bca", 7)) #2
# print(repeatedString2("bcaa", 7)) #3
