# Given a string s, find the length of the longest 
# substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        - have window as set
        - make sure window never has duplicate
        - get max length of window when it doesn't have duplicate
        """

        maxLength = 0
        window = set()
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            maxLength = max(len(window), maxLength)

        return maxLength
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb")) #3
print(sol.lengthOfLongestSubstring("bbbbb")) #1
print(sol.lengthOfLongestSubstring("pwwkew")) #3


