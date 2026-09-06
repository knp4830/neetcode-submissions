class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                l = 0
                h = len(matrix[mid]) - 1
                while l <= h:
                    middle = l + (h - l) // 2

                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        l = middle + 1
                    else:
                        h = middle - 1
                return False
        return False