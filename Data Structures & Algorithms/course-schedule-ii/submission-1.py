class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}     # Create Adjacency List 
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visit = set()               # finished: already in topSort
        path = set()                # Current DFS Chain
        topSort = []

        def dfs(crs):
            if crs in path:         # Checks for Cycle
                return False
            if crs in visit:        # Says we already finished and visited
                return True

            path.add(crs)           # Add to path
            for neighbor in prereq[crs]:        # Check every neighbor
                if not dfs(neighbor):           # Pass the Cycle up
                    return False
            path.remove(crs)                        # Remove from current path
            visit.add(crs)                      # Add to visited
            topSort.append(crs)                 # Append
            return True

        for crs in range(numCourses):           # Go through every course
            if not dfs(crs):
                return []
        return topSort
                

    
    