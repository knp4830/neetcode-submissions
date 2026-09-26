class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # Adjacency list to mark edges and a visit list to mark if has been visited
        adj = {i: [] for i in range(n)}
        visit = [False] * n
        
        # Get every node and add its edges (undirected so both ways)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS helper function marks every node reachable from 'node' as visited
        def dfs(node):
            # for every neighbor reachable at the node
            for neigh in adj[node]:
                # If it is False then mark the node as visited and call dfs on it
                if not visit[neigh]:
                    visit[neigh] = True
                    dfs(neigh)

        # Initialize a result variable for components found
        res = 0
        # Go through every node as a starting point (since nodes are 0 to n-1)
        for node in range(n):
            # If the node is not visited (False in the visit)
            if not visit[node]:
                # Make it true and run dfs on it and add to the result
                visit[node] = True
                dfs(node)
                res += 1

        return res 
        