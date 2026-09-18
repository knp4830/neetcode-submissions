# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Optimal DFS
        # Pre tells us next node to build, forom preorder (root - left - right)
        # inIdx tells us index of how far we've consumed inorder (left - root - right)
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx

            # Ran out of preorder nodes - nothing left to build
            if preIdx >= len(preorder):
                return None
            # We've hit the inorder value that marks the end of current subtree
            # Limit is the value of some ancestor - reaching it inorder
            # means every node belonging to this subtree has already been placed
            if inorder[inIdx] == limit:
                inIdx += 1 # consume that inorder slot (belonging to ancestor)
                return None
            
            # Otherwise, the next preorder value IS the root of this subtree
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            # Build everything that must come before root inorder -
            # That's root's left subtree. It stops once inorder hits root.val
            root.left = dfs(root.val)

            # Build everyting after, still bounded by whatever limit closes off
            # thewhole subtree (root's own limit, inherited form caller)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))