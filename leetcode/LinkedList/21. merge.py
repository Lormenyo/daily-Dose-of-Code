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