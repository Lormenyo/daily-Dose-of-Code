

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        l,r = 0, len(nums) -1
        mid = 0

        while l <= r:
            mid = l + ((r-l) //2)
            

            if nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1

            else:
                return mid
            print(f"mid: {mid} value: {nums[mid]} left: {l} right: {r}")
      
        return r+1

sol = Solution()
nums = [1,3,5,6]
target = 2
print(sol.searchInsert(nums, target)) #ans = 1

nums =[1,3,5,6]
target = 7
print(sol.searchInsert(nums, target)) #ans = 4

nums =[1,3,5,6]
target = 0
print(sol.searchInsert(nums, target)) #ans = 4

# mid: 1 value: 3 left: 0 right: 0
# mid: 0 value: 1 left: 1 right: 0
# 1
# mid: 1 value: 3 left: 2 right: 3
# mid: 2 value: 5 left: 3 right: 3
# mid: 3 value: 6 left: 4 right: 3
# 4
# mid: 1 value: 3 left: 0 right: 0
# mid: 0 value: 1 left: 0 right: -1
# 1