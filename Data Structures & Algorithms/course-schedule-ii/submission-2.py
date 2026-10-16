class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Review
        # Setup (Create Adj List)
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit = set() # Finished: Already in
        path = set() # Current DFS Chain
        topological = [] # What we return

        def dfs(crs):
            if crs in path: # Cycle Detection
                return False
            if crs in visit: # Says we already finished and visited
                return True

            path.add(crs) # Add to path
            for neigh in prereq[crs]:
                if not dfs(neigh): # If theres a cycle (in path)
                    return False
            
            path.remove(crs)
            visit.add(crs)
            topological.append(crs)
            return True

        # Go through every course
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return topological
