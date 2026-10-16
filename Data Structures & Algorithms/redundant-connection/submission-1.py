class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS version
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True
            
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for src, dst in reversed(edges):
            if src in cycle and dst in cycle:
                return [src, dst]
        
        return []