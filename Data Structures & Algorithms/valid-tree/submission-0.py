class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(n)}

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = set()
        # DFS helper function
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for neigh in adjList[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n