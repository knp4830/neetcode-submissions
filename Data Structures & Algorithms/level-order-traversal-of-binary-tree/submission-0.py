# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #Initialize a result array that will store the levels
        # start off with the base case, if there is no root then you return the result
        # you start off with a queue that stores the root
        # Then you go through a while loop that keeps track of the level that you are on
        # you append the root node to the level such that you can pop it to the result
        # from there you check if the root has a left child or right child and you append that to the queue
        # you repeat until there are no children left
        # then you return the result that should have the level order traversal.

        result = []

        if not root:
            return result

        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)

        return result
