class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} # Prerequisite map, For every course initially map to empty list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitS = store all courses along the current DFS path
        visit = set()
        def dfs(crs):
            # There is a loop, so we return false
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                # If it returns false we return false
                if not dfs(pre):
                    return False

            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True