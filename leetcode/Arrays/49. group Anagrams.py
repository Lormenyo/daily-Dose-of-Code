

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            
            if sortedWord not in anagrams:
                anagrams[sortedWord] = [word]
                
            else:
                anagrams[sortedWord].append(word)

        return list(anagrams.values())
