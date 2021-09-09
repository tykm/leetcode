# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # no children return true
        if root == None or (root.left == None and root.right == None):
            return True
        
        # Check if left and right are valid
        if root.left != None:
            if root.left.val >= root.val:
                return False
        if root.right != None:
            if root.right.val <= root.val:
                return False
            
        # Recurse children
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        
                