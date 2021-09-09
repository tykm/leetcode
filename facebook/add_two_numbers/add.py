# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        root = ListNode(0)
        n = root
        carry = 0
        while l1 or l2:
            if l1.val == None:
                sm = 0 + l2.val + carry
            elif l2.val == None:
                sm = l1.val + 0 + carry
            else:
                sm = l1.val + l2.val + carry
            carry = 0
            # two digits greater than 9: then carry a 1
            if sm >= 10:
                carry = 1
                sm -= 10
            n.next = ListNode(sm)
            n = n.next
            
            l1 = l1.next
            l2 = l2.next
        
        
        return root.next
            


sol = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
sol.addTwoNumbers(l1, l2)

# 342
# 465
# 807