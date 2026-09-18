# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Optimal BFS
        res = []
        # Create queue and append root
        q = collections.deque()
        q.append(root)

        # While the queue is nonempty
        while q:
            level = [] # Create a list for the level
            for i in range(len(q)): # Go through all the nods
                node = q.popleft() # Pop them
                # If there is a node, append the value to the level, then its children to the queue.
                if node: 
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # If the list is nonempty we append to the result the level
            if level:
                res.append(level)

        return res