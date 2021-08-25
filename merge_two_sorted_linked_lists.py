# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ptr = res
        x = l1
        y = l2
        while(x and y):
            if(x.val < y.val):
                res.next = x
                res = res.next
                x = x.next
            elif(y.val < x.val):
                res.next = y
                res = res.next
                y = y.next
            else:
                res.next = y
                res = res.next
                y = y.next
                res.next = x
                res = res.next
                x = x.next
        if(x):
            res.next = x
        if(y):
            res.next = y
        
        return ptr.next
                    
                
            