

def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """    
    # p and q are both None
    if not p and not q:
        return True
    # one of p and q is None
    if not q or not p:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.right, q.right) and \
           self.isSameTree(p.left, q.left)

# Complexity Analysis

# Time complexity : O(N)O(N), where N is a number of nodes in the tree, since one visits each node exactly once.

# Space complexity : O(N)O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.