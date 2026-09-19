# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Preorder Traversal - First, Left subtree, then right subtree
# What we can do here is add a comma to each node value into the string and for its children if there aren't any we add N to represent
# Null
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Creating an array makes it easier to join
        res = [] 

        # Helper function
        def dfs(node):
            # If it is null we append our special cause N
            if not node:
                res.append("N")
                return
            # Since it is preorder we append the value first and then call dfs on left then right
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        # Call the root and join the array with a ,
        dfs(root)
        return ",".join(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # We split it into an array by the commas
        vals = data.split(",")
        self.i = 0 # Pointer to our array

        # Helper function
        def dfs():
            # If the current array has N we know its a null node we can just return
            if vals[self.i] == "N":
                self.i += 1
                return None

            # Otherwise we create a node for it and increment i
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # We then get our left node and right node by calling dfs again
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

