class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            a, b = edges[i] # This returns a = src, b = dst, succProb[i] is of a -> b
            adj[a].append([b, succProb[i]])
            adj[b].append([a, succProb[i]])

        pq = [(-1, start_node)] # We want pair of values, so (Probability, Node)
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            if cur in visit:
                continue
            visit.add(cur) # Don't want to revisit
            # If we get there we return the probability
            if cur == end_node:
                return -prob
            # If we don't find ending node or find a cheaper way
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei)) # To the heapq (pq) push the (probability, node)

        return 0.0
