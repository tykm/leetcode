# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        nxt = None
        curr = head
        while curr:
            nxt = curr.next
            prev, curr.next = curr, prev
            curr = nxt
        return prev