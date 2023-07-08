# Definition for a binary tree node.

from typing import Optional
from leetcode.helper import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None or root.val == val:
            return root
        
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
        