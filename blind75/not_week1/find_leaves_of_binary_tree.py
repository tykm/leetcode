# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # { height:values, 0: [4, 5, 3], 1: [2], 2: [1]}
        nodes = defaultdict(list)
        
        def getHeights(node):
            # Base case for no node
            if node == None:
                return -1
            
            # Get left and right heights
            left = getHeights(node.left)
            right = getHeights(node.right)
            
            # Current node height is max of children + 1
            height = max(left, right) + 1
            
            # Store current height and value in nodes dictionary
            nodes[height].append(node.val)
            
            return height
        
        getHeights(root)
        return nodes.values()
        