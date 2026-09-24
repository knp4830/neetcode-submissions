"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a hashmap/adjencency list
        adjList = {}

        # Helper dfs (Nested so we don't need to pass adjList)
        def dfs(node):
            # If node in hashmap we already have clone
            if node in adjList:
                return adjList[node]
            
            # Create copy of node and add it to the hashmap
            copy = Node(node.val)
            adjList[node] = copy

            # Take copy of new node and take its list of neighbors the dfs call and return the copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy

        # Call dfs if there is a node and return the copy, else there isn't one
        return dfs(node) if node else None
