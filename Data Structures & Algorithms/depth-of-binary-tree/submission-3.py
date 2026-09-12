# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        queue = deque()
        # If it is the root then append it
        if root:
            queue.append(root)
        # Initialize level
        level = 0
        # While the queue is nonempty
        while len(queue) > 0:
            # Go through each level first and append its children
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # After you have gone through and added the children increase the level by 1
            level += 1
        # Return the maximum level you got to
        return level