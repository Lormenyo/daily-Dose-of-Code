# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.



from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeqLength = 0

        for n in numSet:
            # check if it is the start of a sequence
            # it is a start of a sequence if there is no number to the left of it
            if (n-1) not in numSet:
                # find the longest sequence
                length = 0
                while (n+length) in numSet:
                    length += 1
                longestSeqLength = max(length, longestSeqLength)

        return longestSeqLength



