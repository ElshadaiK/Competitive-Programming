# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        ptr = x
        y = None
        if(x):
            if(x.next):
                y = x.next
            else:
                return head
        else:
            return head
        if(y):
            while(y):
                temp = None
                if(y.next):
                    temp = y.next
                if(x.val == y.val):
                    x.next = temp
                else:
                    x = x.next
                y = temp
                

            
        return ptr