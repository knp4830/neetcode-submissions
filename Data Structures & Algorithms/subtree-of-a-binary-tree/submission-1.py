# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: no subRoot is a subRoot of any
        if not subRoot:
            return True
        # Nonexistent root can't have subtree
        if not root:
            return False
        # Run helper function to check if they have same left and right children
        if self.sameTree(root, subRoot):
            return True
        
        # Compare to see if the subroot is in the left side or right side
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    # Helper function
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the nodes are both null they match!
        if not root and not subRoot:
            return True
        # if they are both present and equal to each other 
        elif (root and subRoot) and root.val == subRoot.val:
            # check if that is true all the way through left and right
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        # If neither cases above pass then it means it isn't a subtree!
        return False
            
