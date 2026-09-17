# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root, left, right
        stack = []
        curr = root
        res = []
        # While the stack is non empty or there is a node
        while curr or stack:
            # If there is a node
            if curr:
                # append it to the value
                res.append(curr.val)
                # If theres a right child append it
                if curr.right:
                    stack.append(curr.right)
                # Move to the left child
                curr = curr.left
            # If the left child is null pop back up
            else:
                curr = stack.pop()
        
        # Return the result
        return res 