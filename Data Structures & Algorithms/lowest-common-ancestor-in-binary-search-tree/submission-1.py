# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            # If both are smaller than the current we continue left
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # If both are bigger then we continue right
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # Otherwise it means they go separate ways meaning this the their most common ancestor
            else:
                return cur