from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            # check if value is equal to value preceding it
            # if so skip it
            if i > 0 and nums[i - 1] == val:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                theSum = nums[l] + nums[r] + val

                if theSum > 0:
                    r -= 1
                elif theSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    # update the pointer until current left value != previous value
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res