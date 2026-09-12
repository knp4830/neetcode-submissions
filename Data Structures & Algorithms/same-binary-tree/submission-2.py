# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])
        
        while queue1 and queue2:
            for i in range(len(queue1)):
                curr1 = queue1.popleft()
                curr2 = queue2.popleft()

                if curr1 is None and curr2 is None:
                    continue
                if curr1 is None or curr2 is None or curr1.val != curr2.val:
                    return False

                queue1.append(curr1.left)
                queue2.append(curr2.left)
                queue1.append(curr1.right)
                queue2.append(curr2.right)

        
        return len(queue1) == len(queue2)