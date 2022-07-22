# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greaterEqual = ListNode()
        
        le = less
        gte = greaterEqual
        
        while head:
            if head.val < x:
                le.next = head
                le = le.next
            else:
                gte.next = head
                gte = gte.next
            head = head.next
        
        le.next = greaterEqual.next
        gte.next = None
        
        return less.next