# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Something to notice here is we're looking for k smallest, so if we can get a sorted order of the tree
        # We can append to a result from the tree and get teh smallest value by asking return arr[k + 1] since 1 indexed
        # This leads me to thinking that it is Inorder Traversal where we go left root, then right

        # Inorder - Append the left first, then the root, then the right
        stack = []
        cur = root
        res = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        
        return res[k - 1]

        # K = 3 --> [1,2,3,4,5,6,7]