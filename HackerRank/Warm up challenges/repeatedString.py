import math

# this solution has memory issues
def repeatedString1(s, n):
    newString = s
    if len(s) < n:
        newString = (s * math.ceil(n/len(s)))[:n]
    else:
        newString = s[:n]
    return newString.count("a")
    
# 8 test cases failed for this solution
# because the position of a is not the same
# hence ratio and proprtion wasn't working
def repeatedString2(s, n):
    aCount = (n*s.count("a"))/len(s)
    if aCount - math.floor(aCount) <= 0.5:
        return math.floor(aCount)
    else:
        return round(aCount)


def repeatedString3(s, n):
    numRepeated = math.floor(n/len(s))
    return (s.count("a") * numRepeated) + s[: n % len(s)].count("a")


# print(repeatedString2("a", 100))
# print(repeatedString2("a", 1000000000000))
# print(repeatedString2("abc", 500))
# print(repeatedString2("abcac", 5))
# print(repeatedString2("abcac", 7))
# print(repeatedString2("bc", 7)) #0
# print(repeatedString2("bca", 7)) #2
# print(repeatedString2("bcaa", 7)) #3
# print(repeatedString2("bcaa", 5)) #2
# print(repeatedString2("bcaa", 3)) #1
# print(repeatedString2("bac", 7)) #2
# print(repeatedString2("bac", 5)) #2
# print(repeatedString2("bac", 2)) #1


print(repeatedString3("a", 100))
print(repeatedString3("a", 1000000000000))
print(repeatedString3("abc", 500))
print(repeatedString3("abcac", 5))
print(repeatedString3("abcac", 7))
print(repeatedString3("bc", 7)) #0
print(repeatedString3("bca", 7)) #2
print(repeatedString3("bcaa", 7)) #3
print(repeatedString3("bcaa", 5)) #2
print(repeatedString3("bcaa", 3)) #1
print(repeatedString3("bac", 7)) #2
print(repeatedString3("bac", 5)) #2
print(repeatedString3("bac", 2)) #1