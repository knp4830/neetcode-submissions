# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            # Base Case: Empty Tree
            if not node:
                return False
            
            curSum += node.val
            # If its a leaf node, return True if it equals targetSum else false
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum)) or (dfs(node.right, curSum))
        return dfs(root, 0)
