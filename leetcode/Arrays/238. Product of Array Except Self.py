

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefix, postfix = 1, 1

        answer.append(prefix) #[1]
        for i in range(len(nums)-1):
            prefix *= nums[i] #prefix = 6
            answer.append(prefix) #[1, 1, 2, 6]

        for i in range(len(nums), -1, -1):
            if i == len(nums): #i = 4
                pass 
            else:       #i=3 #postfix=1, #i=2,#postfix=4, #i=1,#postfix=12,  #i=0,#postfix=24
                answer[i] *= postfix  #6x1 #[1,1,2,6], #4x2 #[1,1,8,6], #1x12 #[1,12,8,6],#1x24 #[24,12,8,6],   
                postfix *= nums[i]    #postfix = 1x4=4  #postfix = 4x3=12 #postfix = 12x2=24
                
        return answer