# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            one = head
        else:
            return False
        if head.next:
            two = head.next
        else:
            return False
        
        while one and two and two.next:
            if one == two:
                return True
            one = one.next
            two = two.next.next
        return False