# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initialize queue, but with root, low and high
        q = deque([(root, float('-inf'), float('inf'))])

        # While there is a queue
        while q:
            # We want to take the current value, the low and the high
            cur, low, high = q.popleft()
            # If the current value is not greater than the low (left) and high (right) return False
            if not (low < cur.val < high):
                return False
            # If there is a left, we append the left to be our current now, and then take low and cur val as the new high
            if cur.left:
                q.append((cur.left, low, cur.val))
            # If right, we take right to be current, the current value to be low and keep high
            if cur.right:
                q.append((cur.right, cur.val, high))
            
        return True