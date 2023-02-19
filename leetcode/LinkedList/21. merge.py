class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeList(self, list1, list2):
        
        head = ListNode()
        
        currentNode = head
        
        while list1 and list2:
            
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
                
            currentNode = currentNode.next
            
        if list1:
            currentNode.next = list1
            
        if list2:
            currentNode.next = list2
            
        return head.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #for 
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2