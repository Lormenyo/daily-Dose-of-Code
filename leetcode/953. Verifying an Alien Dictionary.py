

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # store the index of the letters in the given order as a hashmap
        characterIndex = {c: i for i, c in enumerate(order)}

        #go through the words in pairs, every word and its adjacent word
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            # go through the first word
            for j in range(len(word1)):

                # if the index is the same as the second word
                # it means word2 is the prefix of word1 which is wrong order
                # eg. [hello, he] is wrong order 
                if j == len(word2):
                    return False

                #find the first differing letter in both words
                if word1[j] != word2[j]:
                    #if the index of the letter in word2 is lower than in word1
                    # it means the order is wrong
                    if characterIndex[word2[j]] < characterIndex[word1[j]]:
                        return False
                    break

        return True
