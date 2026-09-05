# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            # Base case, empty tree is balanced
            if not root:
                return [True, 0]

            # Determine if from left subtree is it balanced and from right is it balanced?
            left, right = dfs(root.left), dfs(root.right)
            # Take absolute value from left and right heights and make sure they are less than 1
            # make sure that they are both True first too! If they aren't we know we don't have a balanced tree
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return the T/F and the height of that subtree + 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]