# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None,None
            left_begin, left_end = dfs(node.left)
            right_begin, right_end = dfs(node.right)
            node.left = None
            node_end = node
            if left_begin:
                node_end.right = left_begin
                node_end = left_end
            if right_begin:
                node_end.right = right_begin
                node_end = right_end
            
            
            return node, node_end
        
        
        dfs(root)