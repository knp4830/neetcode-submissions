class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            adjList[crs].append(preq)

        visit = set()
        def dfs(crs):
            if crs in visit:    # That means we've already seen it
                return False
            
            if adjList[crs] == []:  # No more prerequisites left
                return True
            
            visit.add(crs)
            for preq in adjList[crs]:
                if not dfs(preq):
                    return False
            
            visit.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True