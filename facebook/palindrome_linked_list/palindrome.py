# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []
        ct = 0
        ct_node = head
        while ct_node:
            ct_node = ct_node.next
            ct += 1
        for i in range(ct):
            if i < ct//2:
                q.append(head.val)
                head = head.next
            elif i == ct//2 and ct % 2 == 1:
                head = head.next
            else:
                if head.val != q.pop():
                    return False
                head = head.next
        return True
            