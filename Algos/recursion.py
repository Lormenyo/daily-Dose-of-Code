
from typing import List


def reverseString(index, myStr):

    if myStr == None or index >= len(myStr):
        return
    # elif len(myStr) == 1:
    #     print(myStr)
    reverseString(index+1, myStr)
    print(myStr[index], end="")


reverseString(0, "first")


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if s == None:
            return
        self.reverseStringHelper(0, s)
        print(s)


    def reverseStringHelper(self, index, strArr):

        if strArr == None or index >= len(strArr)/2:
            return
        
        self.reverseStringHelper(index+1, strArr)
        first = strArr[index]
        lastIndex = len(strArr) - (index+1)
        last = strArr[lastIndex]
        strArr[index] = last
        strArr[lastIndex] = first
       

sol = Solution()
sol.reverseString(["h","e","l","l","o"])

