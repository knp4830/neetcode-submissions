class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Build the adjacency list with every point connecting to every other
        # Weighted by manhattan distance. Which will replace the "edges" input
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        
        # Prim's algorithm
        minHeap = [[0,0]]
        visit = set()
        total = 0
        while len(visit) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            total += cost
            visit.add(node)
            for nei, w in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [w, nei])

        return total

        
