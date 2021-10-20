# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: root is None or one of the goals
        if root in (None, p, q):
            return root
        
        # Traverse left and right
        left  = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        
        # Three cases:
        # Solution node - left and right have singular solutions
        if left and right: 
            return root
        
        # No children and no answer - left and right are both None
        if left is None and right is None:
            return None
        
        # Half solution - either left or right has 1 solution
        return left or right