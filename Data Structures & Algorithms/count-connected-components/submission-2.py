class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS
        # Adjacency list to mark edges and a visit list to mark if has been visited
        adj = {i: [] for i in range(n)}
        visit = [False] * n
        
        # Get every node and add its edges (undirected so both ways)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for neigh in adj[cur]:
                    if not visit[neigh]:
                        visit[neigh] = True
                        q.append(neigh)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1

        return res 