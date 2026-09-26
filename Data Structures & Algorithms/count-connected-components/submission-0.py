class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # Find parent helper
        def find(n1):
            res = n1
            # While the node is not its own parent
            while res != par[res]:
                # Path compression
                par[res] = par[par[res]]
                # We want to find the parent
                res = par[res]
            # And return the parent
            return res
        
        # Union Helper
        def union(n1, n2):
            # Find the parents of node1 and node2
            p1, p2 = find(n1), find(n2)

            # If they have the same parents we return immediately
            if p1 == p2:
                return 0

            # Union by rank
            # If parent2 is higher then parent of p1 becomes p2, else opposite, add 1 to rank
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
            