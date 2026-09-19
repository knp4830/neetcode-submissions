# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # This allows us to change it easily
        res = [root.val]

        def dfs(root):
            # Base case, null
            if not root:
                return 0

            # Calculates the leftMax if we were to not split and right max
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # Updates the left and rightMax and sees if it is greater than 0 then we take it
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)


            # Compute max path sum with split
            # So if we chose a subtree and took its right and left and root and we see if its greater than the current
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # We return what the answer would be if we didnt split, we can't choose both or else we're splitting
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
            
