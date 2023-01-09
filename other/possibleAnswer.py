# https://leetcode.com/playground/mb5tFupC/live


'''
They class is cheating and they are hiding the answers in a string. As a teacher you are to find whether the string contains the 
right answers

words = ["cat", "opportunity", "nicer", "slime"]
string = "saddtfc" #cat

words = ["create", "main", "bruce", "techin"]
string = "jtdenhraudc" # -
'''
words_1 = ["cat", "opportunity", "nicer", "slime"]
string_1 = "saddtfc"
words_2 = ["create", "main", "bruce", "tech"]  
string_2 = "jtdenhraudc"



def find(words, string):

    stringMap = {}
    for character in string:
        stringMap[character] = stringMap.get(character, 0) + 1
        
    for word in words:
        wordMap = {}
        isMatch = True
        for character in word:
            wordMap[character] = wordMap.get(character, 0) + 1
        
        for c in wordMap:
            if c not in stringMap or stringMap[c] < wordMap[c]:
                isMatch = False
                
        if isMatch:
            return word
        
    return '-'

def find2(words, string):
    def convertToDic(w):
        mapW = {}
        for character in w:
            mapW[character] = mapW.get(character, 0) + 1
        return mapW
    def compare(stringMap, wordMap):
        for c in wordMap:
            if wordMap[c] > stringMap.get(c,0):
                return False
        return True
    stringMap = convertToDic(string)
    
    for word in words:
        wordMap = convertToDic(word)
        if compare(stringMap, wordMap):
            return word
    return "-"
        
                
        
print(find2(words_1, string_1))
print(find2(words_2, string_2))

