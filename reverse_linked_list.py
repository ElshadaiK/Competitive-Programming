# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        y = None
        if(x):
            if(x.next):
                y = x.next
            else:
                return head
        else:
            return head
        if(y):
            loop = 0
            while(y):
                if(loop == 0):
                    x.next = None
                    loop += 1
                temp = None
                if(y.next):
                    temp = y.next
                y.next = x
                x = y
                y = temp

            
        return x