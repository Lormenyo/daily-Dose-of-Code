


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1

        res = []
        valMap = {}
        for num in numMap.keys():
            valMap[numMap[num]] = valMap.get(numMap[num], []) + [num]

        vals = sorted(list(valMap.keys()), reverse=True)
        for num in vals:
            res += valMap[num]
            if len(res) >= k:
                break

        return res[:k]
    

