# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float('-inf')
        
        def dfs(root):
            nonlocal mx
            if not root:
                return 0
            left  = dfs(root.left)
            right = dfs(root.right)
            
            curr_sum = left + root.val + right
            mx = max(mx, curr_sum, root.val, root.val+left, root.val+right)
            #print(curr_sum, mx)

            return max(root.val + max(right, left), root.val)
            
        
        return max(dfs(root), mx)