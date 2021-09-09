# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], smaller_than=float('inf'), bigger_than=float('-inf')) -> bool:
        # Base case: empty node means we're OK
        if root == None: return True
        
        # Fail case: child does not fit criteria
        if root.left:
            if root.left.val >= root.val or root.left.val <= bigger_than or root.left.val >= smaller_than:
                return False
        if root.right:
            if root.right.val <= root.val or root.right.val >= smaller_than or root.right.val <= bigger_than:
                return False
        
        # Recurse left AND right
        return self.isValidBST(root.left, min(smaller_than, root.val)) and self.isValidBST(root.right, smaller_than, max(bigger_than, root.val))
        
                