# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS Approach
        res = []

        # Helper function 
        def dfs(node, depth):
            if not node:
                return None
                # If result has no list for the depth append a new list
            if len(res) == depth:
                res.append([])

            # At current depth append the node value
            res[depth].append(node.val)
            # Call it again on the left child and continue down
            dfs(node.left, depth + 1)
            # Call it again on the right child and continue down
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res