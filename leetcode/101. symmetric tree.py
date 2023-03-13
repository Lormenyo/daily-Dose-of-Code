# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
#         rootNode = root
        
#         def inOrderTraversal(root):
#             if root == None:
#                 return []
#             return inOrderTraversal(root.left) + [root.val if root.val else None ] + inOrderTraversal(root.right)
        
#         linearTree = inOrderTraversal(root)
        
#         rootNodeIndex = linearTree.index(rootNode.val)
        
#         print(f"{inOrderTraversal(root)}, LEFT: {linearTree[:rootNodeIndex]}, RIGHT: {list(reversed(linearTree[rootNodeIndex+1:]))}")
#         return linearTree[:rootNodeIndex] == list(reversed(linearTree[rootNodeIndex+1:]))


        def compareNodes(leftNode, rightNode):
            # if both of the values on either side is null
            # it is symmetrical
            if not leftNode and not rightNode:
                return True

            # if one of the values on either side is null
            # it is asymmetrical
            if not leftNode or not rightNode:
                return False

            return leftNode.val == rightNode.val and compareNodes(leftNode.left, rightNode.right) and compareNodes(rightNode.left, leftNode.right)
        
        return compareNodes(root.left, root.right)