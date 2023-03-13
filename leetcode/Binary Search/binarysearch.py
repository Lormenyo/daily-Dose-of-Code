# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.



class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l,r = 0, len(nums)-1

        while l <= r:
            #you can calculate the mid by doing (l+r)//2
            # but this makes sure it never exceeds the integer bound 2^31
            midpoint = l + ((r-l) // 2) 

            #search on left side
            if nums[midpoint] > target:
                r = midpoint - 1
            
            #search on right side
            elif nums[midpoint] < target:
                l = midpoint + 1 

            else:
                return midpoint
            
        return -1
    
sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(sol.search(nums, target)) #ans = 4