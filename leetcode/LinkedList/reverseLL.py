# Definition for singly-linked list.


from typing import Optional

from leetcode.helper import ListNode



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead        
    
sol = Solution()
node = ListNode(None, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
print(sol.reverseList(node))